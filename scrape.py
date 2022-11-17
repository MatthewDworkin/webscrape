import requests
import re

BASE_URL = "https://classes.berkeley.edu/content/"
SEMESTER = "2022-fall-"
END = "-001-lec-001"
electives = open("electives.txt").read()
course_names = re.findall(r"[A-Z ]+ [A-Z]?[\d]{1,3}[A-Z]?", electives)
courses = [re.sub(r" ", r"-", name) for name in course_names]
courses = [re.sub(r"IND-ENG", r"INDENG", name) for name in courses]
courses = {course: 0 for course in courses}
years = ["2022", "2021", "2020", "2019", "2018"]
semesters = ["-fall-", "-spring-"]
breadths = ["International Studies", "Historical Studies", "Philosophy & Values", 
"Physical Science", "Biological Science", "Social & Behavioral Sciences", "Arts & Literature"]
breadth_satisfying = {breadth: [] for breadth in breadths}

for course in courses:
    for year in years:
        for sem in semesters:
            page = requests.get(BASE_URL+year+sem+course+END)
            if not page.text:
                print("ERROR: COURSE NOT FOUND IN SEM ", sem)
                continue
            if courses[course]:
                # print("Skipped: ", course)
                continue
            for breadth in breadths:
                x = re.findall(r"Meets " + breadth + r".{0,30} L&S Breadth", page.text)
                if x:
                    courses[course] += len(x) / 2
                    breadth_satisfying[breadth].append(course)
                    # print(course, x[0], "in", sem[1:len(sem)-1], year)
            
for breadth in breadth_satisfying:
    print(breadth)
    for course in breadth_satisfying[breadth]:
        print(course)
