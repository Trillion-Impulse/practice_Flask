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

# 템플릿 렌더링
- Flask는 HTML 코드 안에 사용자 입력을 넣을 때 보안 문제를 방지하기 위해 HTML을 이스케이프해야 함
    - Flask는 그것을 간편하게 하기 위해 Jinja2 템플릿 엔진을 자동으로 구성해 줌
- 템플릿은 모든 종류의 텍스트 기반 출력을 생성하는 데 사용 가능
    - HTML, markdown, 이메일용 일반 텍스트 등
- 템플릿을 렌더링(HTML로 변환)하기 위해서는 `render_template()` 메서드를 사용
    - HTML 파일 이름과, 템플릿 안에서 사용할 변수들을 넘겨주면 됨
    ```
    from flask import render_template

    @app.route('/hello/')
    @app.route('/hello/<name>')
    def hello(name=None):
        return render_template('hello.html', person=name)
    ```
    - /hello/ 또는 /hello/이름으로 접속했을 때 hello.html이라는 템플릿을 렌더링
    - 템플릿 안에서 사용할 변수 person에 name을 전달
- Flask는 기본적으로 템플릿을 찾을 때 templates 폴더를 자동으로 탐색
    - 모듈로 작성한 경우에는 .py 파일 옆에, 패키지로 구성한 경우에는 패키지 내부에 있어야 함
    - 모듈 형태
        ```
        /application.py
        /templates
            /hello.html
        ```
    - 패키지 형태
        ```
        /application
            /__init__.py
            /templates
                /hello.html
        ```
- Flask는 Jinja2 템플릿 엔진을 기반으로 작동하므로, 
    Jinja2의 강력한 기능들(조건문, 반복문, 필터 등)을 자유롭게 사용 가능
    ```
    <!doctype html>
    <title>Hello from Flask</title>
    {% if person %}
        <h1>Hello {{ person }}!</h1>
    {% else %}
        <h1>Hello, World!</h1>
    {% endif %}
    ```
    - `{{ person }}`: 템플릿에 전달된 변수 값을 출력
    - `{% if %}, {% else %}, {% endif %}`: Jinja2의 조건문 구문
    - person이라는 변수가 존재하면 해당 이름으로 인사하고, 없으면 "Hello, World!"를 출력
- 템플릿 안에서는 config, request, session, 그리고 g 객체들뿐만 아니라 
    url_for() 함수와 get_flashed_messages() 함수에도 접근 가능
    - config: Flask 설정에 접근
    - request: 클라이언트의 요청 정보
    - session: 사용자별 세션 정보
    - g: 요청 중 임시로 저장할 수 있는 글로벌 공간
        - "global"의 줄임말
        - 하나의 요청 동안 임시로 데이터를 저장할 수 있는 객체
    - url_for(): 라우팅된 URL을 생성
    - get_flashed_messages(): flash 메시지를 가져오는 함수
- 템플릿은 상속이 사용될 경우 특히 유용
    - 여러 HTML 페이지에 공통으로 들어가는 부분(헤더, 푸터 등)을 매번 반복 작성하지 않고, 
        기본 템플릿을 만들어 상속받는 구조로 효율적으로 관리 가능
- Flask는 자동으로 HTML 이스케이핑을 해줌
    - HTML이 정상적이고 안전한 것이라면 Markup 클래스나 |safe 필터를 사용하여 이스케이핑을 방지 가능
    ```
    from markupsafe import Markup

    Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'
    # 결과: Markup('<strong>Hello &lt;blink&gt;hacker&lt;/blink&gt;!</strong>')

    Markup.escape('<blink>hacker</blink>')
    # 결과: Markup('&lt;blink&gt;hacker&lt;/blink&gt;')

    Markup('<em>Marked up</em> &raquo; HTML').striptags()
    # 결과: 'Marked up » HTML'
    ```
    - Markup(...): 이 문자열을 안전한 HTML로 표시
    - Markup.escape(...): 문자열을 HTML-safe 하게 이스케이프
    - .striptags(): HTML 태그를 제거하고 텍스트만 남김

