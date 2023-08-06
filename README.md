# MBTIGPT

- 진행 중인 프로젝트
- 서비스: http://mbtigpt.site/


<br>

<div align="center">
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"></a>
<a href="https://platform.openai.com/"><img src="https://img.shields.io/badge/OpenAI-FF5A00?style=flat-square&logo=openai&logoColor=white&color=black" alt="OpenAI"></a>
<a href="https://www.djangoproject.com/"><img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white" alt="Django"></a>
<a href="https://www.postgresql.org/"><img src="https://img.shields.io/badge/PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL"></a>
<a href="https://www.docker.com/"><img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker"></a>
<a href="https://nginx.org/en/"><img src="https://img.shields.io/badge/NGINX-009639?style=flat-square&logo=nginx&logoColor=white" alt="NGINX"></a>
<a href="https://cloud.google.com/"><img src="https://img.shields.io/badge/GCP-4285F4?style=flat-square&logo=google-cloud&logoColor=white" alt="GCP"></a>


</div>

##  Settings

```bash
git clone https://github.com/gangjoohyeong/MBTIGPT.git
```

<br>

**MBTIGPT/.env**
```
DB_NAME='postgres'
DB_USER='user'
DB_HOST='111.111.111.111'
DB_PASSWORD='password'
DB_PORT='5432'
```

**MBTIGPT/API.yaml**
```
OPENAI:
  API: sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**RUN**

```bash
docker-compose up --build
```




<br>

## Project architecture

<br>

<div align="center">

<img src="https://github.com/gangjoohyeong/MBTIGPT/assets/93419379/ed640f1e-7200-4000-a9cc-2d424749325f" width="800px" />

</div>

<br>

## UI / UX


<div align="center">


<img width="800" alt="스크린샷 2023-08-06 오후 4 24 57" src="https://github.com/gangjoohyeong/MBTIGPT/assets/93419379/1c27350d-ed7f-4d0b-97d9-e675d277d8aa">
<img width="800" alt="스크린샷 2023-08-06 오후 4 24 38" src="https://github.com/gangjoohyeong/MBTIGPT/assets/93419379/2e400590-ce0b-4e0a-9a33-9c1c355eb066">
<img width="800" alt="스크린샷 2023-08-06 오후 4 24 46" src="https://github.com/gangjoohyeong/MBTIGPT/assets/93419379/17384f8f-c0fa-4cbf-a9cd-a4eaedec8b44">
<img width="800" alt="스크린샷 2023-08-06 오후 4 24 51" src="https://github.com/gangjoohyeong/MBTIGPT/assets/93419379/a6ebc17f-dadd-4336-aa0b-5e561c869afa">
<img width="800" alt="스크린샷 2023-08-06 오후 4 25 04" src="https://github.com/gangjoohyeong/MBTIGPT/assets/93419379/83a0d906-b39a-4e98-9827-c3c9c2186237">





</div>

<br>

## TODO
  
- [x] DB를 PostgreSQL로 변경 후 GCE에 Docker로 올리기
- [x] 친구 사귀기 UI 업데이트
- [x] 유저 이름 추가해서 ID 대신 이름 추가하기
- [x] MBTI별 GPT 페르소나 업데이트 (Prompt Enginnering)
- [x] NGINX 웹서버 구축
- [x] 메인 서버 aistages에서 클라우드 서비스로 이관
- [ ] SSL 인증서 발급 (https)

<br>

## Thanks to

로고 제작: [이은지](https://github.com/eunjios)
