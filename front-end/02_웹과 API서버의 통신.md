# 웹과 API서버의 통신

> 브라우저는 최종적으로 웹을 화면에 그렸습니다.
>
> 그 이후 사용자들이 웹을 사용하게 됩니다.

`이후 페이지 이동을 제외하고는 대부분 API 서버와 통신하게 됩니다.`



[API을 알아보자](https://www.grabbing.me/8d9e92b19e084c5a8cb173a695aa81af#1837c3e178cf4f0bbe9cc097cd07662f)



이 때 사용자가 로그인을 하기 위해 정보(이메일, 패스워드)를 입력하고 로그인하기를 누른다고 가정해보겠습니다.

<img src="https://www.grabbing.me/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fe9585227-129c-4722-b95d-3fe1ef5143d8%2FUntitled.png?table=block&amp;id=c3293a24-6c68-4650-8a76-5a0dd3498218&amp;width=860&amp;cache=v2" style="zoom: 50%;" />

1. **브라우저는 웹 서버에게 요청하는 것이 아닌 API 서버에게 요청을 하게 됩니다.**

<img src="https://www.grabbing.me/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F568dcaf5-a530-4f97-b145-3dc39ed3676a%2FUntitled.png?table=block&amp;id=ecac063f-e443-4c46-a000-1fe52a720d97&amp;width=860&amp;cache=v2" style="zoom:50%;" />

2. **백엔드 API 서버에서는 로그인 정보를 바탕으로 인증정보를 확인하고 브라우저에게 로그인 결과를 전달합니다.**

![](https://www.grabbing.me/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F52a549a9-c472-4eba-af1b-a6dd020ef0fd%2FUntitled.png?table=block&id=21036603-2bae-4d68-83f9-eb28067dfa84&width=860&cache=v2)

3. **API 결과를 바탕으로 해서 메인 페이지로 이동시키라는 javascript 코드가 실행됩니다. (실제로는 더 복잡한 코드가 실행됩니다)**



```
마이페이지에서 유저 정보를 가져오거나, 상품 정보들을 받아오는 등 우리가 서비스를 이용하면서 필요한 데이터들은 거의 전부 API 서버를 통해 받아온다고 생각해도 됩니다.
```



아래는 우리가 사용하는 웹이 최종적으로 만들어지기까지의 과정입니다.

![](https://www.grabbing.me/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ff1b14587-e413-4265-82ba-58a6d28c784c%2FUntitled.png?table=block&id=d7ad3277-c3d9-4f81-9882-d0890358641d&width=1920&cache=v2)



[백엔드 API서버에 대해 더 자세하게 알아보기](https://www.grabbing.me/69a68655ae9c46efaeae5014b9f9034d#7ea94b1c25ac44f297445c83ce84d4b5)