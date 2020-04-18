# Django Message

## 1. Views 와 Templates 에서 Message 사용하기

### View

```python
# import 부분
from django.contrib import messages

# 정석방법
messages.add_message(request, messages.INFO, 'Hello world.')

# 숏컷 단축 명령어
messages.debug(request, '%s SQL statements were executed.' % count)
messages.info(request, 'Three credits remain in your account.')
messages.success(request, 'Profile details updated.')
messages.warning(request, 'Your account expires in three days.')
messages.error(request, 'Document deleted.')
```



### Templates

- 일반적으로 `base.html` 에서 메시지를 보여주는것이 좋다.
- 부트스트랩을 적용해서 색 입히는것도 좋음.
  - `CDN` 또는 `static` 파일을 사용해서 bootstrap4 가져오기

```django
{% if messages %}
<ul class="messages">
    {% for message in messages %}
    <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
    {% endfor %}
</ul>
{% endif %}

<!-- 부트스트랩 적용 -->
{% if messages %}
    <div class="messages">
        {% for message in messages %}
        <div class="alert alert-{% if message.tags %}{{ message.tags }}{% endif %}" role="alert">
            {{ message }}
        </div>
        {% endfor %}
    </div>
{% endif %}
```

