# -*- coding: utf-8 -*-

from audioop import reverse
import os

start = "# 유엘 개발일지 - TIL\n`email`: ulhangry@gmail.com\n"

with open("README.md", "w") as file:
    file.write(start)

post_name_list = os.listdir("post/")

date_list = []
for post_name in post_name_list:
    date = int(post_name[:10].replace("-", ""))
    date_list.append(date)

date_list.sort()
date_list.reverse()
str_date_list = []
year_list = []

for date in date_list:
    date = str(date)
    date = date[:4] + "-" + date[4:6] + "-" + date[6:]
    str_date_list.append(date)
    year_list.append(int(date[:4]))

year_list = list(set(year_list))
year_list.reverse()

set_post_name_list = []

for str_date in str_date_list:
    for post_name in post_name_list:
        if post_name[:10] == str_date:
            set_post_name_list.append(post_name)

before_year = ""

with open("README.md", "a") as file:
    for set_post_name in set_post_name_list:
        title = set_post_name[11:-3].replace("-", " ")
        if before_year != set_post_name[:4]:
            before_year = set_post_name[:4]
            file.write(f"\n## {before_year}<br>\n")
        file.write(f'<a style="color:white" href="https://github.com/umjiwan/TIL/blob/main/post/{set_post_name}">{title}</a><br>\n')

os.system("git add .")
os.system("git commit -m \"Auto Upload\"")
os.system("git push")