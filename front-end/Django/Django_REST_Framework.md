# Django REST Framework



## :one: API

> Application Programming Interface
>
> 개발자용 접점,
>
> 개발자가 쓸 수 있는 데이터



**1. 데이터의 표기법**

- Json
  - JavaScript object ~
- XML
  - eXtended Markup  Language ( W3C, 1996 )



`Django` 에서 `Json` 형식에 맞춰서 `Data` 만 제공한다.

MTV 패턴에서 Template 역할이 사라짐.



## :two: DRF ( Django Rest Framework )

> [공식문서](https://www.django-rest-framework.org/#) 
>
> ```shell
> $ pip install djangorestframework
> ```



```python
# settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework', # 이 부분 추가.
    'board',
]
```



```python
# models.py
from django.db import models
from faker import Faker

f = Faker()

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def dummy(cls, n):
        for _ in range(n):
            cls.objects.create(
                    title = f.name(),
                    content = f.text(),
                )
```



```python
# serializers.py
# modelForm 과 사용법이 유사하다.

from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'content']
        # fields = '__all__'
```



```python
# urls.py
from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('json1/', views.article_list_json_1),
    path('json2/', views.article_list_json_2),
    path('json3/', views.article_list_json_3),
]
```



```python
# views.py
from django.shortcuts import render, redirect
from django.http.response import JsonResponse, HttpResponse # json 으로 응답
from django.views.decorators.http import require_GET

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Article
from .serializers import ArticleSerializer

# Create your views here.
def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'board/article_list.html', context)

# 더이상 return render 가 아니다. 노가다방식 경험
@require_GET
def article_list_json_1(request):
    articles = Article.objects.all() # articles 는 querySet 이다.
    data = []
    for article in articles:
        data.append({
            'article_id': article.id,
            'title': article.title,
            'content': article.content,
            'created_at': article.created_at,
            'updated_at': article.updated_at,
        })
    return JsonResponse(data, safe=False)

# django core serializer
@require_GET
# @require_http_methods(['GET', 'POST'])
def article_list_json_2(request):
    from django.core import serializers

    articles = Article.objects.all()
    data = serializers.serialize('json', articles)

    return HttpResponse(data, content_type='application/json')

# rest framework
# 우리가 앞으로 만들어야 될 모습.
@api_view(['GET'])
def article_list_json_3(request):
    articles = Article.objects.all()
    # form = ArticleForm()
    serializer = ArticleSerializer(articles, many=True) # 쿼리셋일때 many=True 옵션 줘야함

    # rest_framework 의 serializer  를 리턴하려면, Respose 를 써야한다.
    return Response(serializer.data)
```

