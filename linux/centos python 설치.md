```bash
sudo yum -y install gcc openssl-devel libffi-devel bzip2-devel sqlite-devel
wget https://python.org/ftp/python/3.8.7/Python-3.8.7.tgz
tar xzf Python-3.8.7.tgz 
cd Python-3.8.7/
./configure --enable-optimizations
sudo make altinstall

vi ~/.bashrc
alias python="/usr/local/bin/python3.8" ## 이 줄을 추가한다

source ~/.bashrc

python -V
```
