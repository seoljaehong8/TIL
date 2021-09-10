# https 적용

```bash
$ sudo apt-get update
$ sudo apt-get install letsencrypt
```

- nginx 중지

```bash
$ sudo docker stop <front container name>
```

- 인증서 발급

```bash
$ sudo letsencrypt certonly --standalone -d [도메인 네임]
ex ) sudo letsencrypt certonly --standalone -d i4d101.p.ssafy.io
```

> 정상적으로 발급 시 /etc/letsencrypt/live/[도메인 네임] 아래에 키 값을 얻을 수 있다.

- SSL 옮기기

```bash
$ sudo cp /etc/letsencrypt/live/<도메인 네임>/fullchain.pem <볼륨 매핑에 사용될 폴더>
$ sudo cp /etc/letsencrypt/live/<도메인 네임>/privkey.pem <볼륨 매핑에 사용될 폴더>
```

- Nginx 설정 파일 수정

```bash
server {
	listen 80;
	server_name i5d205.p.ssafy.io;

    return 301 https://$server_name$request_uri;


}

server {

        listen 443;
        listen [::]:443;
        ssl on;
        server_name i5d205.p.ssafy.io;

        ssl_certificate /home/node/app/ssh/fullchain.pem;
        ssl_certificate_key /home/node/app/ssh/privkey.pem;


        location / {
                alias /usr/share/nginx/html/homepage/;
                try_files $uri $uri/ /index.html;
        }

		location /api {
			proxy_pass http://i5d205.p.ssafy.io:8080;

			proxy_http_version 1.1;
			proxy_set_header Connection "";
			// 소켓통신 사용시 아래 두줄 추가
			// proxy_set_header Upgrade $http_upgrade;
		    // proxy_set_header Connection "upgrade";
			proxy_set_header Host $host;
			proxy_set_header X-Real-IP $remote_addr;
			proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
			proxy_set_header X-Forwarded-Proto $scheme;
			proxy_set_header X-Forwarded-Host $host;
			proxy_set_header X-Forwarded-Port $server_port;
		}

}

```

- .env.local 수정

```bash
VUE_APP_SERVER_URL=https://i5d205.p.ssafy.io/api
```

- Jenkinsfile 수정

```bash
sh 'docker run -d -v /home/ubuntu/ssh:/home/node/app/ssh -p 80:80 -p 443:443 --name frontend frontend'
```

