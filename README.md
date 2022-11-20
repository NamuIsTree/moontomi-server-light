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