# 리눅스 기본 명령어

리눅스에서 많이 사용되는 기본적인 명령어들



#### pwd

`pwd`는 print working directory의 준말이다.

현재 작업중인 경로를 보여준다.

**예제**

```bash
$ pwd
/home/ulhangry
```



#### ls

`ls`는 list segments의 준말이다.

파일의 목록을 출력하는 기능을 수행한다.



**형식**

```bash
$ ls 옵션 경로
```

| 옵션 | 설명                                   |
| :--: | -------------------------------------- |
|  -l  | 롱 포맷.                               |
|  -f  | 정렬 안함.                             |
|  -F  | 파일의 본질을 나타내는 문자 추가       |
|  -a  | "."으로 시작하는 이름을 포함           |
|  -R  | 하부 디렉터리를 반복하여 나열          |
|  -d  | 심볼 링크나 디렉터리에 대한 정보 표시  |
|  -t  | 수정 시간에 따라 파일 목록을 나열      |
|  -h  | 사람이 인지할 수 있는 크기 형대로 출력 |



#### cd

`cd`는 change directiontory 의 준말이다.

디렉터리를 이동하는 명령어 이다.



**형식**

```bash
$ cd 경로
```



#### mkdir

`mkdir`는 make directory 의 준말.

디렉터리를 생성하는 명령어이다.



**형식**

```bash
$ mkdir 옵션 경로/디렉터리이름
```

| 옵션 | 설명                                                  |
| :--: | ----------------------------------------------------- |
|  -m  | 디렉터리를 생성할때 권한을 설정 기본값은 755          |
|  -p  | 상위 경로도 함께 생성                                 |
|  -v  | 디렉터리를 생성 후 생성된 디렉터리에 대해 메세지 출력 |



#### which

명령어의 경로를 확인하는 명령어이다.

명령어의 위치를 찾아주거나 `alias`를 보여준다.

사용자가 현재 위치에서 명령을 실행했을 때 어떤 명령이 실행되는지를 알고 확인할 수 있다.

`$PATH`가 설정되어 있는 경로에서만 해당 명령어의 경로를 찾는다.



**형식**

```bash
which 명령어
```

**예제**

```bash
$ which httpd
/usr/sbin/httpd
```

```bash
$ which test
alias test='ls -al | more'
		/bin/ls
		/bin/more
```



#### alias

자주 사용하는 명령어를 단축어로 설정해 명령어 대신 해당 단축어를 사용할 수 있게 하는 명령어이다.



**형식**

```bash
$ alias 단축어='명령어'
```

**예제**

명령어 `ls -al | more` 를 문자 `test`로 단축시킨다.

```bash
$ alias test='ls -al | more' 
```



#### unalias

alias에 설정한 단축어를 해제한다.



**형식**

```bash
$ unalias 단축어
```

**예제**

test 단축어를 해제한다.

```bash
$ unalias test
```



#### man

리눅스에서 사용하는 명령어들의 메뉴얼을 제공해준다.



**형식**

```bash
$ man 섹션 옵션 명령어
```



**섹션**은 1~9까지의 번호로 구분되어 해당 섹션에서 해당 정보들을 확인할 수 있다.



| 섹션 | 설명                                                         |
| :--: | :----------------------------------------------------------- |
|  1   | 일반 명령어 관련 매뉴얼이 들어있는 영역                      |
|  2   | 시스템 호출 관련 매뉴얼이 들어있는 영역                      |
|  3   | C 표준 라이브러리 함수 관련 매뉴얼이 들어있는 영역           |
|  4   | 장치 드라이버 또는 특수 파일에 대한 정보가 들어있는 영역     |
|  5   | 특정 파일들에 대한 정보가 들어있는 영역                      |
|  6   | 게임과 화면보호기에 대한 정보가 들어있는 영역                |
|  7   | 리눅스 파일 표준, 프로토콜, 시그널 목록 정보가 들어있는 영역 |
|  8   | 시스템 관리 명령어와 데몬 정보가 들어있는 영역               |
|  9   | 커널 관리 정보가 들어있는 영역                               |

| 옵션 | 설명                                                  |
| :--: | ----------------------------------------------------- |
|  -a  | 찾고자 하는 명령어의 검색된 매뉴얼 페이지를 모두 출력 |
|  -h  | 사용법을 출력                                         |
|  -f  | 키워드와 동일한 man 페이지만 출력                     |
|  -k  | 키워드가 포함된 man 페이지 출력                       |
|  -w  | 찾고자 하는 문자의 매뉴얼 페이지가 있는 위치를 출력   |

