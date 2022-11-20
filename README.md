## MoonTomi Server Light

- FastAPI를 이용한 Light Server
- 더 적은 리소스로 운영하기 위해 Framework를 Spring Boot에서 FastAPI로 변경

### domains

- album
- artist
- comment
- image
- lecture

---
## Plan

- 가장 기본적인 Lecture, Lookup, Top10 부터 Serving
  - album, comment, image, lecture 우선 구현
  - Lookup 페이지를 위해, search (cursor, fetchSize)
- 향후 추가
  - review, column
  - season 별 페이지
  - playlist - Discord 연동
  - push (kakao? mail?)

---
## DB Schema 변경 계획

### album

  - genres를 album_genre table로 이전
    - genre를 JSON column으로 설정하면, genre category별 검색이 어렵다..

### lecture

  - rating을 avg query로 제공하기에는 가장 사용량이 많을 것으로 예상되기에, lecture table에 컬럼으로 추가
    - comment가 추가될 때 업데이트
