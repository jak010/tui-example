## rich Summary
- 해당 예제는 저장소의 `rich-example`에서 코드를 확인할 수 있습니다.
- 문서를 최대한 간결하게 쓰기 위해 코드를 전부 기재하지는 않고 필요한 사항만 적도록 하겠습니다

### Layout
- Source : 001-rich-Layout-Example.py
   - Terminal에서 layout을 잡는 예제입니다
   - 다음 모듈을 import 합니다
    ```python
    from rich.layout import Layout
    ```
  - Layout() 객체로 초기화합니다. 
  - `layout.sploit()`은 화면을 어떻게 나눌지를 정의합니다
    - 관련 소스 코드에서는 upper와 lower로 `header`와 `footer`의 개념으로 나눠습니다.
