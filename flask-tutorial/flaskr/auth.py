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

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')