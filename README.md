# practice_Flask
***

# Flask Official Documentation
- ⚗️[Flask](https://flask.palletsprojects.com/)⚗️

---

# Flask
- Flask는 Python으로 웹 서버를 만들 수 있게 해주는 마이크로 웹 프레임워크

---

# 기본 구조
1. Flask 클래스(웹 서버 생성용)를 flask 패키지에서 가져옴
    ```
    from flask import Flask
    ```
    - flask라는 웹 프레임워크에서 Flask 클래스만 가져옴
    - 정형화된 부분: 거의 모든 Flask 앱은 이 줄로 시작합니다.
    - An instance of this class will be our WSGI application
        - WSGI: Web Server Gateway Interface
            - 파이썬 웹 애플리케이션과 웹 서버 사이의 표준 인터페이스
            - 웹 서버(예: Gunicorn, uWSGI)와 웹 프레임워크(예: Flask, Django)가 서로 통신하기 위해 사용하는 규칙

2. Flask 앱 객체 생성
    ```
    app = Flask(__name__)
    ```
    - Flask 앱 인스턴스를 생성
    - __name__은 파이썬 내장 변수로, 현재 모듈의 이름을 의미
        - 문자열을 직접 넣을 수도 있지만, __name__을 쓰는 것이 정석이며 대부분의 공식 문서나 튜토리얼에서도 사용
    - Flask는 이 값을 사용해서 앱의 루트 경로, 정적 파일 경로 등을 설정
    - Flask 클래스로 app 이라는 인스턴스를 만듬
        - app은 객체(Object)이며, 동시에 인스턴스(Instance)이다.
            - 객체(Object): 데이터 + 기능을 가진 모든 것
            - 인스턴스(Instance): 특정 클래스에 의해 생성된 객체

3. 라우팅 정의: 특정 URL 요청이 왔을 때 어떤 동작을 할지 정의
    ```
    @app.route('/')
    ```
    - 데코레이터라고 하며, `'/'` 경로(URL)에 사용자가 접근했을 때, 바로 아래 함수(index)를 실행하라는 의미
        - 데코레이터(decorator): 함수 위에 @를 붙여서 사용하는 파이썬 문법
            - 기존 함수에 기능을 추가하거나 변경할 수 있게 해줌
    - 정형화된 형식이지만, `'/'`는 경로(path) 이므로 다른 경로로 자유롭게 변경 가능

    ```
    def index():
        return 'hi'
    ```
    - @app.route() 바로 아래에 있는 함수는 사용자가 해당 경로로 접속했을 때 호출
        - 함수 이름은 자유롭게 변경 가능, 다만 의미 있는 이름을 쓰는 것 추천
    - 함수의 **문자열 형태의 반환값**이 브라우저에 그대로 출력
        - 문자열을 반환하는 대신, HTML을 반환하거나 템플릿 파일을 사용 가능
    - The function returns the message we want to display in the user’s browser.
    - The default content type is HTML, so HTML in the string will be rendered by the browser.

4. Flask 애플리케이션 실행
    - Flask 2.2 이전 방식 (직접 실행)
        ```
        app.run(debug=True)
        ```
        - Flask 개발 서버를 실행시키는 코드
        - debug=True는 개발 시 매우 유용
            - 코드 변경 시 서버 자동 재시작
            - 에러 발생 시 상세한 디버깅 정보 출력
            - 바꿀 수 있는 옵션들
            ```
            app.run(debug=True, port=8080, host='0.0.0.0')
            ```
                - debug: 개발 모드 (자동 재시작 + 디버그 메시지)
                - port: 포트 번호 설정 (기본값: 5000)
                - host: 기본은 localhost (127.0.0.1), '0.0.0.0'은 외부에서 접속 가능하게 함
    - Flask 2.2부터
        - 터미널에 CLI 명령어를 아래와 같이 입력해 실행
            - 시스템 또는 가상환경의 **PATH에 flask 실행 파일이 있어야 함**
            - Scripts\flask.exe 또는 bin/flask가 인식되어야 함
            ```
            flask --app hello run
            ```
            - `flask`: Flask 프로젝트를 실행하거나 관리할 수 있게 해주는 명령어 프로그램
                - flask run: 서버 실행
            - `--app`: 내 앱이 어디에 있는지 알려주는 옵션
                - 뒤에 오는 값(hello)이 Flask 앱이 정의된 파일/모듈
                    - 파일 이름이 hello.py 일때
            - `hello`: --app의 값
                - 내 Flask 앱은 hello.py 파일에 있다
                - .py는 생략 (Flask가 자동으로 붙여줌)
                - hello.py 안에 반드시 Flask 앱 인스턴스 `(app = Flask(__name__))` 가 있어야 함
                - 만약 Flask 앱 인스턴스 이름이 app이 아니라면 아래와 같이 명시
                    - 예: `myapp = Flask(__name__)`인 경우
                        ```
                        flask --app hello:myapp run
                        ```
            - `run`: 실행 명령
                - 내부적으로 Flask는 app.run()을 호출해서 웹 서버를 띄움
                - 포트, 디버그 모드 등도 CLI 옵션으로 설정 가능
                    ```
                    flask --app hello run --debug --port 8080
                    ```
        - 파이썬 모듈을 통한 실행
            - 직접 실행 경로를 지정하는 방법
            - flask를 파이썬 모듈로 직접 실행
            ```
            python -m flask --app hello run
            ```
            - `-m`: 모듈 실행을 의미
            - **flask 명령어가 PATH에 없어도 동작함**
            - 특히 가상환경 내에서 안정적으로 실행 가능

---

# 서버
- 기본적으로 `flask run` 명령으로 서버를 실행하면, 해당 서버는 로컬에서만 접근 가능 (default)
    - 보안상의 위험: 디버깅 모드에서는, 애플리케이션의 사용자가 사용자의 컴퓨터에서 임의의 파이썬 코드를 실행할 수 있기 때문
- 아래의 명령어로 사용자의 컴퓨터가 가지고 있는 모든 네트워크 인터페이스 (와이파이, 유선 등)를 통해 접속을 허용 가능
    ```
    flask run --host=0.0.0.0
    ```            

---

# 디버그 모드
- flask run 은 단순히 Flask 앱을 실행하는 명령이지만, 디버그 모드를 활성화하면, 개발자에게 유용한 기능 두 가지가 추가
- 자동 재시작 (Auto-reload)
    - 코드에 변경을 가하면, 서버를 다시 시작하지 않아도 자동으로 리로드
- 상호작용형 디버거 (Interactive Debugger)
    - 웹 페이지에서 에러가 발생했을 때, 브라우저에 에러 메시지와 함께 Python 코드를 직접 실행해보며 원인을 추적할 수 있는 인터랙티브 도구가 뜸
- 이 기능은 보안상 위험할 수 있어서 운영 환경에서는 절대 사용하면 안 됨
    - arbitrary code 실행 가능성이 있기 때문
- 실제 서비스용 서버(운영 환경, production)에서는 절대 flask run이나 디버깅 기능을 사용하면 안 됨
    - 배포 시에는 WSGI 서버 (예: gunicorn, uWSGI) 등을 사용
- 디버그 모드를 활성화하려면 --debug 옵션을 사용
    ```
    flask --app hello run --debug
    ```

---

# HTML Escaping
- Escape: HTML 코드로 해석될 수 있는 문자들을 문자 그대로 보이게 만드는 처리
    - 예: `<` → `&lt;`
- Flask는 기본적으로 HTML을 반환하므로, 사용자 입력이 포함될 경우 스크립트 공격에 취약
- Jinja 템플릿을 사용할 경우에는 이러한 위험한 입력들을 자동으로 이스케이핑해 줌
- escape()는 직접적으로 이스케이핑을 수행하는 함수
- 실제 개발에서는 보안상 필수로 고려해야 하는 처리
- "신뢰되지 않은 데이터"란, 사용자가 입력한 내용, 외부 API 결과 등이며,
    이런 데이터를 그대로 HTML에 출력하면 위험

```
from markupsafe import escape

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
```

- 사용자가 `<script>alert("bad")</script>`라는 이름을 제출했다면,
    이스케이핑은 그것이 스크립트를 실행하는 대신, 텍스트로 렌더링되도록 만듬
- 이스케이핑을 하지 않으면 사용자가 의도적으로 악성 JavaScript 코드를 삽입할 수 있고,
    이는 XSS(크로스 사이트 스크립팅) 공격으로 이어질 가능성이 존재

---

# 라우팅
- 사용자들은 기억할 수 있고 직접 방문할 수 있는 의미 있는 URL을 사용하는 페이지를 더 좋아하고 다시 방문할 가능성이 더 높음
- Flask에서 특정 URL로 들어온 요청에 대해 어떤 함수가 실행될지 지정하려면 @app.route()를 사용
- URL의 일부를 동적으로 만들 수 있고, 여러 규칙을 하나의 함수에 연결 가능
```
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
```

## 라우팅의 변수 규칙
- <변수명> 형태로 URL 안에 변수를 넣으면, Flask가 그 값을 함수에 전달
- 선택적으로, `<converter:variable_name>`처럼 converter를 사용하여 인자의 타입을 지정 가능
```
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'
```
- `/post/10`처럼 접속하면 `10`을 자동으로 정수형(int)로 변환하여 `post_id = 10`으로 show_post() 함수에 들어감
- `<int:post_id>`는 정수 외의 값(ex: "abc")을 허용하지 않음

| types of Converter | |
|-----|-----|
| string | (default) accepts any text without a slash |
| int | accepts positive integers |
| float | accepts positive floating point values|
| path | like string but also accepts slashes|
| uuid | accepts UUID strings|

## 고유한 URL들 / 리디렉션 동작
```
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
```
- projects 엔드포인트에 대한 정식 URL(canonical URL)은 끝에 슬래시가 붙음
    - 이는 파일 시스템의 폴더와 유사합니다.
    - 만약 끝에 슬래시가 없는 URL(/projects)에 접근하면, 
        Flask가 자동으로 301 리디렉션을 해서 끝에 슬래시가 붙은 정식 URL(/projects/)로 이동
    - 그래서 /projects와 /projects/는 결과적으로 같은 페이지로 연결
- about 엔드포인트에 대한 정식 URL은 끝에 슬래시가 없음
    - 이는 파일의 경로(pathname)와 유사
    - 끝에 슬래시가 붙은 URL(/about/)에 접근하면 404 “찾을 수 없음” 오류가 발생
    - 이것은 이러한 리소스들에 대해 URL을 고유하게 유지하는 데 도움이 되며, 
        검색 엔진이 같은 페이지를 두 번 색인하지 않도록 도와줌
    - /about과 /about/이 다른 페이지로 인식되므로, 
        중복 색인(indexing)을 막을 수 있어 검색 엔진 최적화(SEO)에 유리

## URL 생성
- 특정 함수에 대한 URL을 생성하려면 url_for() 함수를 사용
    - 첫 번째 인자로 함수의 이름을 받고, 
        URL 규칙의 변수 부분 각각에 대응하는 여러 개의 키워드 인자를 받을 수 있음
    - 알려지지 않은(정의되지 않은) 변수 부분들은 URL에 쿼리 파라미터로 추가
- URL을 하드코딩하는 대신, URL 역방향 함수인 url_for()를 사용하는 이유
    - 역방향 생성(reversing)은 종종 URL을 하드코딩하는 것보다 더 명확
    - 하드코딩된 URL을 수동으로 변경해야 하는 것을 기억할 필요 없이, URL을 한 번에 바꿀 수 있음
    - URL 생성은 특수 문자의 이스케이핑을 자동으로 처리
    - 생성된 경로는 항상 절대 경로이며, 브라우저에서의 상대 경로로 인한 예기치 않은 동작을 피함
    - 애플리케이션이 URL 루트(/)가 아닌 /myapplication 같은 경로에 위치해 있다면, 
        url_for()는 그것을 적절히 처리
```
from flask import url_for

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))    // /
    print(url_for('login'))    // /login
    print(url_for('login', next='/'))    // /login?next=/
    print(url_for('profile', username='John Doe'))    // /user/John%20Doe
```
- python의 `with` 문: 문맥 관리자(Context Manager) 를 사용하기 위한 문법
    - 어떤 리소스(파일, 네트워크 연결, DB 등)를 열고 닫는 것을 자동으로 처리
    - 전통적인 방식
        ```
        f = open('file.txt')
        data = f.read()
        f.close()  # → 파일을 꼭 닫아줘야 함
        ```
        - 실수로 f.close()를 안 쓰면
             → 파일이 계속 열린 상태로 남아서 메모리 누수, 파일 잠금 문제 발생 가능
    - with 방식
        ```
        with open('file.txt') as f:
        data = f.read()
        ```
        - with는 블록이 끝나면 자동으로 f.close() 호출
             → 더 안전하고 깔끔
- app.test_request_context()란?
    - Flask에서 제공하는 특수한 문맥 관리자
    - Python 셸이나 테스트 환경에서 Flask에게 
        “지금 웹 요청을 하나 받고 있다고 가정해라” 라고 말해주는 역할
    - Flask의 url_for() 같은 함수는 요청 컨텍스트(request context) 내에서만 정상 작동
    - 웹 요청이 없으면 내부 정보가 없어서 URL 생성도 안 됨
    - test_request_context()를 쓰면 Flask가 마치 요청을 하나 받은 것처럼 행동
- `url_for('index')`
    - @app.route('/')에 연결된 index() 함수의 URL → '/'
- `url_for('login')`
    - @app.route('/login')에 연결된 login() 함수의 URL → '/login'
- `url_for('login', next='/')`
    - login 함수에 정의되지 않은 next는 쿼리 파라미터로 처리됨 → '/login?next=/'
- `url_for('profile', username='John Doe')`
    - `/user/<username>` 경로 → 'John%20Doe' (공백은 %20으로 인코딩됨)
    - URL에서는 공백을 직접 쓸 수 없음
    - 공백은 퍼센트 인코딩(percent encoding) 또는 URL 인코딩을 통해 `%20`으로 바뀜
    - 추가적으로
        - 공백, ! @, #, /, ? 가 각각 %20, %21, %40, %23, %2F, %3F 로 인코딩 됨
        - 이 인코딩 방식은 ASCII 문자 코드에 기반해 각 문자를 16진수로 변환한 값
    - url_for()는 이런 특수 문자들을 자동으로 인코딩하므로 'John%20Doe'의 결과가 나옴

## HTTP 메서드
- 기본적으로, 라우트는 오직 GET 요청들에만 응답
- 다른 HTTP 메서드들을 처리하기 위해 route() 데코레이터의 methods 인자를 사용 가능
- 메서드들을 하나의 함수 안에 함께 사용
    ```
    from flask import request

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            return do_the_login()
        else:
            return show_the_login_form()
    ```
    - GET과 POST 요청을 하나의 함수에서 처리하는 방식
    - request.method를 통해 현재 요청이 POST인지 GET인지 구분하고, 각각에 대해 다른 로직을 실행
- 서로 다른 메서드들에 대한 뷰들을 서로 다른 함수들로 분리
    ```
    @app.get('/login')
    def login_get():
        return show_the_login_form()

    @app.post('/login')
    def login_post():
        return do_the_login()
    ```
    - GET과 POST 요청을 별도의 함수로 분리
    - Flask 2.0 이후에는 `@app.get()`, `@app.post()` 같은 데코레이터가 제공되어 코드가 더 명확
- 만약 어떤 라우트에서 GET 메서드를 정의하면, Flask는 자동으로 HEAD 메서드도 지원하도록 설정
    - HEAD 요청이 들어오면, Flask는 본문 없이 응답 헤더만 반환하며, 이 동작은 HTTP 표준(RFC)에 따름
- Flask는 자동으로 OPTIONS 메서드도 구현
    - OPTIONS 요청이 들어오면, Flask는 해당 라우트에서 사용 가능한 HTTP 메서드 목록을 응답으로 제공

---

# 정적 파일 (Static Files)
- 정적(static) 파일은 내용이 바뀌지 않는 파일들을 칭함
- ex: CSS, JavaScript, 이미지 파일, 폰트 등
- Flask에서는 이 정적 파일들을 별도로 처리하는 방식을 제공
- Flask 프로젝트 폴더에 static 폴더만 만들면, 그 안의 파일은 /static/파일이름 형태로 접근 가능
- 정적 파일들에 대한 URL들을 생성하기 위해서는, 특별한 'static' 엔드포인트 이름을 사용
    ```
    url_for('static', filename='style.css')
    ```
    - 해당 파일은 파일 시스템 상에서 static/style.css로 저장되어 있어야 함

---

# 브라우저 탭 아이콘 (favicon)
- 웹사이트를 브라우저에서 열었을 때 탭에 표시되는 작은 아이콘
- `*.py`와 같은 파이썬 파일을 실행했을 때, favicon이 없으면 아래와 같은 에러가 발생
    - `"GET /favicon.ico HTTP/1.1" 404 -`
    - 브라우저가 웹사이트를 열면 자동으로 `http://yourserver/favicon.ico` 경로로 요청을 보내기 때문
    - 아이콘이 있으면 탭에 표시, 없으면 404 에러 발생
    - 필수 사항 아님
- 브라우저 탭 아이콘을 넣고 싶으면, `favicon.ico` 파일을 프로젝트에 추가
    - `*.ico`는 Windows 아이콘 파일 형식
    - 브라우저는 보통 `*.ico` 파일을 파비콘으로 인식해서 자동으로 로딩
- 적용하는 방법
    ```
        from flask import Flask, send_from_directory

        app = Flask(__name__)

        @app.route("/favicon.ico")
        def favicon():
            return send_from_directory("static", "favicon.ico")

        @app.route("/")
        def home():
            return "Hello, world!"

        if __name__ == "__main__":
            app.run()
    ```
    - static 폴더 하위에 `favicon.ico`를 넣으면 됨

---