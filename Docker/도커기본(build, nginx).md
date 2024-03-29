# vue - docker



### 이미지 생성

- vue-test 폴더안에 DockerFile 생성 (nginx 배포)

``` 녀애 bash
# build stage
FROM node:lts as build-stage

# 이미지 내에서 명령어를 실행할 디렉토리 설정
WORKDIR /home/node/app

COPY package*.json ./

# bable-plugin error 생길시
# npm install @vue/babel-preset-app --save-dev

RUN npm install --production

RUN npm install -g @vue/cli-service

COPY . .

RUN npm run build


# production stage
FROM nginx:stable-alpine as production-stage

RUN rm /etc/nginx/conf.d/default.conf

COPY ./nginx/homepage.conf /etc/nginx/conf.d/homepage.conf

COPY --from=build-stage home/node/app/dist /usr/share/nginx/html

EXPOSE 80

# 컨테이너 실행시 실행할 명령어
CMD ["nginx", "-g", "daemon off;"]

```

- nginx/hompage.conf

```bash
server {
	listen 80;

	location / {
		alias /usr/share/nginx/html/homepage/;
		try_files $uri $uri/ /index.html;
	}
}
```



```bash
$ sudo docker build -t vue-test .
$ sudo docker images
$ sudo docker ps -a
```



### 컨테이너 실행

```bash
# 생성만 하기
$sudo docker create --name vue-test-1 -p 8080:8080 vue-test
```

```bash
# 생성과 동시에 실행하고 진입하기
# 현재폴더를 컨테이너상의 /home/node/app 폴더와 연동하겠다
$ sudo docker run --name vue-test-1 -v $(pwd):/home/node/app -p 8080:8080 vue-test
```

```bash
$ sudo docker run --name vue-test-1 -p 8080:8080 vue-test
```

```bash
# 컨테이너 실행하기
$ sudo docker start vue-test-1
```



- 코치님 자료
  - https://glen-protest-a92.notion.site/Docker-CI-CD-cf06950540f743f980de82cebd7d0e4d
