- IP 수동 설정

```bash
# vi /etc/sysconfig/network-scripts/ifcfg-ens33
```

```bash
DEVICE="ens33"
BOOTPROTO="static"
IPADDR="192.168.132.10"
NETMASK="255.255.255.0"
GATEWAY="192.168.132.254"
ONBOOT="yes"
DNS1="168.126.63.1"
DNS2="8.8.8.8"
```

```bash
# systemctl restart network
```

- root 비밀번호가 생각안나거나 할때 싱글유저부트 설정(Runlevel 1)
  - 재부팅 => ctrl+alt+insert
    single boot process

    1. power on 
    2. 부팅로드 5초안에
       화면 마우스 좌클릭 후 e(아무버튼상관 없음)
    3. 커널선택 => e
    4. kernel이동 후(제일 긴거선택하시고) => e
    5. queit => single 변경 후 엔터
    6. b(boot)
    7. passwd 비번 설정
    8. reboot 재부팅



- 주요 디렉토리 설명

  1. /		= 최상위 dir = Window s c:\ 와 같은 의미	

  2. /boot		= 부팅file들의 저장소 (grub의 부트로더) = windows boot.ini	
     	          	= 리눅스 커널의 메모리 이미지와 부팅 과정에서 필요한 정보 파일들이 있다.

  3. /bin		= binary(2진수) = 실행 file 들 	
     	       	= 기본적인 명령어

  4. /sbin		= 시스템 명령어 = windows system32 폴더하고 같다.
     	 	        = 시스템 운영 및 관리 부팅과정에 필요한 것

  5. /root		= 슈퍼 유저 root 의 홈 디렉토리 = windows 의 administrator 의 H.D	

  6. /home		= 관리자 이외의 사용자의 홈 디렉토리가 생성되는 위치			
     		            = 홈 디렉토리의 집합소					

  7. /etc	 	= 서버 관리 및 시스템 관리 = 설정 파일 저장소

  8. /dev		= device 줄임말(장치) = 장치파일 저장소 					

  9. /lib		= 언어 관련 파일 저장소 = 파일에 대한 해석역할을 한다.
     		      = .dll = dinamic Link Library

  10. /mnt		= 파일 시스템을 임시로 마운팅 하는 디렉토리

  11. /media 	= local device 를 이용하기 위한 디렉토리 [ex) CD-ROM]

  12. /usr		= Unix System Resource
      		       = 용량이 크고 자주 사용되지 않는 파일 저장	

      ​               = 기본 실행 파일과 라이브러리 파일,헤더파일등 많은 파일이 있다

  13. proc 	= 커널(운영체제)과 프로세스 정보가 저장되는 디렉토리

  14. /tmp		= 시스템 사용 중에 발생하는 임시 데이터가 저장,재부팅시 모두 삭제

  15. /var		= /var/log 나 /var/adm 과 같이 자주 변경되는 시스템 파일들을 가지고 있다

  16. /opt		= 추가 패키지가 설치되는 디렉토리

  17. /sys		= 리눅스 커널과 관련된 파일이 있는 디렉토리

  18. /lost+found	= 파일 시스템에 문제가 발생하여 복구할 경우,문제가 되는 파일이 저장되는 디렉토리로 보통은 비어있다

  19. /srv		= FTP 나 Web 등 시스템에서 제공하는 서비스의 테이터가 저장된다













# 명령어

- netstat -lntup

  - 내 컴퓨터에 열린 모든 포트 보기

    - -a : 연결된 모든 소켓을 출력한다.

      -n : 기호화된 호스트나 포트이름, 유저이름 대신 숫자로 표시한다.

      -p : 소켓에 대한 PID/프로그램을 출력한다.

      -r : 라우팅 테이블을 출력한다.

      -s : SNMP와 같은 네트워크 통계를 출력한다.

      -e : 랜카드에서 송수신한 패킷의 용량 및 종류 확인 -s와 같이 사용한다.

      -c : 계속되는 리스트를 출력한다.

      -t : tcp를 이용하여 접속한 리스트를 출력한다.

      -u : udp를 이용하여 접속한 리스트를 출력한다.

    - ```bash
      # netstat    -r
      
      # netstat   –t
      
      # netstat   –ant  |  grep  LISTEN
      ```

- firewall-cmd

  - 방화벽

    - ```bash
      # firewall-cmd --permanent --add-port=80/tcp	: 80번 포트 추가
      # firewall-cmd --permanent --add-service=http	: http 서비스 추가
      # firewall-cmd --permanent --remove-port=80/tcp : 80번 포트 삭제
      # firewall-cmd --reload
      # firewall-cmd --list-all						: list 전부 보기
      # systemctl enable httpd (부팅시 httpd 시작)
      
      ```

