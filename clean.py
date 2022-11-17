import re

electives = open("electives.txt").read()
course_names = re.findall(r"[A-Z ]+ [A-Z]?[\d]{1,3}[A-Z]?", electives)
course_names_clean = [re.sub(r" ", r"-", name) for name in course_names]
# course_names_clean = [re.sub(r"[A-Z]-[A-Z]", r"", name) for name in course_names_clean]
print(course_names_clean)
# print(course_names)
# print(electives)