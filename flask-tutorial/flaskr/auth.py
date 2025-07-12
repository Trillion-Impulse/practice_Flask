import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')
# 'auth'라는 이름의 블루프린트를 생성
# __name__은 현재 모듈 위치를 Flask에 알려주기 위해 필요
# 애플리케이션 객체처럼, 블루프린트도 어디에 정의되었는지 알아야 하므로 __name__이 두 번째 인자로 전달
# url_prefix='/auth'는 이 블루프린트에 정의된 모든 URL 앞에 /auth가 자동으로 추가
# 예: @bp.route('/login') → 실제 경로는 /auth/login

# 데코레이터 @bp.route는 URL /register를 register 뷰 함수와 연결
# Blueprint 객체인 bp를 사용하므로 실제 경로는 /auth/register 임
@bp.route('/register', methods=('GET', 'POST'))
def register(): # register 뷰 함수 정의
    if request.method == 'POST': # 요청이 POST인 경우 (폼을 제출한 경우)
        # HTTP 요청 방식 중 POST는 보통 폼 데이터를 서버로 전송할 때 사용
        # 이 조건을 통해 서버는 사용자가 폼을 작성하고 제출했는지를 판단
        
        username = request.form['username']
        password = request.form['password']
        # request.form은 제출된 폼의 키와 값들을 매핑하는 특별한 타입의 딕셔너리(dict)
        # request.form은 HTML 폼에서 보내진 데이터를 key-value 쌍으로 다루는 객체
        # 예를 들어 <input name="username">이면 request.form["username"]으로 가져올 수 있음

        db = get_db() # 데이터베이스 연결 객체 가져옴
        error = None # 초기 에러 변수는 None으로 설정

        # username과 password가 비어 있지 않은지 유효성 검사(validation)
        # 빈 값으로 사용자 등록을 허용해서는 안 되기 때문
        if not username: # username이 비어 있으면
            error = 'Username is required.'
        elif not password: # password가 비어 있으면
            error = 'Password is required.'

        if error is None: # 에러가 없을 경우
            try: # 유효성 검사를 통과한 경우에만 사용자 정보를 DB에 저장하여 실제 등록 절차를 완료
                db.execute( # db.execute는 사용자 입력을 위한 ? 플레이스홀더가 포함된 SQL 쿼리를 받고, 이 플레이스홀더를 대체할 값들의 튜플을 받음
                    # 데이터베이스 라이브러리는 이 값들을 이스케이프 처리하므로, SQL 인젝션 공격에 취약하지 않게 됨
                    "INSERT INTO user (username, password) VALUES (?, ?)", # 사용자 정보를 user 테이블에 삽입
                    # 쿼리를 직접 문자열로 조합하지 않고 플레이스홀더(?)를 사용함으로써, SQL 주입 공격을 막고 보안을 강화
                    (username, generate_password_hash(password)), 
                    # 평문 비밀번호는 보안상 매우 위험하므로 해싱이 필수
                    # 비밀번호는 해시함수로 암호화
                    # 해시된 값만 DB에 저장
                    # INSERT 같은 데이터 조작 SQL은 커밋을 해야 DB에 실제 반영
                    # 이 쿼리는 데이터를 수정하므로, 변경 사항을 저장하기 위해 이후에 db.commit()이 호출되어야 함
                )
                db.commit() # 데이터베이스에 커밋하여 저장
            except db.IntegrityError: # 만약 이미 존재하는 사용자일 경우 예외 발생
                # 데이터베이스의 user 테이블이 username에 대해 고유 제약 조건(UNIQUE)을 가지고 있을 때, 
                # 중복된 이름으로 INSERT를 시도하면 이 오류가 발생
                error = f"User {username} is already registered."
            else: # 예외가 발생하지 않았으면
                return redirect(url_for("auth.login")) # 로그인 페이지로 리다이렉트
                # 사용자 등록이 완료되면 로그인 화면으로 보내야 하므로 리디렉션
                # url_for()는 이름을 기반으로 로그인 뷰에 대한 URL을 생성
                # 이것은 URL을 직접 작성하는 것보다 바람직한데, 
                # 나중에 URL을 변경하더라도 그것을 참조하는 모든 코드를 바꿀 필요가 없기 때문
                # url_for('auth.login')은 auth 블루프린트 안의 login 뷰 함수의 URL을 찾아줌
                # 이렇게 하면 URL 경로(/auth/login)가 변경되어도 코드 전체를 수정하지 않아도 됨
                # redirect()는 이 URL을 받아 실제 HTTP 리디렉션 응답을 만듬

        flash(error) # 에러 메세지를 flash로 저장하여 템플릿에서 표시 가능하도록 함
        # flash()는 템플릿을 렌더링할 때 가져올 수 있는 메시지를 저장
        # flash()는 Flask의 메시지 전달 메커니즘으로, 일시적인 메시지를 저장하고 HTML에서 출력할 수 있게 해줌

    return render_template('auth/register.html')
    # 사용자가 처음으로 /auth/register에 접속하거나 검증 오류가 있을 경우 등록 폼 HTML 반환
    # GET 요청(처음 방문) 또는 유효성 검사 실패 후에는 폼 화면을 다시 보여줘야 합
    # render_template()는 Flask에서 HTML 파일을 로드하고 사용자에게 보여주는 함수