- head / tail

  - 문서 파일 내용을 블럭 단위로 출력(위에서,아래에서)

  - 출력 단위는 10줄씩 출력

    - ```bash
       # head /etc/passwd	: 위에서 10줄 출력
       # tail /etc/passwd	: 아래에서 10줄 출력
       # head -5 /etc/passwd	: 위에서 5줄 출력
       # tail -5 /etc/passwd	: 아래에서 5줄 출력
      ```

- find / which

  - 시스템에서의 파일 또는 디렉터리명을 검색

    - ```bash
      # find / -name samadal		: 최상위 디렉터리 하위에 있는 'samadal'이란 이름을 가진 파일 또는 디렉터리 검색
      # find / -name test -o -name test1 -o -name test2 // 다량 이름으로 한꺼번에 찾기
      # find / -name samadal -type f	: 파일 검색
      # find / -name samadal -type d	: 디렉터리 검색
      # which [실행파일] 		: 실행파일 검색
      ```

- 리눅스 종료 	

  - shutdown -h now = halt = poweroff = init 0

- 리눅스 재부팅 	

  - shutdown -r now = reboot =init 6

- 복사

  - ```bash
    # cp		: 파일 복사
    # cp -r	: 하위 디렉토리까지 복사
    ```

- 부팅모드

  - ```bash
    /etc/inittab (System RunLevel)
    
    # Default runlevel. The runlevels used are:
    #   0 - halt (Do NOT set initdefault to this) 	종료
    #   1 - Single user mode			싱글모드(안전모드) single boot
    #   2 - Multiuser, without NFS 			텍스트모드 NFS미지원 (TUI)
    #   3 - Full multiuser mode			텍스트모드 NFS지원 (TUI)
    #   4 - unused					사용안함 (사용자지정모드)
    #						사용별로 권한을 준게 X = 그냥 막아논것		
    #   5 - X11					그래픽모드 (GUI)
    #   6 - reboot (Do NOT set initdefault to this)	재시작
    #
    id:5:initdefault:				기본값
    ```

  - 





# VI

