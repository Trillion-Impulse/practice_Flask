from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
# abort(404)처럼 HTTP 오류 응답을 강제로 발생시키는 데 사용

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)
# 'blog'라는 이름의 블루프린트를 생성
# __name__은 현재 모듈 위치를 Flask에 알려주기 위해 필요
# 애플리케이션 객체처럼, 블루프린트도 어디에 정의되었는지 알아야 하므로 __name__이 두 번째 인자로 전달
# auth 블루프린트와는 달리, blog 블루프린트는 url_prefix가 없음
# 따라서 url_prefix가 없기 때문에 blog의 index 뷰가 루트(/)에 위치
# 이는 블로그 기능을 이 앱의 메인 기능으로 간주하기 때문에 최상위로 둔다는 뜻

# bp는 Blueprint 객체이며, / URL 경로로 접근하면 아래 함수를 실행
# 블로그의 홈페이지(URL 루트 경로) 가 이 함수와 연결
@bp.route('/')
def index(): # 위에서 연결한 라우트('/')에 해당하는 뷰 함수
                # 브라우저에서 루트 URL(/)에 접속하면 이 index() 함수가 실행
    db = get_db()
    posts = db.execute( # 변수는 이후 템플릿에 넘겨줘서, HTML에서 게시글 목록을 출력할 때 사용
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC' # 결과를 작성일자(created) 기준으로 내림차순 정렬
                                # 가장 최근 글이 맨 위에 표시
    ).fetchall() # SQL 쿼리를 실행한 결과를 전부 가져옴
    # fetchall()은 리스트 형태로 결과를 반환하며, 각 항목은 하나의 게시글을 나타냄
    return render_template('blog/index.html', posts=posts)
    # 'blog/index.html'이라는 템플릿 파일을 불러오고, posts 데이터를 넘겨줌
    # 템플릿에서는 이 posts를 반복문 등으로 활용하여 화면에 게시글 목록을 출력

# bp는 Blueprint 객체이며, / URL 경로로 접근하면 아래 함수를 실행
# /create 경로를 처리하는 라우팅 함수
@bp.route('/create', methods=('GET', 'POST'))
@login_required # 해당 뷰에 접근하기 위해 로그인이 필요
def create():
    if request.method == 'POST': # 요청이 POST인 경우 (폼을 제출한 경우)
        # request.form은 제출된 폼의 키와 값들을 매핑하는 특별한 타입의 딕셔너리(dict)
        title = request.form['title']
        body = request.form['body']

        error = None # 초기 에러 변수는 None으로 설정

        if not title: # title이 비어 있으면
            error = 'Title is required.'

        if error is not None: # 에러가 있을 경우
            flash(error)
        else:
            db = get_db() # 데이터베이스 연결 객체 가져옴
            db.execute( # db.execute는 사용자 입력을 위한 ? 플레이스홀더가 포함된 SQL 쿼리를 받고, 이 플레이스홀더를 대체할 값들의 튜플을 받음
                        # 데이터베이스 라이브러리는 이 값들을 이스케이프 처리하므로, SQL 인젝션 공격에 취약하지 않게 됨
                'INSERT INTO post (title, body, author_id)' # 게시글 정보를 post 테이블에 삽입
                ' VALUES (?, ?, ?)', # 쿼리를 직접 문자열로 조합하지 않고 플레이스홀더(?)를 사용함으로써, SQL 주입 공격을 막고 보안을 강화
                (title, body, g.user['id'])
                # INSERT 같은 데이터 조작 SQL은 커밋을 해야 DB에 실제 반영
                # 이 쿼리는 데이터를 수정하므로, 변경 사항을 저장하기 위해 이후에 db.commit()이 호출되어야 함
            )
            db.commit() # 데이터베이스에 커밋하여 저장
            return redirect(url_for('blog.index')) # 글 작성이 완료되면 blog.index 뷰로 리디렉션

    return render_template('blog/create.html')
    # POST가 아닌 경우 (또는 오류가 있는 경우), create.html 템플릿을 렌더링하여 글쓰기 페이지를 표시


def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post