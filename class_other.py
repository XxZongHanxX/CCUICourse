from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import requests
import time

def get_resource(url):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
               "AppleWebKit/537.36 (KHTML, like Gecko)"
               "Chrome/63.0.3239.132 Safari/537.36"}
    return requests.get(url, headers=headers) 

def parse_html(html_str):
    return BeautifulSoup(html_str, "lxml")


def get_other(soup):
    a,b,c = soup.find_all("table")
    subject = a.select("td")[0].text
    course_id = a.select("td")[1].text
    course_class = a.select("td")[2].text
    population = b.select("tr")[0].select("td")[0].text
    support_department = b.select("tr")[1].select("td")[0].text
    support_grade = b.select("tr")[2].select("td")[0].text
    support_class = b.select("tr")[3].select("td")[0].text
    block_department = b.select("tr")[4].select("td")[0].text
    block_grade = b.select("tr")[5].select("td")[0].text
    block_class = b.select("tr")[6].select("td")[0].text
    keep = b.select("tr")[7].select("td")[0].text
    select_rule = b.select("tr")[8].select("td")[0].text
    support_general_subject = b.select("tr")[9].select("td")[0].text
    support_general_population = b.select("tr")[10].select("td")[0].text
    prerequisite = b.select("tr")[11].select("td")[0].text
    remark = b.select("tr")[12].select("td")[0].text
    others = [[subject,course_id,course_class,population,support_department,support_grade,support_class,block_department,block_grade,block_class,keep,select_rule,support_general_subject,support_general_population,prerequisite,remark]]
    time.sleep(1)
    return others


driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://kiki.ccu.edu.tw/~ccmisp06/cgi-bin/Query/Query_by_time1.cgi?session_id=HqDYi8eAqCcv17eaYZdcjwstR5lGJ4gRI864&get_my_table=1")
driver.find_element_by_xpath("//*[@id='form1']/table/tbody/tr[1]/td[2]/input[2]").click()
driver.find_element_by_xpath("//*[@id='form1']/center/input[1]").submit()

# 使用Beautiful Soup剖析HTML網頁
soup = BeautifulSoup(driver.page_source, "lxml")
rows = soup.find_all("tr") 
wes=[]
i=0
j=0
for row in rows:
    if(i>2):
        a=row.select("td")[10].text
        if(a=="有"):
            b = row.select("td")[10].select_one("a")
            wes.append(b['href'])
            i=i+1
    else:
        i=i+1
print(i)
others = [["科目","代碼","班別","限修人數","支援系所","支援年級","支援班別","擋修系所","擋修年級","擋修班別","保留本系名額","篩選原則","支援通識科目","支援通識人數","先修科目","其他備註"]]
for we in wes:
    r = get_resource(we)
    r.encoding = "utf-8"
    if r.status_code==requests.codes.ok:
        soup = parse_html(r.text)
        other = get_other(soup)
        others = others + other
    j=j+1
    print(j)
with open("others.csv", "w+", newline="", encoding="utf-8") as fp:
    writer = csv.writer(fp)
    for other in others:
        writer.writerow(other)