> ** VI/VIM Editor 사용 방법
>
> VI = notepad= 편집기
> VIM = wordpad = 편집기의 확장팩
>
> ---
>
> 명령 모드 = 초기 모드 = 이동 모드
> 입력 모드 = 편집 모드 = 8가지
> EX 모드   = 실행 모드
> =========================3가지의 모드전환시 항상 ESC 를 누른다
>
> ---
>
> - **명령 모드 = 초기 모드**
>   - h : 커서를 왼쪽으로 이동
>   - j : 커서를 아래로 이동
>   - K : 커서를 위로 이동
>   - l : 커서를 오른쪽으로 이동
>
> ---
>
> - **단어 단위로 이동**
>   - W,w : 다음 단어의 처음으로 이동 West 라고 외우면 편함
>   - E,e : 단어의 끝으로 이동        East 라고 외우면 편함
>   - B,b : 단어의 처음으로 이동      back West 라고 외우면 편함
>
> ---
>
> - **행단위 로 이동**
>   - 0 (숫자)		행의 처음으로 이동
>   - $		           행의 마지막으로 이동
>
> ---
>
> - **문서 단위**
>   - G(shift + g)	문서의 마지막으로 이동
>   - gg		      : 문서의 처음으로 이동
>   - Ctrl + f	  : 페이지 앞으로 이동
>   - Ctrl + b	 : 페이지 뒤로 이동
>   - shift + h	: high   화면 처음
>   - shift + m   : middle 화면 중간
>   - shift + l	  : low    화면 끝
>
> --------------------------------------------------------
> - **복사 / 삭제**
>   - x(소)	커서가 있는 문자 삭제 = delete
>   - X	커서가 있는 앞 문자 삭제 = back space
>   - dd	현재 커서의 행 삭제 = 한줄씩 삭제
>   - 3 dd	현재행 포함 아래의 3줄 삭제
>   - yy	현재 커서가 있는 라인을 복사
>   - 3 yy	현재 커서부터 숫자만큼의 행을 복사
>   - p(소)	복사한 내용을 현재 라인 이후에 붙여넣기 (paste)
>   - P	복사한 내용을 현재 라인 이전에 붙여넣기 (paste)
>
> ---
>
> - **dd 와 yy 의 활용**
>   - 이동 명령과 조합가능
>     단어 삭제 			단어 복사
>     dw 				            yw
>     de				              ye
>     db			              	yb
>     d0		              		y0
>     d$			              	y$
>     dG			                 yG
>
> ​              dgg		            		ygg
>
> ---
>
> - Ctrl + v  = visual block  = 블락표시
>   ============================================================= 명령모드 끝
>
> ---
>
> - **입력 모드 = 편집 모드**
> - i(소)	: 현재 위치에서 입력 모드로 전환 =현재 프롬프트를 우측 밀어내고 입력
> - I	       :행의 제일 처음에서 입력 모드로 전환 0+i
> - a(소)	: 현재 위치에서 우측으로 한 칸 이동 후 입력 모드로 변경
>   	         =현재 프롬프트를 좌측 밀어내고 입력
> - A	      : 행의 제일 마지막에서 입력모드로 변경 
> - o(소)	: 커서 아래에 새로운 행을 추가하고 입력모드로 변경
> - O(대)	: 커서 위에 새로운 행을 추가하고 입력모드로 변경
> - s(소)	: 현재 문자를 지우고 입력모드로 변경
> - S	      : 현재 행의 모든 문자를 지우고 입력모드로 변경
>   =============================================================== 입력모드 끝
>
> ---
>
> - **EX 모드   = 실행 모드**
>   - 검색 = Ctrl + f
>   - /Pattern 	Pattern 을 아래쪽으로 검색
>     -  패턴이 검색된 후 n 키를 통해 아래 방향으로 계속 찾기(정방향)
>        패턴이 검색된 후 N 키를 통해 위 방향으로 계속 찾기(역방향)
>   - ?Pattern	Pattern 을 위쪽으로 검색
>     -  패턴이 검색된 후 n 키를 통해 위 방향으로 계속 찾기(정방향)
>     - 패턴이 검색된 후 N 키를 통해 아래 방향으로 계속 찾기(역방향) 
>
> ---
>
> - **치환**
>
>   - ctrl + h
>
>     - [범위]s/[Old]/[New]/[옵션] 	: Old  를 New 로 치환
>       -  범위는 n 혹은 n,n 혹은 %를 넣을 수 있다
>       -  g 옵션을 주면 적용되는 라인의 모든 부분 변경
>       -  g 옵션을 주지 않으면 처음 찾은 부분만 변경
>
>   - ex)
>     :s/th/1234
>     :s/th/1234/g
>     :10s/i/777/g
>       └ 10번째 줄에서 i를 777로 = 지정한 행 모두 
>     :10,12,15s/i/777 => 지정범위행당 최초 1개씩만 치환
>     :10,12s/i/777/g => 지정범위행당 모두 치환
>
>     :%s/th/1234/g  => 문서 모두 th 를 1234 로 치환
>
> ---
>
> - :set nu 번호표 활성
> - :set nonu 번호표 비활성
>
> ---
>
> - :!	vi를 잠시 중단하고 명령어 수행
> - :.!	수행한 명령의 결과를 현재 커서가 위치한 행의 전체 문자열을 삭제하고 vi 편집기로 출력한다
>
> ---
>
> - **Split Window**
>
>   - :[n]split [파일이름] 	수평 나누기 vi/vim
>
>   - :[n]vs [파일이름]		수직 나누기 vim 전용
>
>   - [n] 창 번호 
>
>   - 명령모드에서 Ctrl + wn 은 현재 화면을 수평으로 나누기 = 새 창 추가에 의미
>
>   - 명령모드에서 Ctrl + wv 는 현재 화면을 수직으로 나누기
>
>   - 명령모드에서 Ctrl + ww 는 창간 이동
>
>   - ex)
>     :split /backup/inittab
>
>     :3sp /backup/grub.conf
>
> ---
>
> - **파일관련 명령**
>   - :q 	저장안하고 나가기
>   - :w	저장하기
>   - :wq	저장하고 나가기
>   - :q!	강제 나가기
>   - :e	현재 창을 닫고 파일 열기/파일 생성 / 꼭 :e [생성경로] 를 적어준다
>   - :enew	현재 창을 닫고 빈 새 문서를 연다
>   - :f	커서위치 찾기/현재 파일 위치=pwd
>
> ---
>
> - **파일 생성 명령어 모음 **
>   - touch 	파일 크기 0인 빈 문서를 생성
>   - cat >	내용을 간단히 순차적 삽입하면서 생성 
>   - cat >>  내용을 추가
>   - vi 	파일 마음대로 편집/생성/추가/삭제
>     - dos 창에서 vi /test/a 입력 
>       	a. 파일 존재시 vi 보기
>       	b. 파일 미존재시 새 파일 생성
>     - vi 를 연 상태에서 :sp wn입력으로 새 문서 만들기
>     - vi 를 연 상태에서 :e /test/a 라는 경로로 새문서 만들기
>
> ---
>
> - :w >> [목적파일이름]  현재편집중인 파일을 지정된 파일 제일 밑으로 추가
>
> - :w [파일이름]   : 다른이름으로 저장
>
> - :[n]r[파일이름]	   파일이름의 내용을 현재 편집중인 파일의 n라인부터 삽입			
>
> - 한 파일만 실행 / 여러파일 안됨
>
> - :[n]r![command]	   Command 실행결과를 파일의  n라인부터 삽입
>
> - :.! [command]	Command 실행결과를 파일의 프롬프트가 위치하는곳에서부터 삽입
>
> - vi +숫자 [경로] 	지정한 숫자행으로 커서가 이동되면서 파일오픈
>
> - vi + [경로]	문서가장 아래 커서가 이동되면서 파일오픈
>
>   