---

# Request Data에 접근
- 웹에서 클라이언트(사용자)가 어떤 입력을 보내든 서버는 그것에 반응해야 하며, Flask는 이를 위해 `request`라는 객체를 제공
- `request` 객체는 전역(global) 으로 존재
- 전역 객체가 여러 사용자 요청에서 동시에 접근되면 충돌이 생기지 않을까?
    - Flask는 동시에 여러 요청을 처리할 수 있어야 하므로, 스레드 안전성이 매우 중요
    - Flask는 이 문제를 해결하기 위해 컨텍스트 로컬(context local) 이라는 개념을 사용
        - context local: 요청마다 분리된 컨텍스트에서 request 객체가 각각 독립적으로 작동하도록 해주는 기술

## Request 객체
- Flask의 request 객체는 클라이언트로부터 들어온 HTTP 요청 정보를 담고 있는 핵심 객체
- Request 객체는 Flask의 공식 문서의 API 섹션에 문서화되어 있음
- 일반적인 작업 예시
    ```
    from flask import request

    @app.route('/login', methods=['POST', 'GET'])
    def login():
        error = None
        if request.method == 'POST':
            if valid_login(request.form['username'],
                        request.form['password']):
                return log_the_user_in(request.form['username'])
            else:
                error = 'Invalid username/password'
        # the code below is executed if the request method
        # was GET or the credentials were invalid
        return render_template('login.html', error=error)
    ```
    - request 객체를 사용하려면 반드시 flask 모듈에서 import 해야 함
    - 예시의 요청 메서드는 method 속성과 form 속성을 사용함으로써 이용 가능
    - `request.method`: 현재 들어온 요청이 'GET'인지 'POST'인지를 문자열로 반환
    - `request.form`: POST 또는 PUT 요청에서 넘어온 HTML 폼 데이터를 딕셔너리 형태로 접근할 수 있게 해줌
    - POST 요청이면, 폼으로 제출된 username과 password를 꺼내어 로그인 검사
    - 인증에 실패하면 에러 메시지를 띄우고, 성공하면 로그인 처리
    - GET 요청일 경우 혹은 로그인 실패 시, 로그인 폼(login.html)을 렌더링
    - 폼 속성 안에 키가 존재하지 않는다면 무슨 일이 발생할까?
        - request.form['username']처럼 딕셔너리 방식으로 접근할 때, 
            만약 'username'이라는 키가 존재하지 않으면 Python의 KeyError가 발생
        - Flask에서는 이 경우 예외를 따로 처리하지 않으면 자동으로 HTTP 400 (Bad Request) 에러 페이지를 반환
        - 따라서 대부분의 경우, 예외 처리를 하지 않아도 기본적인 안전 장치가 작동
    - URL 안에 제출된 매개변수들(?key=value)에 접근하기 위해서는 args 속성을 사용 가능
        - GET 요청에서 URL 끝에 붙는 쿼리스트링(예: /search?key=hello)은 request.args를 통해 접근
        ```
        searchword = request.args.get('key', '')
        ```
        - request.args는 ImmutableMultiDict 객체이며, 딕셔너리처럼 사용 가능
        - get() 메서드를 사용하면 키가 없을 때 기본값을 설정 가능
            - 위 예제에서는 'key'가 없으면 빈 문자열을 반환
    - URL 쿼리스트링은 사용자가 직접 수정할 수 있으므로, 
        존재하지 않는 키에 대해 request.args['key']로 바로 접근하면 KeyError가 발생하고 400 에러가 뜰 수 있음
        - 사용자 입장에서 이런 에러 페이지는 불편하게 느껴질 수 있기 때문에, get()을 통해 안전하게 접근하는 것을 권유

