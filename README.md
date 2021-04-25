# 🌿 Greatingdor
Greatingmall Clone Project

## ⚡️ Backend
- [이서진](https://github.com/leechanmul)
- [이윤형](https://github.com/YunhyungLee)
- [함경재](https://github.com/hiyee-gj)

## 🐝 Period
- 2021.04.12 ~ 2021.04.22

## 🐍 Skill
- Django
- MySQL

## 💡 Implement Function
### 회원가입
- bcrypt 사용해서 비밀번호 byte화
- validation.py 작성해서 유효성 검사
- Q 사용해서 데이터 중복 여부 확인
### 로그인
- bcrypt 사용해서 비밀번호 비교 확인
- query parameter 사용해서 
- JWT 사용해서 인가 token 발행
### 상품 전체 목록
- Q 사용해서 검색하는 필터 구현
- 빈 Q 사용해서 여러 조건 담아서 필터 구현
- pagination offset/limit 계산해서 구현
- list comprehension 사용
### 상품 상세 정보
- GET/:id 형태로 RESTful API 구현
- 모델 객체와 참조, 역참조를 이용해 데이터 가공
- 이미지, 태그는 배열 형태로 전송
### 상품 옵션
- 필요한 데이터를 뽑아 할인 가격 연산 후 전송
### 상품 리뷰
- request에 page 번호와 page_size를 받아서 페이징 구현
- 데이터베이스에서 작성 시각 최신 순서로 정렬
- 페이징에 따라 원하는 만큼만 슬라이스 후 데이터 전송
### 장바구니
- decorator 사용으로 인가 확인
- get or create로 True/False 값 사용
- pass variable 사용으로 delete method 구현