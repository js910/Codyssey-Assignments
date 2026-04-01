# AI/SW 개발 워크스테이션 구축 과제

## 1. 프로젝트 개요
- 목표: 도커를 이용한 로컬 개발 환경 구축 및 웹 서버 컨테이너화

## 2. 실행 환경
- OS: macOS (OrbStack)
- Shell: zsh
- Docker Version: (나중에 채우기)
- Git Version: (나중에 채우기)

## 3. 수행항목 체크리스트
- [ ] 터미널 기초 실습 및 로그 기록
- [ ] 파일 권한(755, 644) 실습
- [ ] Docker 설치 및 hello-world 확인
- [ ] Dockerfile 작성 및 커스텀 이미지 빌드
- [ ] 포트매핑 및 볼륨 설정
- [ ] Github 연동 완료

## 4. 터미널 조작 로그
### 1. Git 설정 확인
![깃허브 연결](01-github-link.png)
```bash
izzzar00788078@c6r9s1 Assignment-1-Docker % git config --global user.name "js910"
izzzar00788078@c6r9s1 Assignment-1-Docker % git config --global user.email "jysong0914@gmail.com"
izzzar00788078@c6r9s1 Assignment-1-Docker % git config --list
credential.helper=osxkeychain
user.name=js910
user.email=jysong0914@gmail.com
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
core.ignorecase=true
core.precomposeunicode=true
remote.origin.url=https://github.com/js910/Codyssey-Assignments.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.main.remote=origin
branch.main.merge=refs/heads/main
```
### 2. 터미널 실습 로그
본 실습은 `script` 명령어를 통해 기록되었으며, 주요 수행 내역은 다음과 같습니다.

1. **디렉토리 생성 및 이동**
   - `mkdir test`: 실습용 디렉토리 생성
   - `cd test`: 디렉토리 진입

2. **파일 생성 및 권한 변경 (`chmod`)**
   - `touch sample.txt`: 빈 파일 생성
   - `chmod 755 sample.txt`: 실행 권한 부여 (rwxr-xr-x)
   - `chmod 644 sample.txt`: 읽기/쓰기 권한으로 복구 (rw-r--r--)

3. **파일 관리 (`cp`, `mv`, `rm`)**
   - `cp sample.txt backup.txt`: 파일 복사
   - `mv backup.txt renamed.txt`: 파일 이름 변경
   - `rm sample.txt`: 원본 파일 삭제

> **Note:** 상세 실행 로그는 [assignment_log.txt](./assignment_log.txt) 파일에서 확인 가능합니다.