## 파일 업로드
- Flask에서는 클라이언트가 업로드한 파일을 쉽게 받을 수 있음
    - HTML `<form>` 요소에 enctype="multipart/form-data"를 반드시 추가
        - 이 설정이 없으면 브라우저는 파일을 서버로 보내지 않음
- 간단한 사용 예
    ```
    from flask import request

    @app.route('/upload', methods=['GET', 'POST'])
    def upload_file():
        if request.method == 'POST':
            f = request.files['the_file']
            f.save('/var/www/uploads/uploaded_file.txt')
    ```
    - 파일은 request.files라는 딕셔너리 속성에 저장됨
        - 키는 `<input type="file" name="...">`의 name 값
    - request.files['the_file']는 파일을 읽을 수 있는 객체(Python 파일 객체처럼 동작)를 반환
        - 이 파일 객체는 save(path) 메서드를 제공하므로, 지정된 경로로 서버의 파일 시스템에 저장 가능
    - /upload 경로에 POST 요청이 오면 the_file이라는 이름으로 전송된 파일을 /var/www/uploads/uploaded_file.txt 경로에 저장
- 클라이언트가 보낸 파일 이름을 다룰 때 생기는 보안 문제
    - file.filename은 클라이언트에서 업로드된 원래 파일 이름
        - 하지만 이 값은 사용자가 임의로 조작할 수 있기 때문에 신뢰할 수 없음
    - 따라서 filename을 저장 경로로 쓸 경우, 
        반드시 werkzeug.utils의 secure_filename() 함수를 통해 안전한 파일 이름으로 바꿔야 함
        - 이 함수는 특수 문자, 경로 문자 등을 제거하고 안전하게 만들어줌
    ```
    from werkzeug.utils import secure_filename

    @app.route('/upload', methods=['GET', 'POST'])
    def upload_file():
        if request.method == 'POST':
            file = request.files['the_file']
            file.save(f"/var/www/uploads/{secure_filename(file.filename)}")
    ```
    - 사용자가 보낸 파일을 서버에 저장할 때 안전한 파일 이름으로 바꾸어 /var/www/uploads/ 경로에 저장

## Cookies
- cookies는 사용자의 브라우저에서 서버로 전송된 데이터를 저장하거나 가져오는 데 사용
- `request.cookies`: 클라이언트가 보낸 쿠키들을 담고 있는 딕셔너리
- `response.set_cookie`: 서버에서 클라이언트에게 쿠키를 설정할 때 사용
- 보안을 위해, 민감한 데이터는 세션(Session)을 사용하는 것이 권장
    - 세션은 쿠키 위에 암호화나 서명 등 보안 요소가 추가된 구조
- Reading cookies
    ```
    from flask import request

    @app.route('/')
    def index():
        username = request.cookies.get('username')
        # use cookies.get(key) instead of cookies[key] to not get a
        # KeyError if the cookie is missing.
    ```
    - `request.cookies.get('username')`는 
        'username'이라는 이름의 쿠키가 존재하면 값을 반환하고, 없으면 None을 반환
    - `request.cookies['username']`처럼 대괄호로 접근할 경우, 
        해당 키가 없으면 KeyError가 발생하므로 .get()을 사용하는 것이 안전
- Storing cookies
    ```
    from flask import make_response

    @app.route('/')
    def index():
        resp = make_response(render_template(...))
        resp.set_cookie('username', 'the username')
        return resp
    ```
    - 쿠키는 응답(Response) 객체에 설정해야 하므로, 먼저 `make_response()`로 응답 객체를 생성
    - 그런 다음 `set_cookie()`를 통해 'username'이라는 이름으로 값을 저장
    - 마지막으로 이 응답 객체를 반환하여 클라이언트가 쿠키를 저장할 수 있도록 함