**예제**

`uname`의 모든 `man` 페이지 섹션을 표시

```bash
$ man -a uname
```



`uname`의 섹션 2의 man 페이지를 표시

```bash
$ man 2 uname
```



`uname`의 `man` 페이지를 `more` 명령을 사용하여 페이지 단위로 표시

```bash
$ man uname -P more 
```



`uname`이 포함된 `man` 페이지 표시

```bash
$ man -f uname
```



#### info

리눅스 명령어의 사용 방법, 옵션 등을 나타낸다.

명령어 `man`에 비해 제공되는 명령어가 한정적이다.



**형식**

```bash
$ info 명령어
```



#### whatis

명령어에 대한 기능을 간략하게 나타낸다.

자세한 사용법과 설명은 명령어 `man`이나 `info`로 확인해야 한다.

완전히 키워드가 일치해야만 해당 명령어의 기능을 확인할 수 있다.

`whatis` 데이터베이스에서 문자열만 검색한다.



**형식**

```bash
$ whatis 명령어
```



#### manpath

`man` 페이지의  위치 경로를 검색하여 표시해 주는 명령어이다.



**형식**

```bash
$ manpath 명령어
```



**예제**

`man` 명령이 참조하는 매뉴얼 페이지의 경로를 표시한다.

```bash
$ manpath
/usr/local/share/man:/usr/share/man/overrides:/usr/share/man
```



#### whereis 

찾고자 하는 명령어의 실행 파일 절대 경로와 소스코드, 설정 파일 및 매뉴얼 페이지를 찾아 출력하는 명령어이다.



**형식**

```bash
$ wheris 옵션 명령어
```



| 옵션 | 설명                          |
| :--: | :---------------------------- |
|  -b  | 바이너리 파일만 찾음          |
|  -m  | 지정된 매뉴얼 섹션에서만 찾음 |
|  -M  | 매뉴얼 페이지의 위치를 제한   |
|  -u  | 특정 파일을 제외              |



**예제**

명령어 `shutdown` 의 소스 파일 위치나 매뉴얼 페이지의 위치 정보를 출력한다.

```bash
$ whereis shutdown
shutdown: /usr/sbin/shutdown /usr/share/man/man2/shutdown.2.gz
/usr/share/man/man3p/shutdown.3p.gz /usr/share/man/man8/shutdown.8.gz
```



#### apropos

`man` 페이지 설명에서 지정한 키워드를 포함하고 있는 명령어이다.

`whatis` 데이터베이스에서 문자열을 포함한 것을 검색한다.

`whatis` 데이터베이스가 만들어져 있어야 이 명령을 쓸 수 있다.



**형식**

```bash
$ apropos 문자열
```



**예제**

명령어 매뉴얼에서 `system` 이 포함된 명령어 목록을 출력한다.

```bash
$ apropos system
```



`system` 으로 시작하는 명령어를 찾는다.

```bash
$ apropos system | grep ^system
```



#### useradd

계정을 생성하는 명령어로 명령어 `adduser` 과 같은 기능을 수행한다.

계정자의 홈 디렉터리는 `"/home/계정명"` 이다.

생성된 계정 정보는 파일 `"etc/password"`, `"etc/shadow"`, `"/etc/group"` 에 저장된다.



**형식**

```bash
$ useradd 옵션 계정명
```

| 옵션 | 설명                                                         |
| :--: | ------------------------------------------------------------ |
|  -s  | 사용자의 로그인 기본 셸을 지정                               |
|  -d  | 계정의 홈 디렉터리를 지정                                    |
|  -f  | 패스워드가 만기된 후 계정이 영구히 말소될 때까지의 기간 지정 |
|  -e  | 사용자 계정의 유효기간을 설정<br />일정 시간 동안 사용 가능한 임시 계정을 만들고자 할 때 사용 |
|  -c  | 파일 /etc/passwd에 새로운 사용자 설명을 추가                 |
|  -G  | 계정이 속한 그룹 외에 다른 그룹 계정 추가                    |



#### passwd

생성된 계정자의 패스워드를 입력 및 변경하는 명령어이다.

생성된 계정자의 패스워드는 `"etc/shadow"` 파일 안에 기록된다.



**형식**

