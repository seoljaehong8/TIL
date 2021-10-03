# django,mysql beasntalk 배포(ebcli)



### linux 작업

```bash
sudo yum update -y
python3 -m pip install --upgrade pip
python3 -m pip install awsebcli
eb --version
sudo yum install git -y
git clone https://github.com/seoljaehong8/todo.git
cd todo/server/
mkdir .ebextensions
vi .ebextensions/django.config
```

```bash
option_settings:
  aws:elasticbeanstalk:application:environment:
    DJANGO_SETTINGS_MODULE: mypjt.settings
  aws:elasticbeanstalk:container:python:
    WSGIPath: mypjt.wsgi:application
    NumProcesses: 3
    NumThreads: 20
packages:
  yum:
    python3-devel: ''
    gcc: ''
    mariadb-devel: ''
container_commands:
  00_test_output:
    command: "echo 'testing.....'"
  01_migrate:
    command: "source /var/app/venv/staging-LQM1lest/bin/activate && python3 manage.py migrate --noinput"
    leader_only: true
```

인스턴스에 빈스토크 롤 부여

각각의 폴더의 마이그레이션 파일들을 지워주고 다시 makemigrations 명령어를 통해 실행해줘야 한다.

```bash
# 다시 마이그레이션 할 경우
sudo yum install gcc python3-devel mysql-devel -y
cd ~
python3 -m venv venv
source venv/bin/activate
cd todo/server/
pip install -r requirements.txt
python3 manage.py makemigrations
deactivate
```



- beanstalk 생성

````bash
eb init
'''
지역 선택 : 9) ap-northeast-1 : Asia Pacific (Tokyo)
application name 설정
플랫폼 설정 : 2) Python 3.7 running on 64bit Amazon Linux 2
SSH, keypair 설정
'''

# .elasticbeanstalk 폴더 생성

eb create
'''
환경 이름 설정
DNS CNAME 설정
로드밸런서 타입 설정
스팟 인스턴스 설정
```

eb deploy

# 삭제
eb terminate django-env(환경 이름)


````

