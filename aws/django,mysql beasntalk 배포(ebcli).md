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
```

```bash
vi .ebextensions/00_eb_setting.config

option_settings:
    aws:autoscaling:asg:
        MinSize: '2'
        MaxSize: '4'
        Cooldown: 600
    aws:ec2:instances:
        EnableSpot: false
        InstanceTypes: "t2.micro, t3.micro"        
    aws:autoscaling:launchconfiguration:
        EC2KeyName: nds-key-pair
        SecurityGroups: sg-030290b5ee039b722
        RootVolumeType: gp3
        RootVolumeSize: 8
        RootVolumeIOPS: 3000
    aws:autoscaling:trigger:
        MeasureName: CPUUtilization
        Unit: Percent
        LowerThreshold: 20
        UpperThreshold: 60
        LowerBreachScaleIncrement: -1
        UpperBreachScaleIncrement: 1
    aws:elbv2:loadbalancer:
        SecurityGroups: sg-030290b5ee039b722
    aws:ec2:vpc:
        VPCId: "vpc-0a878c5dc4b348897"
        Subnets: "subnet-0c31aacfbfdb624ce,subnet-0af4fb2f4d70012cc"
        ELBSubnets: "subnet-07613168517418534,subnet-01c6eb906cfbfcc03"
        #AssociatePublicIpAddress: true
    aws:elasticbeanstalk:command:
        DeploymentPolicy: Rolling
```

```bash
vi .ebextensions/01_healthcheckurl.config

option_settings:
  aws:elasticbeanstalk:environment:process:default:
    DeregistrationDelay: '20'
    HealthCheckInterval: '15'
    HealthCheckPath: /ok/
    HealthCheckTimeout: '5'
    HealthyThresholdCount: '3'
    UnhealthyThresholdCount: '5'
    Port: '80'
    Protocol: HTTP
```

```bash
vi .ebextensions/02_django.config

option_settings:
  aws:elasticbeanstalk:application:environment:
    DJANGO_SETTINGS_MODULE: mypjt.settings
  aws:elasticbeanstalk:container:python:
    WSGIPath: mypjt.wsgi:application
```

```bash
vi .ebextensions/03_packages.config

packages:
  yum:
    python3-devel: ''
    gcc: ''
    mariadb-devel: ''
```

```bash
vi .ebextensions/04_migrate.config

container_commands:
  00_test_output:
    command: "echo 'migrate.....'"
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