```bash
$ passwd 옵션 계정명
```

| 옵션 | 설명                                                         |
| :--: | ------------------------------------------------------------ |
|  -S  | 계정 상태 표시 (Status)<br />(PS : 정상, NP : 패스워드가 없음, LK : Lock 상태이거나 NP 상태) |
|  -d  | 계정 패스워드 삭제 (delete)                                  |
|  -l  | 계정을 lock 상태로 변경 (lock)                               |
|  -u  | 계정의 lock 상태를 해제 (unlock)                             |



**예제**

계정자 ulhangry의 상태를 확인한다. 확인후 패스워드가 지정되어 있지 않으면 패스워드를 지정한다.

```bash
$ passwd -S ulhangry
ulhangry LK 2022-01-24 0 99999 7 - 1

$ passwd ulhangry
password:
New Password:
```



#### su

`su`는 switch user, substitute user 의 줄임말이다.

현재의 사용자 계정에서 로그아웃하지 않고 다른 사용자 계정으로 로그인하여 해당 사용자의 권한을 획득하는 명령어이다.



**형식**

```bash
$ su 옵션 사용자 셸변수
```

|      옵션      | 설명                                       |
| :------------: | ------------------------------------------ |
| -, -l, --login | 지정한 사용자의 환경변수를 적용하여 로그인 |
|       -s       | 지정된 셸로 로그인                         |
|       -c       | 셸을 실행하지 않고 주어진 명령어 수행      |



**예제**

관리자 root로 계정을 변경한다.

```bash
$ su root
```



사용자 계정 변환 없이 root 권한으로 명령어 `"cat /etc/shadow"` 를 수행한다.

```bash
$ su -c 'cat /etc/shadow' - root
daemon:*:18674:0:99999:7:::
bin:*:18674:0:99999:7:::
sys:*:18674:0:99999:7:::
sync:*:18674:0:99999:7:::
games:*:18674:0:99999:7:::
man:*:18674:0:99999:7:::
lp:*:18674:0:99999:7:::
mail:*:18674:0:99999:7:::
news:*:18674:0:99999:7:::
uucp:*:18674:0:99999:7:::
proxy:*:18674:0:99999:7:::
.
.
.
```



#### usermod

디렉터리 `"/home"` 에 위치한 사용자들의 정보를 변경하는 명령어이다.

사용자의 홈 디렉터리 변경, 그룹 변경, 유효기간 등을 변경한다.



**형식**

```bash
$ usermod 옵션 계정명
```

|      옵션      | 설명                                                         |
| :------------: | ------------------------------------------------------------ |
|     -u did     | 새로운 uid를 지정<br />-o 옵션과 같이 사용하면 강제 설정이 가능 |
|       -g       | 새로운 gid를 지정<br />사용자 그룹을 지정 또는 변경          |
|       -G       | 새로운 보조그룹 지정<br />기존 그룹에 포함되어 있는 상태에서 새로운 그룹에 추가 지정 |
| -d 홈 디렉터리 | 새로운 홈 디렉터리를 지정                                    |
|     -s 셸      | 새로운 셸 지정                                               |
|    -c 주석     | 새로운 주석 지정                                             |
|     -I ID      | 로그인 ID를 바꾸는 옵션으로 새로운 계정명으로 변경           |



#### userdel

기존 계정 정보를 삭제하는 명령어이다.

옵션 없이 userdel을 사용하면 디렉터리 `"/etc/passwd"`, `"/etc/shadow"`, `"etc/group"`에서 해당 계정의 정보가 삭제된다.



**형식**

```bash
$ userdel 옵션 계정명
```

| 옵션 | 설명                                                         |
| :--: | ------------------------------------------------------------ |
|  -r  | 계정명의 /var/spool/mail의 메일 파일과 홈 디렉터리의 내용 모두를 삭제 |



#### chage

패스워드의 만료 정보를 변경하는 리눅스 명령어이다.



**형식**

```bash
$ chage 옵션 계정명
```

| 옵션 | 설명                                                         |
| :--: | ------------------------------------------------------------ |
|  -l  | 사용자 계정 정보를 출력                                      |
|  -m  | 설정 암호 최소 사용 일자                                     |
|  -M  | 설정 암호 사용 가능 일자                                     |
|  -E  | 암호 만기일 지정                                             |
|  -W  | 만기 전 변경 요구 경고 날짜 지정(지정된 날짜에 경고 메세지 출력) |



