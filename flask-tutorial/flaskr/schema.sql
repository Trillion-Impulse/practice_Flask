DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
/*
이미 해당 테이블이 존재하면 먼저 제거
초기화 시 중복 생성 오류를 방지하기 위한 안전한 초기화 패턴
*/

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);
/*
id: 고유한 정수형 ID, 자동 증가
username: 고유한 사용자 이름 (중복 불가)
password: 비밀번호 (해시 저장 예정)
*/

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);
/*
id: 게시글 고유 ID
author_id: 글쓴이의 user ID
created: 작성 시간, 기본값은 현재 시간 (CURRENT_TIMESTAMP)
title: 게시글 제목
body: 게시글 본문
FOREIGN KEY: author_id는 user 테이블의 id를 참조
게시글(post)은 사용자(user)와 관계를 맺고 있으며, 외래 키(Foreign Key)를 통해 연결
이를 통해 어떤 사용자가 어떤 글을 썼는지를 추적 가능
*/