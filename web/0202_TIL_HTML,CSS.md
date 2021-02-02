# HTML

- HTML(Hyper Text Markup Language)
  - 웹 페이지를 작성하기 위한 언어
  - 웹 컨텐츠의 **구조를 정의**
- 구조
  - head
    -  해당 문서의 정보를 담고 있다.(제목, 문제 인코딩)
    - 외부 로딩 파일 지정도 할 수 있다. (link)
  - body 
    - 브라우저 화면에 실질적으로 나타나는 정보
  - DOM(Document of Model) tree: 부모관계, 형제관계
  - 요소(element) 
    - 태그와 내용으로 구성
    - 태그별로 사용하는 속성은 다르다.
    - 시멘틱 태그 : 의미론적 요소를 담은 태그
  - 그룹 컨텐츠 : p, hr, ol, ul, pre, blockquote, div
  - 텍스트 관련 요소 : a, b, i, span, img, em, strong
  - 테이블 관련 : tr, td, th, thead, tbody, tfoot, caption, colspan, ...
  - form 태그
    - 입력받은 데이터와 함께 서버에 요청해 주는 태그
    - action : 요청하는 서버의 주소를 설정하는 속성
    - input : 다양한 타입을 가지는 입력데이터 필드 설정할 수 있다.
      - text, checkbox, radio, range, date, ...
      - name(데이터를 담을 이름, 변수명), placeholder, required, disabled, autofocus, ...
      - label tag : 서식에 입력의 이름표 같은 역할, input의 id 값과 연결.





# CSS

- 스타일, 레이아웃 등을 표시하는 방법을 지정하는 언어

- 적용방법

  1. 인라인 방식 : 관리가 힘듦. 테스트용
  2. 내부 참조 : `<style>`태그 사이에 css 문법을 사용하는 방식. 모든 html 에 적용할 수없다.
  3. 외부 참조 : `<link>`태그에 css 파일 경로를 명시해서 사용하는 방식. 유지보수가 수월

- 선택자

  - 특정한 요소를 선택하기 위해서 필요

  - 기초선택자

    - 전체 선택자(*), 요소(element) 선택자
    - 아이디 선택자, 클래스 선택자, 속성 선택자

  - 고급 선택자

    - 자손 선택자 : 띄워쓰기로 구분, 하위의 모든 요소

      `article p { color: red; }`

    - 자식 선택자 : `>` 로 구분, 바로 아래의 요소

      `article > p { color: blue; }`

    - 형제 선택자 : `~` 로 구분, 같은 계층(레벨)에 있는 요소

      `p ~ section { color : green; }`

    - 인접형제 선택자 : `+`로 구분, 바로 붙어있는 형제 요소

      `section + p { color : orange; }`

- 적용 순위

  1. `!important`
  2. inline style 적용
  3. id 선택자
  4. class 선택자
  5. 요소 선택자
  6. 코드 순서

- CSS 상속

  - 상속 되는 것 : text 관련 요소(font, color, text-align), opacity, visiblity
  - 상속 되지 않는 것 : box model 관련요소(width, height, padding, margin, border), position 관련(top, right, bottom, right, left,..)

- CSS 단위

  - px
  - % (기준 되는 사이즈에서의 배율)
  - em(상속받는 사이즈에서의 배율) / rem(root size의 배율)
  - vh, vw(화면 사이즈에서의 배율 )
  - 색상 표현 단위
    - HEX(#000, #000000)
    - RGB / RGBA
    - 색상명
    - HSL(명도, 채도, 색조, ...)

- Box model
  - margin : 바깥 여백
  - border : 테두리 영역
  - padding : 내부 여백
  - content : 글이나 이미지 요소
- box-sizing 
  - content-box : 기본값, width의 너비는 content 영역을 기준으로 잡는다.
  - border-box : width의 너비를 테두리를 기준으로 잡는다.
- 마진상쇄
  - 수직간의 형제요소에서 주로 발생.
  - 큰 사이즈의 마진을 조정해준다.
  - padding을 이용한다.
- Display
  - block : 가로폭 전체를 차지
    - div, ul, ol, p, hr, form, ...
    - 수평정렬 margin auto 사용
  - inline
    - 컨텐트의 너비 만큼 가로폭을 차지
    - width, height, margin-top, margin-bottom 지정할 수 없다.
      - line-height 로 위아래 간격 조정.
  - inline-block
  - none : 화면에서 완전히 없애 버림.
    - visbility : hidden (보여주지만 않을 뿐 그곳에 자리잡고 있다.)





