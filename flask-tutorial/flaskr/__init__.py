import os
# 파일 경로 등을 처리하기 위해 Python 표준 모듈인 os를 가져옴

from flask import Flask

# create_app은 애플리케이션 팩토리 함수
# Flask 앱을 생성하는 기본 함수
# 테스트 설정을 외부에서 주입할 수 있도록 test_config 파라미터를 받음
def create_app(test_config=None):
    
    # Flask 객체(app)를 생성하는 핵심 코드
    # Flask 인스턴스를 생성
    # 이 인스턴스가 전체 웹 애플리케이션의 핵심
    # __name__: 현재 Python 모듈의 이름
    #           현재 파일의 이름을 Flask에 넘겨서 앱의 위치를 알 수 있게 함
    #           현재 모듈의 위치 정보를 Flask에 전달
    #           Flask는 애플리케이션 루트 디렉터리를 알아야 정적 파일, 템플릿 등을 찾을 수 있음
    # instance_relative_config=True: 인스턴스 폴더 (instance/)의 설정 파일을 로드할 수 있도록 허용
    # 앱에게 설정 파일들이 인스턴스 폴더를 기준으로 한다고 알려줌
    # instance/ 디렉토리는 민감한 정보(DB 비밀번호 등)를 안전하게 보관할 수 있도록 프로젝트 폴더 밖에 따로 생성됨
    #           인스턴스 폴더는 flaskr 패키지 외부에 위치
    #           설정 비밀이나 데이터베이스 파일과 같이 버전 관리에 커밋되지 않아야 하는 로컬 데이터를 보관
    # 이 설정을 통해 Flask는 그곳에서 설정 파일을 찾게 됨
    app = Flask(__name__, instance_relative_config=True)
    
    # 앱이 사용할 몇 가지 기본 설정을 설정
    app.config.from_mapping(
        # SECRET_KEY: 보안에 필요한 키 (예: 쿠키 암호화, 세션 보호). 개발용으로 'dev'를 설정
        # Flask와 확장 기능들이 데이터를 안전하게 유지하기 위해 사용
        # 개발 중에는 편리한 값을 제공하기 위해 'dev'로 설정되지만, 실제 배포할 때는 꼭 안전한 무작위 값으로 바꿔야 함
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        # DATABASE: 데이터베이스 파일의 경로를 설정
        # instance/ 디렉토리 안에 flaskr.sqlite 파일로 저장
        # Flask는 instance/ 폴더를 앱의 데이터 저장소로 간주
        # 데이터베이스 파일은 그 안에 위치
    )

    if test_config is None:
        # 테스트 설정이 주어지지 않았을 때(즉, 일반 실행 시) 실행되는 조건
        app.config.from_pyfile('config.py', silent=True)
        # config.py 파일에서 설정을 로드
        # config.py: 배포 환경에서 개별적인 설정을 적용하기 위한 파일
        # 인스턴스 폴더 안의 config.py 파일에서 가져온 값들로 기본 설정을 덮어씀(만약 그 파일이 존재한다면)
        # 예를 들어, 배포 시 실제 SECRET_KEY, API 키, DB 비밀번호 등이 이곳에 들어갈 수 있음
        # silent=True: 파일이 없어도 조용히 넘어감
        # config.py를 통해 개발·테스트와 다른 배포 환경 설정을 별도로 관리 가능
        # 존재하지 않아도 에러가 나지 않도록 silent=True가 앞서 설정
    else:
        # 그 외의 경우에는 (test_config가 주어진 경우)
        # 테스트할 때는 별도의 설정(예: 테스트 전용 DB 등)을 적용해야 하므로, 테스트 설정을 함수에 직접 전달할 수 있게 설계
        app.config.from_mapping(test_config)
        # test_config 딕셔너리로부터 설정을 로드
        # 테스트 시에는 외부 설정 파일이 아닌, 파라미터로 주어진 설정을 적용

    # 인스턴스 폴더가 존재하도록 보장
    # 데이터베이스 파일 등이 저장될 instance/ 폴더를 미리 만듬
    # Flask는 인스턴스 폴더를 자동으로 생성하지 않지만,
    #  앞으로 진행할 프로젝트가 그곳에 데이터베이스 파일을 만들 것이기 때문에 그것은 반드시 존재해야 함
    try:
        os.makedirs(app.instance_path)
        # app.instance_path 디렉토리를 생성하려 시도
    except OSError:
        # 실패해도 무시
        pass
    # instance/ 폴더가 이미 존재하면 에러가 나기 때문에, try-except로 감싸서 에러를 무시

    # "hello"라고 말하는 간단한 페이지
    # /hello 경로로 접근하면 Hello, World!를 반환하는 hello 함수를 정의
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # app을 반환
    # 모든 설정이 끝난 Flask 애플리케이션 인스턴스를 반환
    # 이 객체가 실행 주체가 됨
    return app