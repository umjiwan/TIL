# Github MarkDown TIL 만들기
깃허브 레파지토리를 TIL로 활용하는걸 목적으로<br>
가장 앞 README.md에 목차를 자동적으로 작성해주는<br>
파이썬 프로그램을 만들기 위한 과정.<br>

### 목표
post라는 폴더에 양식에 맞는 파일이름의 마크다운 파일들이 있을 때<br>
그 파일들을 작성한 날에 따라서 정렬하고 파일들의 제목을 볼 수 있는<br>
README.md(목차)가 자동적으로 작성 되는 deploy.py를 만든다.

## 1. 파이썬으로 파일 읽고 쓰기
```python
file = open("test.txt", "r")
a = file.read()

file.close()
```
이런 양식으로 쓴다.<br>

위의 코드는 test.txt이란 파일의 내용을 a태그에 저장한다.

`test.txt` 에는 작성을 원하는 파일 이름 즉 경로를 작성해주고<br>
`r` 에는 읽기, 쓰기 등등의 필요한 기능에 따른 옵션이 오면 된다.<br>

#
option<br>

`r`: 파일을 읽기 위할때 사용<br>
`w`: 파일을 작성할때 사용<br>
`a`: 파일이 초기화 되는 `w`와 다르게<br> 
기존 파일 내용이 유지된 상태로 내용을 덧붙인다.<br>
#

파일을 열었으면 마지막에 `f.close()`로 무조건 닫아주어야 한다.<br>

하지만 프로그램이 오류가 나서 중간에 종료되거나 했을때를 대비하여<br>
`with`문을 써주는 것이 바람직하다.<br>

```python
with open("filename", "option") as file:
    a = file.read()
```
처음에 작성한 코드와 동일한 기능을 수행한다.<br>
하지만 프로그램이 종료되거나 하는 돌발 상황에도 알아서<br>
파일을 닫아준다.

자세한 함수, 옵션은 <a target="_blank" href="https://wikidocs.net/26">이곳</a> 참고<br>

TIL 맨위 글을 작성하기 위해<br>
```python
start = "# 유엘 개발일지 - TIL\n\
`email`: ulhangr\y@gmail.com\n\
### 배포\n```\npython deploy.py \n```"

with open("README.md", "w") as file:
    file.write(start)
```
이렇게 작성하여 주었다.

## 2. 작성된 마크다운 날짜순으로 정렬
먼저 파일들의 이름에 대한 정보를 가져오기 위해서<br>
```python
import os

post_name_list = os.listdir("post/")
```
이렇게 작성하여 주었다.<br>
post_name_list에는 post폴더 안에 담긴 파일이름들이 리스트 형식으로 되어있다.<br>

파일들의 제목 양식을 0000-00-00-title.md 로 정해주었다.<br>
방법은 2022-01-22-test.md 라는 파일이 있다면<br>

2022-01-22 부분만 가져와 20220122 로 변환 해준다<br>
만약 2022-01-13 이라는 파일이 있다면 20220113 이기 때문에<br>
더큰 숫자부터 정렬 시켜주면 된다.<br>

그리고 숫자들과 파일들의 이름을 대조시켜 해당한 파일을<br>
가져와 순서대로 정렬하면 파일들이 날짜별로 정렬된다.<br>

```python
date_list = []
for post_name in post_name_list:
    date = int(post_name[:10].replace("-", ""))
    date_list.append(date)
```

아까 저장한 파일이름들에서 날짜만 추출해준다.<br>

```python
date_list.sort() # 정렬
date_list.reverse() # 리스트 순서 뒤집기
```
최근에 작성된 날짜가 위에 올라가는것을 원하기 때문에 .reverse()로 한번 뒤집어 준다.<br>

```python
str_date_list = []
year_list = []

for date in date_list:
    # 아까 해체한 날짜 (20220202) 를 다시 2022-02-02로 만들어 준다
    date = str(date)
    date = date[:4] + "-" + date[4:6] + "-" + date[6:]
    str_date_list.append(date)
    # 나중에 쓸 연도 리스트도 만들어 준다.
    year_list.append(int(date[:4]))

year_list = list(set(year_list)) # 정렬, 중복제거
year_list.reverse() # 순서 뒤집기
```

원래 파일 이름들과 대조 시키기 위해 아까 변형한 애들을 다시 원래<br>
형식으로 돌려준다.<br>

```python
set_post_name_list = []

for str_date in str_date_list:
    for post_name in post_name_list:
        # 날짜와 파일명의 날짜가 같다면 리스트에 추가한다
        # 즉 순서대로 정렬한다.
        if post_name[:10] == str_date: 
            set_post_name_list.append(post_name)
```
이렇게 정렬이 완료 되었다.<br>

## 3. 마크다운 목차 작성

마크다운을 앞의 값들로 날짜별로 정렬되어있는<br>
목차를 자동작성 해주는 것을 구현해보자<br>

```python
before_year = ""

with open("README.md", "a") as file:
    for set_post_name in set_post_name_list:
        title = set_post_name[11:-3].replace("-", " ") # 제목 얻기
        date  = set_post_name[5:10].replace("-", ". ") # 날짜 얻기
        if before_year != set_post_name[:4]:
            before_year = set_post_name[:4]
            file.write(f"\n## {before_year}<br>\n")

        # 양식대로 작성
        file.write(f'<a href="https://github.com/umjiwan/TIL/blob/main/post/{set_post_name}">{title}</a> - <i>{date}</i><br>\n')
        
```

이렇게 자동적으로 README 목차를 쓰는 것 까지 완료했다.<br>
이제 이걸 모두 add, commit, push 해주자.<br>

## 파이썬으로 콘솔 명령어 사용하기
가능하다
```python
import os

os.system("원하는 콘솔 명령어")
```
이렇게 해주면 셸에서 사용 가능한 명령어를 사용할 수 있다.<br>
이를 응용해서 깃허브 커밋을 반자동으로 할 수 있다.

```python
os.system("git add .")
os.system("git commit -m \"Auto Upload\"")
os.system("git push")
```

이제 모두 완료되었다.<br>

### 전체 소스코드
```python
import os

start = "# 유엘 개발일지 - TIL\n\
`email`: ulhangr\y@gmail.com\n\
### 배포\n```\npython deploy.py \n```"

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
        date  = set_post_name[5:10].replace("-", ". ")
        if before_year != set_post_name[:4]:
            before_year = set_post_name[:4]
            file.write(f"\n## {before_year}<br>\n")

        file.write(f'<a href="https://github.com/umjiwan/TIL/blob/main/post/{set_post_name}">{title}</a>\
                         - <i>{date}</i>\
                        <br>\n\
                    ')

os.system("git add .")
os.system("git commit -m \"Auto Upload\"")
os.system("git push")
```

끝



