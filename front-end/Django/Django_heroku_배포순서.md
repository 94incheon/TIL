# Heroku 배포
Django Application 배포하기 (공식문서 재편집본)
(https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Deployment#requirements)

## I. Heroku 가입
### (1) heroku

### (2) C9 CLI 로그인
- c9에는 heroku가 이미 설치되어 있음
```shell
$ heroku --version
```
- CLI에서 heroku 로그인
```shell
$ heroku login -i
```
- 이메일, 비밀번호로 가입 가능

## II. Django 프로젝트 생성 및 배포 설정
### (1) 프로젝트 생성
```shell
$ mkdir django_pjt2
$ cd django_pjt2
```

### (2) 가상(독립) 환경 설정
- 가상환경 생성 및 실행
```shell
$ python -m venv venv
$ source venv/bin/activate
```

### (3) 패키지 설치
- Django 관련 패키지 및 배포를 위한 패키지 설치
```shell
$ pip install django dj-database-url gunicorn whitenoise
```

### (4) Django 프로젝트 생성
- Django 프로젝트 생성
```shell
$ django-admin startproject django_pjt2 .
```

## III. (중요) 배포 설정
### (1) `Procfile`
- `Procfile` 파일 생성 후 다음의 내용 추가
```
web: gunicorn django_pjt2.wsgi --log-file -
```
- `web: gunicorn <프로젝트명>.wsgi --log-file -`
- :cupid:**(주의) `<프로젝트명>`에는 반드시 프로젝트 폴더명을 적어야 함**

### (2) `requirements.txt`
- 패키지 리스트 requirements 파일 생성
```shell
$ pip freeze > requirements.txt
```
- `requirements.txt`에 `psycopg2` 패키지 추가
```shell
dj-database-url==0.5.0
Django==2.1.15
...
psycopg2
```

### (3) `runtime.txt`
- `runtime.txt` 파일 생성 후 다음의 내용 추가
```
python-3.7.6
```
- 현재 C9의 python 버전과 일치시켜 줌

### IV. 세부설정
#### (1) `settings.py` 설정
1. `settings.py` 최하단에 다음의 내용 추가(Database 관련)
```python
# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
```

2. `settings.py` 최하단에 다음의 내용 추가(static 파일 관련)
```python
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# The URL to use when referring to static files (where they will be served from)
STATIC_URL = '/static/'
```

3. `whitenose` 미들웨어 추가하기
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # 추가하기
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

4. `settings.py` 최하단에 다음의 내용 추가
```python
# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### (2) 기타 `settings.py` 내용 설정
- ALLOWED_HOSTS 내용 추가
  - 추후에 헤로쿠앱 URL 생성 후 변경
```
ALLOWED_HOSTS = ['*']
```
## V. Git을 통한 heroku 배포
### (1) `.gitignore` 추가
- django용 gitignore 템플릿(http://gitignore.io/api/django)
- `venv` 환경 추가
```
...

venv/
```

### (2) `git`으로 현재 상태 버저닝
```
$ git init
$ git add .
$ git commit -m "first commit"
```

### (3) heroku 앱 생성 및 앱으로 코드 push
1. heroku 앱 생성
```shell
$ heroku create [앱이름]
```
2. remote 확인 -> heroku 라는 이름의 remote 확인 가능
```shell
$ git remote -v
```
3. heroku 리모트 서버로 git push
```shell
$ git push heroku master
```

### django 로켓 확인후 개발 시작 :)

## VI. 추가 설정
### (1) 배포용 설정 사항 확인
- 다양한 배포 관련 설정 상태 확인
```shell
$ python3 manage.py check --deploy
```

### (2) Secret Key

### (3) local, production 설정 분리

TBC...



- 헤로쿠에 배포할때 비어있는 새로운 DB를 만들었기 때문에 실행할 것

```shell
$ heroku run python manage.py migrate

# 필요하면 할 것, fixtures 폴더안에 json파일 있어야함
$ heroku run python manage.py loaddata [json파일]
```





:cupid: 배포 오류 잡기

- Heroku 환경 변수 설정하기
  - Decouple 라이브러리로 가렸던 `.env` 환경변수 설정해주었음.

```shell
# master -> master (pre-receive hook declined) 에러
# 환경 변수 설정
$ heroku config:set DISABLE_COLLECTSTATIC=1

치면 해결가능.

```



:cupid: Heroku CLI 주요 명령어

[참고문서](https://hi-dev.tistory.com/45)





## 마지막 실행

```shell
$ heroku open
```

