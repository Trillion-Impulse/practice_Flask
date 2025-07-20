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

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')