- 일반적으로 Flask는 문자열을 반환하면 내부적으로 응답(Response) 객체로 변환해 줌
    - 그러나 쿠키를 설정해야 하는 경우, 응답 객체를 직접 생성해야 하므로 make_response()를 사용
- 보통 쿠키는 응답 객체가 만들어진 후 설정되지만, 응답 객체 없이도 쿠키를 설정해야 하는 경우
    - Flask의 `after_request`, `before_request`, `teardown_request` 같은 콜백 시스템을 활용해 대응

---

# Redirects and Errors
- `redirect()`: 사용자를 다른 엔드포인트(페이지나 라우트)로 보내는 데 사용
    - redirect: 다른방향으로 전환
- `abort()`: 특정 HTTP 에러 상태 코드를 응답하며 요청을 강제로 종료
    - 예: 404, 401 등
- 예
    ```
    from flask import abort, redirect, url_for

    @app.route('/')
    def index():
        return redirect(url_for('login'))

    @app.route('/login')
    def login():
        abort(401)
        this_is_never_executed()
    ```
    - /로 접근하면 login이라는 이름의 함수(= 엔드포인트)로 리디렉션
    - /login에서 401 에러를 발생시키므로, 그 이후 코드 (this_is_never_executed())는 실행되지 않음
        - 401은 인증되지 않은 사용자에게 접근을 거부할 때 사용
- Flask는 기본적으로 에러가 발생하면 아주 단순한(흑백의) 에러 페이지를 표시
    - errorhandler(에러코드) 데코레이터를 사용하면, 해당 에러에 대한 사용자 정의 페이지를 만들 수 있음
    ```
    from flask import render_template

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('page_not_found.html'), 404
    ```
    - 404 에러 발생 시 'page_not_found.html'이라는 HTML 파일을 렌더링해서 사용자에게 보여줌
    - 두 번째 인자로 404를 명시함으로써, 응답의 상태 코드가 200 OK가 아닌 404 Not Found로 설정
    - render_template()만 반환하면 Flask는 정상 응답(200)을 보냈다고 간주
    - 그래서 명시적으로 404 같은 에러 코드를 지정해 줘야 브라우저나 클라이언트가 정확하게 인식

---

# About Responses
- Flask에서는 뷰 함수에서 값을 반환하면, Flask가 알아서 HTTP 응답 객체로 바꿔줌
    - 문자열을 반환하면, HTML 페이지처럼 응답 본문으로 사용되고, 상태 코드 200이 자동으로 붙음
    - 리스트나 딕셔너리를 반환하면, Flask가 jsonify() 함수를 호출해서 JSON 형태로 응답을 만들어 줌
- Flask가 다양한 반환 형태에 따라 응답 객체를 생성하는 단계
    - 응답 객체(flask.Response 등)를 직접 만들었다면, Flask는 그대로 반환
    - 문자열이면, 해당 데이터를 사용하여 기본 파라미터로 응답 객체가 생성
        - 문자열은 HTML 콘텐츠로 간주되며, 상태코드 200, MIME 타입 text/html이 적용
    - 문자열이나 바이트를 반환하는 반복자 또는 제너레이터이면, 스트리밍 응답으로 처리 됨
        - 데이터를 한 번에 보내는 대신, 점진적으로 전송하는 "스트리밍 방식" 응답으로 처리
    - 딕셔너리나 리스트이면, jsonify()를 사용하여 응답 객체가 생성됨
    - 튜플이 반환되면, 튜플 안의 항목들이 추가 정보를 제공할 수 있음
        - 튜플은 (response, status), (response, headers), 또는 (response, status, headers) 형태여야 함
        - 상태(status) 값은 상태 코드를 덮어쓰며, 헤더는 추가적인 헤더 값을 담은 리스트나 딕셔너리가 될 수 있음
        - 뷰 함수에서 튜플을 사용하면 상태 코드나 헤더 값을 직접 설정 가능
    - 위의 어떤 것도 적용되지 않으면, Flask는 반환 값이 유효한 WSGI 애플리케이션이라고 가정하고 그것을 응답 객체로 변환
