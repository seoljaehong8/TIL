### cmd 에서 접속

```shell
> ssh -i ssh -i .\aws_daum_administrator_pwd.pem ubuntu@54.209.132.174
```

### apahce 설치

```shell
$ sudo apt-get update
$ sudo atp-get install apahce2
$ sudo service apache2 (start,stop,restart)

# 켜져있는지 확인
$ ps aux | grep apache2
```

### demon 프로그램 확인

```shell
$ ls /etc/init.d

$ sudo service --status-all | grep +
```

> etc/init.d 는 디렉토리는 daemon 프로그램들이 있는 디렉토리
>
> 실행되고 있는 프로그램들



### firewalld

```shell
$ sudo apt install firewalld -y

# 버전확인
$ sudo firewall-cmd --version

# 새로운 rule 적용
$ sudo firewall-cmd --permanent --zone=public --add-port=80/tcp
$ sudo firewall-cmd --reload

# 모든 값 조회
$ sudo firewall-cmd --list-all
```



### apt, apt-get 차이

> apt는 apt-get과 apt-cache의 기능 중에서 잘 사용되지 않는 기능을 제외하고 만든 새로운 tool이다.
> 여기서 apt-get은 패키지 설치를 담당하고, apt-cache는 패키지 검색을 담당하는 tool이다.
> 결론적으로 apt-get이 아닌 apt를 사용하는 것이 사용성 측면에서는 유리하다.



### python(apach2,django 연결)

> ubuntu에는 python3.8.5가 설치 되어있다
>
> - 가상환경 설치 및 장고 설치
>
> > ```shell
> > $ sudo apt-get install python3-venv -y
> > $ mkdir /home/ubuntu/tutorial/django
> > 
> > $ python3 -m venv venv
> > $ source venv/bin/activate
> > 
> > (venv) $ pip install --upgrade pip
> > (venv) $ pip install django
> > 
> > (venv) $ cd /home/ubuntu/tutorial/django
> > (venv) $ django-admin startproject tutorial
> > ```
> >
> > - settings.py 수정
> >
> > ```python
> > ALLOWED_HOSTS = ['*'] # 모든 아이피에서 접속허용
> > # 나중에는 현재 우분투 서버의 IP를 넣을것이다.
> > ```
> >
> > - apach2 설정 파일 수정
> >
> > ```shell
> > (venv) $ sudo apt install libapache2-mod-wsgi-py3
> > (venv) $ sudo vi /etc/apache2/sites-available/000-default.conf
> > 
> > # 수정
> > <VirtualHost *:80>
> >         
> >         ServerAdmin webmaster@localhost
> >         DocumentRoot /var/www/html
> > 
> >         
> >         ErrorLog /home/ubuntu/tutorial/site/logs/error.log
> >         CustomLog /home/ubuntu/tutorial/site/logs/access.log combined
> > 
> >         <Directory /home/ubuntu/tutorial/django/tutorial/tutorial/>
> >                 <Files wsgi.py>
> >                         Require all granted
> >                 </Files>
> >         </Directory>
> > 
> > 
> >         WSGIDaemonProcess tutorial python-path=/home/ubuntu/tutorial/django/tutorial python-home=/home/ubuntu/tutorial/venv
> >         
> >         WSGIProcessGroup tutorial
> >         WSGIScriptAlias / /home/ubuntu/tutorial/django/tutorial/tutorial/wsgi.py
> >         
> > </VirtualHost>
> > ```
> >
> > ```shell
> > <VirtualHost *:80>
> >         
> >         ServerAdmin webmaster@localhost
> >         DocumentRoot /var/www/html
> > 
> >         
> >         ErrorLog /home/ubuntu/tutorial/site/logs/error.log
> >         CustomLog /home/ubuntu/tutorial/site/logs/access.log combined
> > 
> >         <Directory /home/ubuntu/app/django/firstproject/pjt06/>
> >                 <Files wsgi.py>
> >                         Require all granted
> >                 </Files>
> >         </Directory>
> > 
> > 
> >         WSGIDaemonProcess firstproject python-path=/home/ubuntu/app/django/firstproject python-home=/home/ubuntu/app/django/firstproject/venv
> >         
> >         WSGIProcessGroup firstproject
> >         WSGIScriptAlias / /home/ubuntu/app/django/firstproject/pjt06/wsgi.py
> >         
> > </VirtualHost>
> > ```
> >
> > 

https://blog.naver.com/PostView.nhn?blogId=semtul79&logNo=221485859880&categoryNo=11&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=section



디비설정

https://yuddomack.tistory.com/entry/%EC%B2%98%EC%9D%8C%EB%B6%80%ED%84%B0-%EC%8B%9C%EC%9E%91%ED%95%98%EB%8A%94-EC2-nginx%EC%99%80-uwsgi%EB%A1%9C-django-%EC%84%9C%EB%B9%84%EC%8A%A4%ED%95%98%EA%B8%B0?category=777812