# 데코레이터 @bp.route는 URL /login를 login 뷰 함수와 연결
# Blueprint 객체인 bp를 사용하므로 실제 경로는 /auth/login 임
@bp.route('/login', methods=('GET', 'POST'))
def login(): # login 뷰 함수 정의
    if request.method == 'POST': # 요청이 POST인 경우 (폼을 제출한 경우)
        username = request.form['username']
        password = request.form['password']
        
        db = get_db()
        error = None

        # 데이터베이스에서 사용자 정보를 먼저 가져오고, 이후에 비밀번호 확인 등 검증에 사용
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
            # 데이터베이스에서 username이 일치하는 사용자를 검색
        ).fetchone() # fetchone()은 결과가 없으면 None, 있으면 첫 번째 행을 반환
        # fetchone()은 쿼리에서 한 행을 반환
        # 쿼리가 결과를 반환하지 않으면, None을 반환

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            # check_password_hash()는 제출된 비밀번호를 저장된 해시와 동일한 방식으로 해싱하고, 이를 안전하게 비교
            # 만약 일치한다면, 비밀번호는 유효
            # not이므로 일치하지 않으면 에러 메시지를 설정
            error = 'Incorrect password.'

        if error is None: # 에러가 없다면 (= 로그인 성공 시)
            # session은 요청 사이에 데이터를 저장하는 딕셔너리
            # session 딕셔너리를 사용하면 로그인 상태나 사용자 정보를 안전하게 유지 가능
            session.clear() # session.clear()로 이전 세션 데이터를 지움
            session['user_id'] = user['id'] # 현재 로그인한 사용자의 id를 세션에 저장
            # 이 데이터는 브라우저로 전송되는 쿠키에 저장되고, 이후의 요청들에서 브라우저가 이를 다시 보냄
            # Flask는 로그인 정보를 브라우저 쿠키에 저장하지만, 이를 암호화된 서명으로 보호
                # 1. 사용자가 로그인 정보를 입력하여 로그인 요청을 보냄 (POST)
                # 2. 서버가 로그인 정보 검증 후 사용자 ID를 session에 저장
                # 3. Flask가 session 내용을 서명(signed)된 쿠키로 만들어 브라우저에게 전송
                # 4. 브라우저가 이 쿠키를 저장
                # 5. 이후 요청마다 브라우저는 자동으로 쿠키를 서버에 전송
                # 6. 서버는 쿠키에서 세션 정보를 읽어 로그인 상태를 확인

            return redirect(url_for('index')) # 이후 url_for('index')로 리디렉션 (index 뷰로 이동)

        flash(error)

    return render_template('auth/login.html')
    # GET 요청일 경우 또는 로그인 실패 시
    # auth/login.html 템플릿을 렌더링하여 로그인 폼을 보여줌