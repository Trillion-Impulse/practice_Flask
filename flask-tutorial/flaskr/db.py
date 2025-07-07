import sqlite3
from datetime import datetime

import click
from flask import current_app, g
# current_app은 현재 실행 중인 Flask 앱 인스턴스를 가리킴
# Flask의 앱 팩토리 패턴을 쓸 때는 앱 객체가 전역에 존재하지 않음
# get_db는 애플리케이션이 생성되어 요청을 처리하고 있을 때 호출되므로 current_app을 사용
# g는 Flask에서 요청 단위의 전역 저장소
# 요청 하나가 처리되는 동안만 살아 있는 공간으로, 
# 이 안에 DB 연결을 저장해두면 같은 요청 내에서는 효율적으로 재사용 가능


def get_db():
    if 'db' not in g:
        # sqlite3.connect()는 config['DATABASE']에 지정된 경로에 연결을 시도
        # 파일이 없으면, init-db 명령 등을 통해 나중에 데이터베이스를 초기화하면 파일이 생성됨
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
        # sqlite3.Row는 연결에게 행(row)을 딕셔너리처럼 동작하게 반환하라고 지시
        # 기본적으로 SQLite는 결과를 튜플로 반환
        # row_factory를 sqlite3.Row로 설정하면, row['username']처럼
        # 컬럼명을 키로 사용해서 데이터에 접근 가능

    return g.db

# close_db는 g.db가 설정되었는지를 확인함으로써 연결이 생성되었는지를 검사
def close_db(e=None):
    db = g.pop('db', None)

    # 연결이 존재하면, 그것을 닫음
    # 이후에는 애플리케이션 팩토리에서 애플리케이션에게 close_db 함수에 대해 알려주어, 
    # 각 요청 후 이 함수가 호출되도록 할 것
    if db is not None:
        db.close()