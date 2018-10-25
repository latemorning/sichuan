
- ## aws 접속
    - #### pem 권한
    <pre><code>chmod 0400 .ssh/my_private_key.pem</code></pre>
    - #### 접속
    <pre><code>ssh -i /home/harry/.ssh/my_private_key.pem ubuntu@ip....</code></pre>
        
- ## AWS 셋팅
    - #### 타임존 변경
    <pre><code>sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime</code></pre>
    
    - #### 도커 설치
    <pre><code>sudo snap install docker</code></pre>
    
    - #### Django + uWSGI + Nginx 설치
        - ##### 도커 HUB URL
            <pre><code>https://hub.docker.com/r/dockerfiles/django-uwsgi-nginx/</code></pre>
        - ##### 소스 checkout
            <pre><code>git clone https://github.com/dockerfiles/django-uwsgi-nginx.git</code></pre>
        - ##### docker build
            <pre><code>sudo docker build -t webapp .</code></pre>
        - ##### webapp start
            <pre><code>docker run --name webapp -d -p 80:80 webapp</code></pre>
        - ##### 연동 작업 참고
            <pre><code>https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html?highlight=Django
          </code></pre>
                
    - #### 젠킨스
        - ##### 설치
        <pre><code>sudo docker volume create jenkinsvol
      sudo docker run --name jenkins -d --restart always -p 8080:8080 -p 50000:50000 -v jenkinsvol:/var/jenkins_home -v /etc/localtime:/etc/localtime:ro jenkins/jenkins:lts</code></pre>
    
        - ##### Jenkins 관리 - Global Tool Configuration
        - ##### Jenkins 관리 - 플러그인 관리
            - ###### Publish over SSH 플러그인 설치
        - ##### Jenkins 관리 - 시스템 설정
            - ###### Publish over SSH 서버 추가
                <pre><code>Publish over SSH - SSH Servers 추가</code></pre>
        - ##### 개별 빌드 구성
            <pre><code>소스 코드 관리 Git 설정
          빌드 유발 GitHub hook trigger for GITScm polling 체크
          Build - Send files or execute commands over SSH
            - 시스템 설정에 추가한 서버 선택
            - Exec command 추가
                - </code></pre>
        - ##### 기타
            <pre><code>인증파일을 jenkins 컨테이너에 복사
          /var/jenkins_home/인증서.pem</code></pre>
                              
        - ###### item 설정
        <pre><code>이름 입력
      Freestyle project
      소스 코드 관리 -> Git
        Repositories - Repository URL -> https://github.com/latemorning/sichuan.git
                     - Credentials -> git hub id/pass 정보로 생성 후 선
      </code></pre>
        
    - #### mariadb
        - ##### 도커 URL
        <pre><code>https://hub.docker.com/_/mariadb/</code></pre>
        
        - ##### 설치 & 실행
        <pre><code>sudo docker pull mariadb:10.3.10
      sudo docker volume create mariadbvol
      sudo docker run --name mariadb -e MYSQL_ROOT_PASSWORD=my-secret-pw -d -p 3306:3306 -v mariadbvol:/var/lib/mysql -v /etc/localtime:/etc/localtime:ro mariadb:10.3.10
      </code></pre>
        
        - ##### 사용자 추가
        <pre><code>create user '계정아이디'@'접속위치' identified by '패스워드';</code></pre>
        
        - ##### DB 생성
        <pre><code>create database DB명;</code></pre>
        
        - ##### 권한 주기
        <pre><code>grant all privileges on DB이름.테이블 to '계정아이디'@'접속위치';
      grant all privileges on sichuan.* to 'sichuan'@'%';</code></pre>
        
    - #### phpmyadmin
        - ##### 설치
        <pre><code>docker pull phpmyadmin/phpmyadmin:4.8.3
      sudo docker run --name myadmin -d --link mariadb:db -p 8087:80 phpmyadmin/phpmyadmin:4.8.3</code></pre>


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
  
  
- ## 웹서버 설치


- ## Django 소스 코딩
    - #### settings.py (mariaDB)
    <pre><code>DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db-name',
        'USER': 'user-name',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
  }
</code></pre>


- 소스 업로드
- nginx uwsgi 설정
- docker compose로 변경