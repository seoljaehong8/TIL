```bash
sudo -s
apt-get update
apt install python3-pip -y
pip install awsebcli --upgrade --user
export PATH="/root/.local/bin:$PATH"
source ~/.bashrc
eb --version
apt install python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip install django==2.2
django-admin startproject ebdjango
cd ebdjango
python3 -m manage migrate
pip freeze > requirements.txt
deactivate
mkdir .ebextensions
vi .ebextensions/00django.config

option_settings:
  aws:elasticbeanstalk:application:environment:
    DJANGO_SETTINGS_MODULE: mypjt.settings
  aws:elasticbeanstalk:container:python:
    WSGIPath: mypjt.wsgi:application

    
    
vi .ebextensions/01packages.config

packages:
  yum:
    python3-devel: ''
    gcc: ''
    mariadb-devel: ''
    
    
vi .ebextensions/02db-migrate.config
container_commands:
  01_migrate:
    command: "django-admin.py migrate"
    leader_only: true
option_settings:
  aws:elasticbeanstalk:application:environment:
    DJANGO_SETTINGS_MODULE: mypjt.settings
    
인스턴스에 역할 부여


### 스냅샷
eb init -p python-3.8 django-tutorial
eb init

eb create django-env
eb status

settings.py -> ALLOWED_HOSTS에 추가
django-env.eba-yg7qxzix.us-west-2.elasticbeanstalk.com
django-env.eba-6ictkmne.ap-northeast-1.elasticbeanstalk.com


eb deploy
eb open

eb terminate django-env





https://velog.io/@_gyullbb/Elastic-Beanstalk-%EB%B0%B0%ED%8F%AC#%EB%B0%B0%ED%8F%AC-%EB%B0%A9%EB%B2%95-2-elastic-beanstalk
```