- 뷰 내부에서 생성된 응답 객체를 직접 다루고 싶다면, make_response() 함수를 사용
    - 예: 헤더를 추가하고 싶은 경우
    - 기본 반환 방식 대신 명시적으로 응답 객체를 생성할 수 있게 해줌
    ```
    from flask import render_template

    @app.errorhandler(404)
    def not_found(error):
        return render_template('error.html'), 404
    ```
    - 404 에러가 발생했을 때 error.html 템플릿을 렌더링하고, 상태 코드를 404로 설정하여 응답
    - (response, status) 형태의 튜플을 반환하는 예시
    ```
    from flask import make_response

    @app.errorhandler(404)
    def not_found(error):
        resp = make_response(render_template('error.html'), 404)
        resp.headers['X-Something'] = 'A value'
        return resp
    ```
    - make_response()로 반환 표현식을 감싸고, 응답 객체를 얻은 뒤 수정한 다음 반환하면 됨
    - 이 예제는 응답 객체에 직접 헤더를 추가하는 방법을 보여줌
    - make_response()를 사용하면 응답 객체에 자유롭게 접근할 수 있어, 
        커스텀 헤더를 추가하거나 쿠키를 설정하는 등 다양한 조작이 가능

## APIs with JSON
- API를 작성할 때의 흔한 응답 형식은 JSON
    - Flask에서는 API를 만들 때, 
        dict(딕셔너리)나 list(리스트) 형태의 값을 리턴하면 Flask가 자동으로 이를 JSON으로 변환
    - 별도로 jsonify()를 호출하지 않아도, Flask가 내부적으로 변환 작업을 처리
- 예
    ```
    @app.route("/me")
    def me_api():
        user = get_current_user()
        return {
            "username": user.username,
            "theme": user.theme,
            "image": url_for("user_image", filename=user.image),
        }

    @app.route("/users")
    def users_api():
        users = get_all_users()
        return [user.to_json() for user in users]
    ```
    - `user.to_json()`은 커스텀 메서드로, 사용자 객체를 JSON 직렬화 가능한 형태로 변환
        - 보통 데이터베이스 모델(예: SQLAlchemy 모델)은 바로 JSON으로 변환할 수 없음
        - 그래서 .to_json() 같은 커스텀 메서드를 정의
            - 예를 들면 return {"id": self.id, "name": self.name} 같은 식
            - JSON 직렬화가 가능한 형태로 바꿔줍
- 반환하려는 데이터가 단순한 자료형이 아니라 클래스 인스턴스(예: SQLAlchemy 모델)인 경우, 
    해당 데이터를 JSON으로 직렬화할 수 있도록 직접 변환해 주어야 함
- `JSON 직렬화 가능(JSON serializable)`하다는 것은, 숫자, 문자열, 불린값, 리스트, 딕셔너리 등 기본 자료형만 포함되어야 한다는 뜻
    - 예: datetime, set, 사용자 정의 클래스 같은 것은 JSON 직렬화가 불가능하므로 추가 작업이 필요
- SQLAlchemy 모델, 사용자 정의 객체 등은 JSON으로 바로 변환할 수 없기 때문에 직렬화 도구가 필요
    - marshmallow, pydantic, Flask-RESTful, Flask-Marshmallow 등 
        라이브러리는 모델을 JSON으로 자동 변환하거나 필드 유효성 검사, 중첩 구조 표현 등을 도와줌

---

# Sessions
- Flask에서는 사용자의 요청(request) 외에도, 사용자별 정보를 여러 요청 사이에 유지할 수 있도록 session이라는 객체를 제공
    - 예를 들어 사용자가 로그인했는지를 기억하는 데 사용