**예제**

|             예시             | 설명                                   |
| :--------------------------: | -------------------------------------- |
|      chage -l ulhangry       | 계정자 ulhangry의 패스워드 정보를 표시 |
|     chage -m 2 ulhangry      | 최소 패스워드 사용 일자는 2일          |
|     chage -M 30 ulhangry     | 최대 패스워드 사용 일자는 30일         |
| chage -E 2022/01/24 ulhangry | 2022년 1월 24일에 패스워드 만기        |
|     chage -W 10 ulhangry     | 만기 10일부터 경고 메세지 출력         |

#### 

#### groupadd

새로운 그룹을 생성하는 명령어이다.



**형식**

```bash
$ groupadd 옵션 그룹명
```

|  옵션  | 설명                                                         |
| :----: | ------------------------------------------------------------ |
| -g gid | 그룹에 gid를 지정                                            |
|   -r   | 시스템 그룹 생성 시 사용, 500번 이하 값 지정(남아있는 가장 높은 범위로 할당) |



#### groupdel

기존의 그룹을 삭제하는 명령어이다.

그룹 안에 소속되어 있는 계정명이 있을 경우 해당 그룹은 삭제되지 않는다.



**형식**

```bash
$ groupdel 그룹명
```



#### users

시스템에 로그인한 사용자 정보를 출력하는 명령어이다.



**형식**

```bash
$ users 옵션
```

|   옵션    | 설명                        |
| :-------: | --------------------------- |
| --version | users 명령어 버전 정보 출력 |



**예제**

현재 시스템에 로그인 사용자 정보를 출력한다.

```bash
$ users
ulhangry
```



#### who

현재 시스템에 접속해 있는 사용자들을 조회하는 명령어이다.

사용자 계정명, 터미널 정보, 접속 시간, 접속한 서버 정보 등을 확인할 수 있다.

관리자 root와 일반 사용자 모두 사용이 가능하다.

명령어 `"who am i"` 혹은 `"whoami"` 는 자신의 정보를 조회할 수 있다.



**형식**

```bash
who 옵션
```

| 옵션 | 설명                                    |
| :--: | --------------------------------------- |
|  -b  | 마지막 시스템 부팅 시간 출력            |
|  -q  | 로그인한 사용자와 사용자 수를 모두 출력 |
|  -r  | 현재 시스템의 실행 레벨을 확인 가능     |



**예제**

```bash
$ who
ubuntu   pts/0        2022-01-24 00:00 (:0)
$ who -r
         run-level 5  2021-11-11 23:44
$ who -b
         system boot  2021-11-11 23:44
```



#### w

현재 접속 중인 사용자들의 정보를 나타내는 명령어이다.

```bash
$ w
 00:00:00 up 74 days, 54 min,  1 user,  load average: 0.00, 0.00, 0.00
USER       TTY      FROM   LOGIN@   IDLE   JCPU   PCPU WHAT
ulhangry   pts/0    :0     00:35    1.00s  0.16s  0.00s w
```

확인 가능한 정보는 서버의 현재 시간 정보, 서버 부팅 후 시스템 작동 시간, 서버 접속자의 총 수, 

접속자별 서버 평균 부하율, 접속자별 서버 접속 계정명, TTY명, 로그인 시간 정보 등등 이다.



**JCPU**는 **TTY** 필드의 장치명에서 사용되는 모든 프로세스의 **CPU** 사용 시간이다.

**PCPU** 는 **WHAT** 필드에 나타나는 프로세스명에서 사용하는 **CPU** 총 사용 시간이다.



#### id

사용자 계정의 `uid`, `gid`, `group` 을 확인하는 명령어이다.



**형식**

``` bash
$ id 옵션 계정명
```

| 옵션 | 설명                                       |
| :--: | ------------------------------------------ |
|  -g  | 사용자의 GID만 표시                        |
|  -G  | 사용자가 포함되어 있는 모든 그룹 정보 표시 |
|  -u  | 사용자의 UID만 표시                        |



**예제**

```bash
$ id
uid=1001(ulhangry) gid=1001(ulhangry) groups=1001(ulhangry)
```



#### groups

사용자 계정이 속한 그룹 목록을 확인하는 명령어이다.



**형식**

```bash
$ groups 계정명
```



**예제**

현재 시스템에 로그인 사용자의 그룹명을 확인한다.

```bash
$ groups
ullest
```



끝