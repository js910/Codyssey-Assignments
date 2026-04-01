# AI/SW 개발 워크스테이션 구축 과제
<br>

## 1. 프로젝트 개요
- 목표: 도커를 이용한 로컬 개발 환경 구축 및 웹 서버 컨테이너화
<br>

## 2. 실행 환경
- OS: macOS (OrbStack)
- Shell: zsh
- Docker Version: (나중에 채우기)
- Git Version: (나중에 채우기)
<br>

## 3. 수행항목 체크리스트
- [ ] 터미널 기초 실습 및 로그 기록
- [ ] 파일 권한(755, 644) 실습
- [ ] Docker 설치 및 hello-world 확인
- [ ] Dockerfile 작성 및 커스텀 이미지 빌드
- [ ] 포트매핑 및 볼륨 설정
- [ ] Github 연동 완료
<br>

## 4. 터미널 조작 로그
### 1. Git 설정 확인
> **깃허브 연결**
>
> <img src="./01-github-link.png" width="600">
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

> ### 권한 숫자 계산법
> 
> 권한은 **4(읽기), 2(쓰기), 1(실행)**의 조합으로 구성됩니다.
>
> | 숫자 | 권한 (rwx) | 디렉토리에서의 의미 |
> | :--- | :--- | :--- |
> | **7** | `rwx` | 읽기, 쓰기, **접근(cd)** 모두 가능 |
> | **5** | `r-x` | 읽기 및 **접근(cd)** 가능 (일반적) |
> | **4** | `r--` | 목록만 확인 가능 (**접근 불가**) |
>
> **주의사항**
> * **`-R` 옵션:** 디렉토리 내부 모든 파일에 일괄 적용할 때 사용
> * **홀수 권한:** 디렉토리는 실행 권한(+1)이 있어야 `cd`로 입장 가능

3. **파일 관리 (`cp`, `mv`, `rm`)**
   - `cp sample.txt backup.txt`: 파일 복사
   - `mv backup.txt renamed.txt`: 파일 이름 변경
   - `rm sample.txt`: 원본 파일 삭제

> **Note:** 상세 실행 로그는 [assignment_log.txt](./assignment_log.txt) 파일에서 확인 가능합니다.
<br>

### 5. 도커 실행 결과

* **실행 명령어:** `docker run hello-world`
* **결과 요약:** 도커 클라이언트가 `hello-world`를 가져오고, 컨테이너를 생성하여 실행하는 데 성공함.
> **도커 실행 성공 화면**
>
> <img src="./03-docker-hello.png" width="600">
<br>

## 6. 트러블슈팅
### ① git push rejected & pull divergence
* **문제:** 로컬에서 작업 완료 후 `git push`를 시도했으나 `[rejected]` 에러가 발생하며 거절당함.
* **원인가설:** GitHub 웹사이트에서 직접 README를 수정했기 때문에, 원격 저장소에 로컬에는 없는 새로운 커밋이 생겨서 이력이 어긋났을 것으로 추측함. `pull`을 하면 해결될 것이라 예상함.
* **확인:** `git pull`을 실행했으나 `fatal: Need to specify how to reconcile divergent branches` 메시지가 출력됨. 깃이 두 갈래로 갈라진 이력을 합치는 방법(Merge 또는 Rebase)을 정해주지 않아 멈춘 것을 확인.
* **해결:** 이력을 하나로 묶어주는 가장 확실한 방법인 **Merge** 방식을 쓰기 위해 `git config pull.rebase false` 설정을 적용함. 이후 다시 `pull`을 수행하여 `Merge made by the 'ort' strategy` 메시지와 함께 이력을 성공적으로 합침.
> **[참고] 트러블슈팅 실행 화면**
>
> <img src="./02-trouble-git.png" width="600">