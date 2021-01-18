# Git
## Git 개념

>  git은 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율하기 위한 분산 버전 관리 시스템이다.

## Git 설정

* 전역 영역에서 commit 기록의 주인을 등록

  ```bash
  $ git config --global user.name "username"
  $ git config --global user.email "edu@hphk.kr"
  $ git config --global --list
  user.email=mulcamp.ed@gmail.com
  user.name=ed
  ```

## Git 기본

### 1. git init

* `git init` 해당 디렉토리를 Git이 관리하도록 초기화

  * `.git`폴더가 생성되며, 여기에 git과 관련된 모든 정보가 저장된다.

    * `.git` 폴더가 위치한 폴더 부터 하위 폴더까지 관리하게 된다. 

  * git bash에 `(master)` 라고 표시가 된다.

  * ## git init 할땐 `(master)` 가 없는 곳에서...

    * 상위 폴더에 `.git` 폴더가 있는 경우는 하위 폴더에서 따로 `git init` 을 하지 않는다.
    * 하위 폴더의 코드를 따로 관리하고 싶을때 사용한다.

### 2. git add

* `git add 파일명` 

  * `working directory (작업공간)`변경된 사항을 이력으로 저장하기 위해 반드시 `staging area`에 올려야 한다.

    ```bash
    $ git add git_정리.md # 특정 파일
    $ git add python/ # 특정 폴더
    $ git add . # 현재 디렉토리의 모든 파일
    ```

    - `add` 전 상태

      ```
      $ git status
      On branch master
      
      No commits yet
      
      Untracked files: # git 이력에 담기지 않은 파일들
        (use "git add <file>..." to include in what will be committed)
        # git add 명령어를 통해서 커밋될 곳에 추가 해라.
              a.txt
              b.txt
      
      nothing added to commit but untracked files present (use "git add" to track)
      ```

    - `add` 후 상태

      ```
      $ git status
      On branch master
      
      No commits yet
      
      Changes to be committed: # 커밋될 변경 사항
        (use "git rm --cached <file>..." to unstage)
              new file:   a.txt # a.txt 새로운 파일 생성
      
      Untracked files: # 트래킹 되고 있지 않은 파일들
        (use "git add <file>..." to include in what will be committ
              b.txt
      ```

    **항상 `git status` 명령어를 통해 현재 상태를 확인 하는 것이 중요하다!!!!**

### 3. git commit

* `git commit -m "커밋 메시지"` 

  * 버전의 이력을 확정짓는 명령어, 해당 시점을 스냅샷으로 만들어서 기록을 한다.
    * 변경된 내용을 기록하여 저장하게됨.
  * 커밋시에는 **반드시 commit 메세지를 작성**해야하며, commit 메세지는 변경사항을 알 수 있도록 명확하게 작성해주면 된다.
    * 메시지는 주로 해당 이력에 대한 정보를 담는다.

  ```bash
  $ git commit -m '파일 추가'
  [master (root-commit) 31f694c] Add files
   2 files changed, 0 insertions(+), 0 deletions(-)
   create mode 100644 a.txt
   create mode 100644 b.txt
  ```

  * 커밋 이력을 확인하기 위해서는 아래의 명령어를 활용한다.

  ```bash
  $ git log
  commit 31f694c245f18a6388574bf83206ee9873cb1603 (HEAD -> master)
  Author: ed <mulcamp.ed@gmail.com>
  Date:   Mon Dec 9 14:25:09 2019 +0900
  
      Add files
  $ git status
  On branch master
  nothing to commit, working tree clean
  ```

  * 이후 변경 사항이 발생하게 된다면, `add` -> `commit` 을 한다.

### 4. git remote 설정

*  원격 저장소 설정

```
$ git remote add origin https://~
```

* 원격 저장소(`remote`)를 `origin` 이라는 이름으로 `https://~`로 설정한다.

* 아래의 명령어를 통해서 저장된 원격 저장소 목록을 확인할 수 있다.

```
$ git remote -v
origin  https://github.com/edutak/gittest.git (fetch)
origin  https://github.com/edutak/gittest.git (push)
```

* 혹시 잘못 설정되었다면 아래의 명령어를 통해 삭제 가능하다.

```
$ git remote rm origin
$ git remote -v
```

### 5. git push

* `git push origin master` 

  * 원격 저장소에 업로드 하기 위해서는 `push` 명령어가 필요하다.

  ```
  $ git push origin master
  Enumerating objects: 3, done.
  Counting objects: 100% (3/3), done.
  Delta compression using up to 8 threads
  Compressing objects: 100% (2/2), done.
  Writing objects: 100% (3/3), 210 bytes | 210.00 KiB/s, done.
  Total 3 (delta 0), reused 0 (delta 0)
  To https://github.com/edutak/gittest.git
   * [new branch]      master -> master
  ```

  * `origin` 으로 설정된 원격 저장소에 `push` 한다.

### 6. git pull

* `git pull origin master` 
* 원격 저장소의 버전 내용을 로컬로 가져오는 명령어
* 로컬 컴퓨터의 내역을 원격 저장소의 내용으로 업데이트 할 수 있다.



## 7. git clone

- ``` bash
  $ git clone https://github.com/seoljaehong8/testgit.git
  ```

- github에서 repasitory를 복사해올 수 있다.



## 8. git rm

- ```bash
  $ git rm test.txt
  ```

- 로컬과 원격에서 파일 삭제

  

---

* 오프라인 수업이 진행되었을 때 git work flow
  1. `git pull origin master`
  2. `git add .`
  3. `git commit -m 'message'`
  4. `git push origin master`

---

## 



## Git 저장소

| 로컬(working directory) | staging area                     | local commit                                | remote repository(github, bitbucket, gitlab) |
| ----------------------- | -------------------------------- | ------------------------------------------- | -------------------------------------------- |
| 실제 작업하는 공간      | 커밋되기 전 임시로 확인하는 공간 | 로컬 컴퓨터 저장소 해당 버전의 스냅샷(기록) | 원격 저장소                                  |



### 1 Repository == 1 Project

* 하나의 Repository엔 하나의 프로젝트!!
  * 하나의 Repository 에 두 개이상의 프로젝트가 있으면 (나중에 후회한다)