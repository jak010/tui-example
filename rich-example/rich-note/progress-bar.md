
## Rich ProgressBar Summary
```python
from rich.progress import Progress

# Progress 객체에 파라미터로 집어넣는 순서는 ProgressBar 표시 순서에 연관
job_progress = Progress(
    "{task.description}",
    SpinnerColumn(),
    BarColumn(),
    "{task.percentage:<2.2f}%",
)
```
- `Rich`에서 `상태 바`를 표현하는 방법의 예시는 위와 같다
  - 여기서 `상태 바`는 `htop`으로 실행시킨 CPU 사용률 표시해주는 `가로 막대 그래프`와 같은 의미를 나타낸다.

- **Source Comment**
  - 위의 소스 코드에서 표현된 파라미터는 다음과 같은 의미를 지닌다
    - `{task.description}` : 나타낼 상태바의 제목을 표현
    - `SpinnerColumn()` : rich에서 진행 표시를 `SpinnerColumn()`로 정의. 
      - SpinnerColumn() 외에도 다른 효과는 Document를 참고
    - `BarColumn()` : 상태바의 진행 상태 라인을 표시
    - `"{task.percentage:<2.2f}%"` : 진행 상태의 percentage를 어떤 식으로 표현해줄지 정의한다 
      - `2.2f` 와 같이 표시된 부분은 `소수점 2자리`까지 표시를 해주는 의미

#### Task 추가하기
```python
job_progress.add_task("[green]CPU Usage")
```
- `Progress()` 객체의 `add_task()` 메서드를 호출함으로 작업 상태바를 표시

```python
for idx in range(1,100):
  job_progress.update(task_id=0, advance=float(cpu))
```
- 위의 코드는 `ProgressBar`가 나타내는 `현재 값`을 바꿔준다