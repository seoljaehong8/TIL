# vue, nodejs 설치

```bash
$ sudo apt update
$ sudo apt upgrade
$ sudo apt install npm (6.14.4)
$ sudo atp install nodejs (10.19.0)
$ sudo npm install -g @vue/cli
$ vue create vue-test
$ cd vue-test
$ npm run serve
```



# 도커설치

```bash
$ sudo apt update
$ sudo apt install apt-transport-https ca-certificates curl software-properties-common
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
$ sudo apt update
$ sudo apt-get install docker-ce docker-ce-cli containerd.io
$ docker -v
$ sudo systemctl enable docker && service docker start
```

https://docs.docker.com/engine/install/ubuntu/

https://blog.dalso.org/linux/ubuntu-20-04-lts/13118

