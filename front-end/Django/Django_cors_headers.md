# CORS

> 다른 포트에 있는 리소스(자원)을 가져오려면 CORS 인증받아야함.





## :one: CORS

> [MDN 참고문서](https://developer.mozilla.org/ko/docs/Web/HTTP/CORS)
>
> 비동기요청은 브라우저가 받아주지않는다.
>
> vue.js 홈페이지에서 localhost 로 비동기 요청을 보냈음.
>
> 응답의 헤더에 Access-Control-Allow-Origin 가 있어야 받아준다.



- [CORS-headers](https://github.com/adamchainz/django-cors-headers)

```shell
$ pip install django-cors-headers
```

1. settings.py 미들웨어에 하나 추가
2. 모든 설정 추가 or 화이트리스트 추가



