jenkins 설치

github 연동 확인

jenkins 에서 aws 명령어 확인

webhook 확인

beanstalk 확인



```
sudo wget -O /etc/yum.repos.d/jenkins.repo \
    https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
sudo yum upgrade -y
sudo yum install epel-release java-11-openjdk-devel -y
sudo amazon-linux-extras install epel -y
sudo yum install jenkins -y
sudo yum install java-11-amazon-corretto -y
sudo service jenkins restart
sudo systemctl enable jenkins

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws --version

sudo yum update -y
sudo yum install git -y

sudo cat /var/lib/jenkins/secrets/initialAdminPassword

# 플러그인 설치
gitlab

pipeline {
    agent any
    stages {
        stage('delete origin zip file'){
            steps{
                sh 'cd server && ls -al && rm -rf *.zip'
            }
        }
        stage('make zip file'){
            steps{
                sh 'cd server && zip -r beanstalk_${BUILD_NUMBER}.zip .'
            }
        }
        stage('upload to S3'){
            steps{
                sh 'cd server && aws s3 cp beanstalk_${BUILD_NUMBER}.zip s3://elasticbeanstalk-ap-northeast-1-090274807648 --region ap-northeast-1'
                
            }
        }
        stage('deploy'){
            steps{
                sh 'aws elasticbeanstalk create-application-version --region ap-northeast-1 --application-name django-tutorial --version-label beanstalk_${BUILD_NUMBER} --source-bundle S3Bucket="elasticbeanstalk-ap-northeast-1-090274807648",S3Key="beanstalk_${BUILD_NUMBER}.zip"'
                sh 'aws elasticbeanstalk update-environment --region ap-northeast-1 --environment-name django-env --version-label beanstalk_${BUILD_NUMBER}'
            }
        }        
    }
}


```