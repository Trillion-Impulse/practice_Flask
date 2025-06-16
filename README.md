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
        CLI에 아래와 같이 입력해 실행
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