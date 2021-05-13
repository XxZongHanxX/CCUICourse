import time
import requests
import csv
from bs4 import BeautifulSoup

# 目標URL網址
URL = "https://kiki.ccu.edu.tw/~ccmisp06/Course/"
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

def get_course(soup,academys):
    courses = []
    rows = soup.find_all("tr")
    de = soup.find("h1").font.text
    d = de.split(" ")[-1]
    first = False
    for row in rows:
        if(first):
            grade = row.select("td")[0].select_one('font').text
            course_id = row.select("td")[1].select_one('font').text
            course_class = row.select("td")[2].select_one('font').text
            subject = row.select("td")[3].select_one('font').text
            subject_chinese=""
            subject_english=""
            j=0
            for i in subject:
                if (u'\u0041'<= i <= u'\u005a') or (u'\u0061'<= i <= u'\u007a'):
                    if(subject[j+1]=="組"):
                        j=j+2
                    subject_chinese = subject[:j]
                    if(subject[-28:-21]=="程式設計相關/"):
                        print(subject[-51:-45])
                        if(subject[-51:-45]=="全英語授課/"):
                            subject_chinese += " (全英語授課) (程式設計相關)"
                            subject_english = subject[j:-51] + subject[-45:-28] + subject[-21:]
                        else:
                            subject_chinese += " (程式設計相關)"
                            subject_english = subject[j:-28] + subject[-21:]
                    elif(subject[-23:-17]=="全英語授課/"):
                        subject_chinese += " (全英語授課)"
                        subject_english = subject[j:-23] + subject[-17:]
                    else:
                        subject_english = subject[j:]
                    break
                j=j+1
            teacher = row.select("td")[4].select_one('font').text
            course_hour = row.select("td")[5].select_one('font').text
            course_hour1 = (course_hour.split(" ")[0])[0]
            course_hour2 = course_hour.split(" ")[-1]
            credit = row.select("td")[6].select_one('font').text
            course_type = row.select("td")[7].select_one('font').text
            course_time = row.select("td")[8].select_one('font').text
            course_place = row.select("td")[9].select_one('font').text
            population = row.select("td")[10].select_one('font').text
            syllabus = row.select("td")[11].select_one('a')
            syllabus = syllabus['href']
            other = row.select("td")[12].select_one('font').text
            course = [academys,d,grade,course_id,course_class,subject,subject_chinese,subject_english,teacher,course_hour1,course_hour2,credit,course_type,course_time,course_place,population,syllabus,other]
            courses.append(course)
        else:
            first = True
    return courses

def get_course2(soup,academys):
    courses = []
    rows = soup.find_all("tr")
    de = soup.find("h1").font.text
    d = de.split(" ")[-1]
    first = False
    for row in rows:
        if(first):
            grade = row.select("td")[0].select_one('font').text
            course_id = row.select("td")[1].select_one('font').text
            course_class = row.select("td")[2].select_one('font').text
            subject = row.select("td")[3].select_one('font').text
            subject_chinese=""
            subject_english=""
            j=0
            for i in subject:
                if (u'\u0041'<= i <= u'\u005a') or (u'\u0061'<= i <= u'\u007a'):
                    if(subject[j+1]=="組"):
                        j=j+2
                    subject_chinese = subject[:j]
                    if(subject[-28:-21]=="程式設計相關/"):
                        if(subject[-51:-45]=="全英語授課/"):
                            subject_chinese += " (全英語授課) (程式設計相關)"
                            subject_english = subject[j:-51] + subject[-45:-28] + subject[-21:]
                        else:
                            subject_chinese += " (程式設計相關)"
                            subject_english = subject[j:-28] + subject[-21:]
                    elif(subject[-23:-17]=="全英語授課/"):
                        subject_chinese += " (全英語授課)"
                        subject_english = subject[j:-23] + subject[-17:]
                    else:
                        subject_english = subject[j:]
                    break
                j=j+1
            teacher = row.select("td")[4].select_one('font').text
            course_hour = row.select("td")[5].select_one('font').text
            course_hour1 = (course_hour.split(" ")[0])[0]
            course_hour2 = course_hour.split(" ")[-1]
            credit = row.select("td")[6].select_one('font').text
            course_type = row.select("td")[7].select_one('font').text
            course_time = row.select("td")[8].select_one('font').text
            course_place = row.select("td")[9].select_one('font').text
            population = row.select("td")[10].select_one('font').text
            school_system = row.select("td")[11].select_one('font').text
            syllabus = row.select("td")[12].select_one('a')
            syllabus = syllabus['href']
            other = row.select("td")[13].select_one('font').text
            course = [academys,d,grade,course_id,course_class,subject,subject_chinese,subject_english,teacher,course_hour1,course_hour2,credit,course_type,course_time,course_place,population,school_system,syllabus,other]
            courses.append(course)
        else:
            first = True
    return courses

