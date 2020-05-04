# Django TemplateTags

장고의 MTV 패턴중에서 Template 에 커스텀으로 자신이 만든 태그와 필터를 적용할 수 있다.



## 1. 기본세팅하기

- 폴더 구조
  - `polls/` 앱안에 `templatetags` 폴더를 생성한다.
  - `gravatar.py` 생성

```python
 polls/
	__init__.py
	models.py
	templatetags/ # 여기다가 폴더 생성
		__init__.py 
		gravatar.py
  views.py
```



## 2. 사용하기

그리고, 나의 template 에서 사용하려면 불러와야 한다.

```html
{% load gravatar %}
```



Gravatar.py

```python
# gravatar.py

import hashlib
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def profile_url(email):
    # return hashlib.md5(email.encode('uft-8').strip().lower()).hexdigest()
    return f"https//s.gravatar.com/avatar/{hashlib.md5(email.encode('uft-8').strip().lower()).hexdigest()}?s=80"
```



_nav.html

```html
<!-- _nav.html -->
{% load gravatar %}

{% if request.user.is_authenticated %}
	<li class="nav-item">
		<a class="nav-link" href="{% url 'accounts:detail' request.user.id %}">    	
      <img src="{ { request.user.email|profile_url } }">
      {{ requeest.user.username }}님
    </a>
	</li>
```





# Models.py 에서 활용하기

- Model 과 연관이 있다면 @property 사용하기
  - 파이썬 문법 @property
    - getter, setter 비슷한 개념

```python
# models.py

class User(AbstractUser):
  followers = models.ManyToManyField(
    		settings.AUTH_USER_MODEL,
    		related_name='follwings'
  			)
  
  @property
  def gravatar_url(self):
    return f"https//s.gravatar.com/avatar/{hashlib.md5(self.email.encode('uft-8').strip().lower()).hexdigest()}?s=80"
```



```html
<!-- _nav.html -->
{% load gravatar %}

{% if request.user.is_authenticated %}
	<li class="nav-item">
		<a class="nav-link" href="{% url 'accounts:detail' request.user.id %}">    	
      <img src="{ { request.user.email|profile_url } }">
      <img src="{ { request.user.gravatar_url } }"> <!-- 이 부분 활용 -->
      {{ requeest.user.username }}님
    </a>
	</li>
```

