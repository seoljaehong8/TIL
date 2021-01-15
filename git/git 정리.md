```bash 
$ git init
$ git config --global user.email seoljaehong8@gmail.com
$ git config --global user.name jay
$ git config --global --list
$ git status
$ git add .
$ git commit -m 'first commit'
$ git status
```

> git 홈페이지에서 create repository
>
> 일단 이름만 설정



```bash
$ git remote add origin https://github.com/seoljaehong8/testgit.git
```

> local에서 github의 주소를 알게된다. (등록)
>
> local의 commit 내용을 github로 올려준다.



``` bash
$ git push -u origin master
```

> github 홈페이지에서 로그인



```bash
$ git checkout .
```

> 파일을 지웠더라도 깃에서 받아올 수 있다.



``` bash
$ git clone https://github.com/seoljaehong8/testgit.git
```

> testgit repasitory 를 복사해 올 수 있다.



# Git 

### Git 개념 

git은 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율하기 위한 분산 버전 관 리 시스템이다.

### Git 설정 

- 전역 영역에서 commit 기록의 주인을 등록 

  ``` bash 
  $ git config --global user.name "username"
  $ git config --global user.email "edu@hphk.kr"
  ```

  

### Git 기본 

- `git init`  해당 디렉토리를 Git이 관리하도록 초기화 

- `git add`파일명 커밋할 목록에 추가 

- `commit -m "커밋 메시지"` (히스토리의 한 단위) 만들기 

- `git push origin master` 현재까지의 역사(commits)가 기록되어 있는 곳에 새로 생성한 커밋 반영 

- `git pull origin master` remote와 로컬 git의 버전을 맞추는 명령어(강의장과 집을 왕복하면서 두개의 컴퓨터로 작업할 때 필수인 명령어)

  - git work flow
    1. git pull origin master
    2. git add .
    3. git commit -m 'message'
    4. git push origni master

  

### Git 저장소 

로컬(working directory) - staging area - remote repository(github, bitbucket, gitlab) 로컬 컴퓨터 저장소 해당 버전의 스냅샷(기록). 원격 저장소 

### Git branch

같은 작업물을 기반으로 동시에 다양한 작업을 할 수 있게 만들어 주는 기능 독립적인 작업 영역 안에서 마음대로 소스코드를 변경할 수 있다. 분리된 작업 영역에서 변경

된 내용은 추후에 기존 버 전과 비교해서 새로운 하나의 버전을 만들어 낼 수 있다.



### 리모트 확인하는 명령어

`git remove -v`



### git init은 상위 폴더 에서!!

- 상위폴더에 `.git` 폴더가 있는 경우는 하위 폴더에서 git init을 하지 않는다.

---