def get_course3(soup,academys):
    courses = []
    rows = soup.find_all("tr")
    de = soup.find("h1").font.text
    d = de.split(" ")[-1]
    first = False
    for row in rows:
        if(first):
            grade = row.select("td")[0].select_one('font').text
            dimension = row.select("td")[1].text
            course_id = row.select("td")[2].select_one('font').text
            course_class = row.select("td")[3].select_one('font').text
            subject = row.select("td")[4].select_one('font').text
            subject_chinese=""
            subject_english=""
            j=0
            for i in subject:
                if (u'\u0041'<= i <= u'\u005a') or (u'\u0061'<= i <= u'\u007a'):
                    if(subject[j+1]=="組"):
                        j=j+2
                    subject_chinese = subject[:j]
                    if(subject[-28:-21]=="程式設計相關/"):
                        if(subject[-51:-45]=="全英語授課/"):
                            subject_chinese += " (全英語授課) (程式設計相關)"
                            subject_english = subject[j:-51] + subject[-45:-28] + subject[-21:]
                        else:
                            subject_chinese += " (程式設計相關)"
                            subject_english = subject[j:-28] + subject[-21:]
                    elif(subject[-23:-17]=="全英語授課/"):
                        subject_chinese += " (全英語授課)"
                        subject_english = subject[j:-23] + subject[-17:]
                    else:
                        subject_english = subject[j:]
                    break
                j=j+1
            teacher = row.select("td")[5].select_one('font').text
            course_hour = row.select("td")[6].select_one('font').text
            course_hour1 = (course_hour.split(" ")[0])[0]
            course_hour2 = course_hour.split(" ")[-1]
            credit = row.select("td")[7].select_one('font').text
            course_type = row.select("td")[8].select_one('font').text
            course_time = row.select("td")[9].select_one('font').text
            course_place = row.select("td")[10].select_one('font').text
            population = row.select("td")[11].select_one('font').text
            syllabus = row.select("td")[12].select_one('a')
            syllabus = syllabus['href']
            other = row.select("td")[13].select_one('font').text
            course = [academys,d,grade,dimension,course_id,course_class,subject,subject_chinese,subject_english,teacher,course_hour1,course_hour2,credit,course_type,course_time,course_place,population,syllabus,other]
            courses.append(course)
        else:
            first = True
    return courses

def save_to_csv(items, file):
    with open(file, "w+", newline="", encoding="utf-8") as fp:
        writer = csv.writer(fp)
        for item in items:
            writer.writerow(item)

def web_scraping_bot(urls,academys):
    courses = [["學院","系所","年級","編號","班別","科目名稱","科目名稱_中文","科目名稱_英文","任課教授","上課時數","正課/實驗實習/書報討論","學分","選必","上課時間","上課地點","限修人數","課程大綱","備註"]]
    courses2 = [["學院","系所","年級","編號","班別","科目名稱","科目名稱_中文","科目名稱_英文","任課教授","上課時數","正課/實驗實習/書報討論","學分","選必","上課時間","上課地點","限修人數","開課學制","課程大綱","備註"]]
    courses3 = [["學院","系所","領域","向度","編號","班別","科目名稱","科目名稱_中文","科目名稱_英文","任課教授","上課時數","正課/實驗實習/書報討論","學分","選必","上課時間","上課地點","限修人數","課程大綱","備註"]]
    a = len(urls)
    b = 0
    for url in urls:
        r = get_resource(url)
        r.encoding = "utf-8"
        if r.status_code == requests.codes.ok:
            soup = parse_html(r.text)
            if(b!=a-3):
                rows = soup.find_all("tr")
                school_system = rows[0].select("th")[11].select_one('font').text
                if(school_system==' 開課學制'):
                    course2 = get_course2(soup,academys[b])
                    courses2 = courses2 + course2
                else:
                    course = get_course(soup,academys[b])
                    courses = courses + course
                b = b + 1
                
            else:
                course3 = get_course3(soup,academys[b])
                courses3 = courses3 + course3
                b = b + 1
            print("等待2秒鐘...")
            time.sleep(2) 
        else:
            print("HTTP請求錯誤...")
    return courses,courses2,courses3

def get_department(url1):
    colleges = []
    r = get_resource(url1)
    r.encoding = "utf-8"
    if r.status_code == requests.codes.ok:
        soup = parse_html(r.text)
        departments = []
        academys = []
        rows = soup.find_all("td")
        first = 0
        for row in rows:
            if(first<10 and first>1):
                colleges = row.select("font")[0].select("a")
                for college in colleges:
                    department = college['href']  
                    departments.append(department)
                    a=department.split(".")
                    b=a[0]
                    c=b[0]
                    if (c=='1'):
                        academys.append("文學院");
                    elif(c=='2'):
                        academys.append("理學院");
                    elif(c=='3'):
                        academys.append("社會科學學院");
                    elif(c=='4'):
                        academys.append("工學院");
                    elif(c=='5'):
                        academys.append("管理學院");
                    elif(c=='6'):
                        academys.append("法學院");
                    elif(c=='7'):
                        academys.append("教育學院");
                    else:
                        academys.append("其他");
                first = first + 1
            else:
                first = first + 1
        print("等待2秒鐘...")
        time.sleep(2) 
    else:
        print("HTTP請求錯誤...") 
    return departments,academys

if __name__ == "__main__":
    URL1,academys = get_department(url1)
    urls = generate_urls(URL, URL1)
    courses,courses2,courses3 = web_scraping_bot(urls,academys)
    save_to_csv(courses, "bachelor_courses.csv")
    save_to_csv(courses2, "master_courses.csv")
    save_to_csv(courses3, "general_courses.csv")
