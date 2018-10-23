
- ## aws 접속
    - #### pem 권한
    <pre><code>chmod 0400 .ssh/my_private_key.pem</code></pre>

- ## aws 셋팅
    - #### 도커 설치
    <pre><code>sudo snap install docker</code></pre>
    - #### 젠킨스 설치
    <pre><code>sudo docker volume create jenkinsvol
  
  sudo docker run --name jenkins -d --restart always -p 8080:8080 -p 50000:50000 -v jenkinsvol:/var/jenkins_home -v /etc/localtime:/etc/localtime:ro jenkins:2.60.3</code></pre>
    - #### 젠킨스 셋팅
    
    - #### 타임존 변경
    <pre><code>sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime</code></pre>

- ## git hub 등록
    - https://github.com/latemorning/sichuan.git
    - create a new repository on the command line
    - <pre><code>echo "# sichuan" >> README.md
      git init
      git add README.md
      git commit -m "first commit"
      git remote add origin https://github.com/latemorning/sichuan.git
      git push -u origin master</code></pre>
    - push an existing repository from the command line
    - <pre><code>git remote add origin https://github.com/latemorning/sichuan.git
      git push -u origin master</code></pre>
    - 추적 제외
    - <pre><code>git rm -rf --cached .idea/</code></pre>


- ## 로컬 git 셋팅
    <pre><code>~/dev/workspace/python/sichuan
  git init</code></pre>
  
  
  
  git remote add origin https://github.com/latemorning/sichuan.git
  
  