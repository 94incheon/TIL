const form = document.querySelector('form');
const users = ['admin', 'ssafy', 'test'];

form.addEventListener('submit', function (event) {
  // 각 변수에 담기 위한 코드 입니다. 수정을 금합니다.
  event.preventDefault();
  const formData = new FormData(event.currentTarget);
  const userName = formData.get('username');
  const password = formData.get('password');
  const passwordConfirmation = formData.get('password_confirmation');
  // 개발자 도구를 통해 해당 값들을 모두 확인하세요.
  console.log(userName, password, passwordConfirmation);
  // 위의 값들을 활용하여, 회원가입 로직을 작성하시오.

  //가입된 회원이 아닌가
  if (users.indexOf(userName) != -1) {
    alert("존재하는 회원입니다.");
    return false;
  }

  //비밀번호가 일치하는가
  if (password != passwordConfirmation) {
    alert("비밀번호가 일치하지 않습니다.");
    return false;
  }

  //다 잘되었을때
  alert(userName + "님, 회원가입을 축하합니다.");


})
