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
            # sqlite3.register_converter(
            #    "timestamp", lambda v: datetime.fromisoformat(v.decode())
            # ) 를 작동하기 위한 옵션
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

# init_db() 함수는 get_db()를 사용하여 DB 연결을 가져옴
def init_db():
    db = get_db()
    # get_db는 데이터베이스 연결을 반환하며, 이 연결은 파일에서 읽은 명령어들을 실행하는 데 사용

    # open_resource()함수는 Flask에서 제공하는 애플리케이션 내부 리소스 파일 열기 도구
    # flaskr/schema.sql처럼 애플리케이션 패키지 내부 경로를 기준으로 파일을 읽기 모드로 안전하게 염
    # 경로를 절대 경로나 상대 경로로 직접 지정하지 않아도 되기 때문에, 개발환경/배포환경 어디에서든 작동
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
        # executescript()는 여러 SQL 문장을 한꺼번에 실행 가능
        # decode('utf8')는 파일 내용을 UTF-8로 디코딩하여 문자열로 변환
    
    # with current_app.open_resource("schema.sql") as f:
    # schema.sql 파일을 읽기모드로 열어서 파일 객체 f에 담는다
    # Flask 애플리케이션 패키지 (flaskr) 내부의 상대 경로 기준으로 파일을 찾음
    # with 문을 사용했기 때문에, 파일을 다 쓰고 나면 자동으로 닫힘
    # f는 schema.sql 파일의 바이트 스트림 파일 객체입니다. (텍스트가 아니라 bytes)

    # f.read().decode("utf-8")
    # 파일을 한 번에 읽어서 UTF-8로 디코딩된 문자열로 변환
    # f.read() → 파일 전체 내용을 bytes 형식으로 읽습니다.
    # .decode("utf-8") → bytes를 문자열(str)로 변환합니다.
    # schema.sql은 일반 텍스트 파일이므로 UTF-8 디코딩이 필요
    # 예: b"CREATE TABLE user (...);" → "CREATE TABLE user (...);"

    # db.executescript(...)
    # 읽은 SQL 문장을 한 번에 실행
    # executescript()는 여러 개의 SQL 문장이 포함된 하나의 문자열을 받아, 이를 순차적으로 실행
    # 만약 executescript() 대신 execute()를 썼다면, SQL 한 문장만 실행 가능

# Flask는 내부적으로 Click이라는 Python 라이브러리를 사용해 커맨드라인 명령어(CLI)를 정의
# 개발자가 명령어를 통해 데이터베이스 초기화, 샘플 데이터 삽입, 관리자 계정 생성 등의 작업을 터미널에서 자동으로 실행할 수 있도록 함
# @click.command('init-db'): Flask CLI에서 사용할 수 있는 init-db라는 커맨드라인 명령어를 정의
@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    # 명령어를 실행하면 init_db() 함수를 호출하여 DB를 초기화
    click.echo('Initialized the database.')
    # 완료 후 'Initialized the database.'라는 메시지를 출력
# 사용 예: $ flask init-db

# sqlite3.register_converter()를 호출하는 것은 데이터베이스에 있는 timestamp 값들을 어떻게 해석할지 파이썬에게 알려주는 것
# SQLite와 Python 간의 데이터 타입 변환을 자동화
# SQLite에서 timestamp 타입으로 저장된 값(예: '2025-07-07 10:00:00')을 
# Python 코드에서 자동으로 datetime.datetime 객체로 변환해 주도록 설정
# datetime.datetime은 파이썬에서 날짜와 시간(날짜+시각) 정보를 표현하고 조작하기 위한 표준 객체
# SQLite는 timestamp 컬럼에 날짜와 시간을 문자열 형태로 저장
# 파이썬에서는 이런 값을 datetime.datetime 객체로 변환해야 날짜 계산이 편리해짐
# sqlite3.register_converter(type_name, converter_func)
# type_name: SQLite에 정의된 데이터 타입 이름 (여기서는 "timestamp")
# converter_func: 바이트(byte) 값을 파이썬 객체로 바꾸는 함수
# "timestamp"이라는 타입을 만났을 때, lambda v: datetime.fromisoformat(v.decode())를 사용해서 변환
sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)
# lambda v: datetime.fromisoformat(v.decode())
# v: SQLite가 전달하는 값은 bytes 타입
# v.decode() → UTF-8로 디코딩 → '2025-07-07 10:00:00' (str)
# datetime.fromisoformat(...) → 문자열을 datetime 객체로 변환
# 결과: datetime.datetime(2025, 7, 7, 10, 0, 0)
# 설정이 작동하려면, sqlite3.connect() 호출 시
# detect_types=sqlite3.PARSE_DECLTYPES 옵션이 있어야 함