- Flask의 세션은 HTTP 쿠키(cookie) 를 사용하여 작동
    - 일반 쿠키와 달리 암호 서명을 하여 보안성을 높임
    - 쿠키는 사용자 브라우저에 저장되지만, 그 내용이 변경되지 않았음을 Flask가 확인할 수 있게 되어 있음
- 세션 정보는 사용자의 브라우저에 저장되므로 내용을 볼 수는 있지만, Flask는 암호 서명을 통해 위변조를 방지
    - 비밀 키(secret key) 를 모르면 쿠키 값을 바꿔도 Flask가 그것을 거부
- session을 사용하기 전에, Flask 앱에 secret_key 값을 설정해야 함
    - 이 키는 쿠키 서명에 사용되며, 외부에 유출되면 안 됨
- 예
    ```
    from flask import session

    # Set the secret key to some random bytes. Keep this really secret!
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    @app.route('/')
    def index():
        if 'username' in session:
            return f'Logged in as {session["username"]}'
        return 'You are not logged in'

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return '''
            <form method="post">
                <p><input type=text name=username>
                <p><input type=submit value=Login>
            </form>
        '''

    @app.route('/logout')
    def logout():
        # remove the username from the session if it's there
        session.pop('username', None)
        return redirect(url_for('index'))
    ```
    - `app.secret_key`: 서명을 만들 때 사용하는 키
    - session['username'] = ... 이 실행되면:
        - Flask는 이 데이터를 JSON 형태로 직렬화한 뒤
        - secret_key로 서명하고
        - 서명된 데이터를 쿠키로 브라우저에 보냄
        - 이후 브라우저가 다시 요청을 보낼 때, Flask는 쿠키 안의 세션 데이터를 secret_key로 검증
            - 서명이 맞지 않으면 세션은 무효 처리
    - secret_key가 변경되면 이전에 저장된 세션 쿠키는 더 이상 유효하지 않게 됨
        - 따라서 서버를 재시작할 때마다 secret_key를 바꾸지 않도록, 환경 변수나 설정 파일을 통해 고정된 값을 사용
- 쿠키 기반 세션에 대한 주의사항
    - Flask의 기본 세션은 클라이언트 측 쿠키에 저장되며, session[...]에 넣은 값들이 모두 쿠키 안에 담김
    - 브라우저는 일반적으로 쿠키 크기 제한이 있으며(보통 4KB), 이를 초과하면 데이터가 잘리거나 무시될 수 있음
    - 세션 값이 저장되지 않거나 갑자기 사라지는 문제가 생긴다면, 쿠키 용량 초과가 원인일 수 있음
- 기본적으로 Flask는 세션을 클라이언트(사용자 브라우저)의 쿠키에 저장
    - 더 복잡하거나 안전한 세션 관리가 필요할 경우, 서버 측 저장 방식을 선택 가능
        - 이를 위해 Flask는 다음과 같은 확장 기능들을 제공
            - Flask-Session, Flask-KVSession, Flask-Redis, Flask-SQLAlchemy 등
            - 이런 확장 기능은 세션 데이터를 서버의 메모리, 데이터베이스, 파일, Redis 등 다양한 저장소에 저장하게 해 줌

## 좋은 비밀 키를 생성하는 방법
- 보안을 위해 secret_key는 예측 불가능하고 충분히 무작위(random)적이어야 함
- 운영체제는 보통 secrets 같은 암호학적으로 안전한(random secure) 라이브러리를 통해 난수를 생성 가능
- Flask에서 이 키는 세션 데이터의 무결성을 보호하는 데 사용되므로, 
    단순한 문자열이나 사람이 만든 값보다 보안 수준이 높은 난수를 사용해야 함
- 32바이트 길이의 난수를 16진수(hex) 문자열로 출력
    ```
    $ python -c 'import secrets; print(secrets.token_hex())'
    ```
    - 이 값을 그대로 Flask의 app.secret_key에 복사해서 사용

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