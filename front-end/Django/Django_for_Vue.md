# Django for Vue

> Vue + API 
>
> [설치문서](https://django-rest-auth.readthedocs.io/en/latest/installation.html)
>
> [DRF 공식문서](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication)

```shell
$ pip install django-rest-auth django-allauth
```



**[ django-rest-auth ]**  

- 로그인
  - 토큰 발급
- 로그아웃
  - 토큰 삭제



**[ django-rest-auth ] + [ django-allauth ]**

- 회원가입도 시켜줌







## :one: 초기설정

```python
# settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # DRF
    'rest_framework',
    'rest_framework.authtoken',

    # rest_auth
    'rest_auth',

    # my Apps
    'accounts',
    'articels',
]



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}
```







JWT 토큰이 요근래에 많이 쓰이고 있다.

아이디.정보.사인