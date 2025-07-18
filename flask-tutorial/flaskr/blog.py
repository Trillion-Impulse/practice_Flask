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