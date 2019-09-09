# docker-selenium-chrome

## Getting Started

### 1) Build Dockerfile
```sh
docker build -t docker-selenium-chrome .
```

### 2) Run example

주어진 QUERY 문자열에 대한 검색결과 중 웹 페이지의 제목들을 크롤링해서 저장하는 예제입니다.

```sh
docker run -e QUERY=google -v [LOCAL_OUTPUT_PATH]:/app/output -t docker-selenium-chrome
```

### Output

- `./output/result-{QUERY}.txt`

```sh
구글(google)
Google - YouTube
Google Accounts: Sign in
정보 | Google
Welcome to My Activity - Google
비즈니스를 위한 애널리틱스 도구 및 솔루션 - Google 애널리틱스
The Keyword | Google
Google - The Keyword
```
