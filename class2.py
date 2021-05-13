import time
import requests
import csv
from bs4 import BeautifulSoup

# 目標URL網址
URL = "https://kiki.ccu.edu.tw/~ccmisp06"
url1 = "https://kiki.ccu.edu.tw/~ccmisp06/Course/index.html"

def generate_urls(url, departments):
    urls = []
    for department in departments:
        urls.append(url + department)
    return urls

def get_resource(url):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
               "AppleWebKit/537.36 (KHTML, like Gecko)"
               "Chrome/63.0.3239.132 Safari/537.36"}
    return requests.get(url, headers=headers) 

def parse_html(html_str):
    return BeautifulSoup(html_str, "lxml")

def get_course4(soup,course_of_study):
    courses4 = []
    rows = soup.find_all("tr")
    first = False
    i=0
    for row in rows:
        if(first):
            department = row.select("td")[0].text
            course_id = row.select("td")[1].text
            subject = row.select("td")[2].text
            credit = row.select("td")[3].text
            course = [course_of_study[i],department,course_id,subject,credit]
            courses4.append(course)
            i+=1
        else:
            first = True
    return courses4
def save_to_csv(items, file):
    with open(file, "w+", newline="", encoding="utf-8") as fp:
        writer = csv.writer(fp)
        for item in items:
            writer.writerow(item)

def web_scraping_bot(urls,course_of_study):
    courses4 = [["學程","開課系所","科目代碼","科目名稱","學分"]]
    for url in urls:
        r = get_resource(url)
        r.encoding = "utf-8"
        if r.status_code == requests.codes.ok:
            soup = parse_html(r.text)
            course4 = get_course4(soup,course_of_study)
            courses4 = courses4 + course4
            print("等待2秒鐘...")
            time.sleep(2) 
        else:
            print("HTTP請求錯誤...")
    return courses4

def get_department(url1):
    colleges = []
    r = get_resource(url1)
    r.encoding = "utf-8"
    course_of_study=[]
    if r.status_code == requests.codes.ok:
        soup = parse_html(r.text)
        departments = []
        rows = soup.find_all("td")
        first = 0
        for row in rows:
            if(first==10):
                colleges = row.select("font")[0].select("a")
                x=row.select("font")[0].text
                course_of_study=x.split()
                for college in colleges:
                    department = college['href']  
                    a = department[2:]
                    departments.append(a)
                first = first + 1
            else:
                first = first + 1
        print("等待2秒鐘...")
        time.sleep(2) 
    else:
        print("HTTP請求錯誤...") 
    return departments,course_of_study

if __name__ == "__main__":
    URL1,course_of_study = get_department(url1)
    urls = generate_urls(URL, URL1)
    courses4 = web_scraping_bot(urls,course_of_study)
    save_to_csv(courses4, "cross_domain.csv")
