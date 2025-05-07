## 📘 Python 문법 정리

### 1. `ord()` 함수

- `ord()` 함수는 **문자 하나를 유니코드 정수로 변환**해주는 내장 함수이다.  
이를 통해 알파벳 문자가 몇 번째인지 계산할 수 있다.

#### ✅ 예시
```python
ord('a')  # 결과: 97
ord('b')  # 결과: 98
ord('c')  # 결과: 99
...
ord('z')  # 결과: 122
```

---

### 2. 리스트 컴프리헨션 (List Comprehension)

- 리스트 컴프리헨션은 **반복문을 간결하게 하나의 줄로 작성할 수 있는 문법**이다.  
기존의 `for` 반복문보다 짧고 직관적으로 리스트를 생성할 수 있다.

#### ✅ 기본 문법
```python
[표현식 for 변수 in 반복가능한_객체]
```
#### ✅ 예시 1: 0부터 4까지의 숫자를 담은 리스트 만들기
```python
numbers = [x for x in range(5)]
print(numbers)  # 출력: [0, 1, 2, 3, 4]
```
#### ✅ 예시 2: 값 변형하기
```python
squares = [x**2 for x in range(5)]
print(squares)  # 출력: [0, 1, 4, 9, 16]
```

---

### 3. 슬라이싱 (`:` & `::` 문법)

- 파이썬의 슬라이싱은 `리스트[start:stop:step]` 형태로 사용되며, 원하는 범위나 간격으로 리스트를 추출할 수 있는 문법이다.

#### ✅ 기본 문법
```python
list[start:stop:step]
```
- `start`: 시작 인덱스 (포함)
- `stop`: 끝 인덱스 (포함하지 않음)
- `step`: 간격 (기본값은 1)

#### ✅ 예시

```python
arr = [0, 1, 2, 3, 4, 5, 6]

arr[1:5]      # [1, 2, 3, 4]
arr[::2]      # [0, 2, 4, 6] → 처음부터 끝까지, 두 칸씩 건너뛰며
arr[1::2]     # [1, 3, 5]    → 1부터 끝까지, 두 칸씩
arr[::-1]     # [6, 5, 4, 3, 2, 1, 0] → 리스트를 역순으로
```

- `::`만 쓰는 경우는 `list[::step]` 형태로, 전체 리스트를 일정 간격으로 추출하거나 역순으로 뒤집을 때 자주 사용된다.

---

### 4. `deque` (덱)

- `deque`는 **double-ended queue**의 줄임말로, **양쪽 끝에서 빠르게 삽입과 삭제가 가능한 자료구조**이다.
- `collections` 모듈에서 불러와 사용하며, **리스트보다 큐나 스택 구현에 더 적합**하다.

#### ✅ 예시
```python
from collections import deque

dq = deque([1, 2, 3])

dq.append(4)       # 오른쪽에 삽입 → deque([1, 2, 3, 4])
dq.appendleft(0)   # 왼쪽에 삽입 → deque([0, 1, 2, 3, 4])

dq.pop()           # 오른쪽에서 삭제 → 4
dq.popleft()       # 왼쪽에서 삭제 → 0

print(dq)          # deque([1, 2, 3])
```

- 큐처럼 사용하려면 `append()` + `popleft()`  
- 스택처럼 사용하려면 `append()` + `pop()`  

> 리스트로 구현하면 앞쪽 데이터를 제거할 때 시간이 오래 걸리지만,  
> `deque`는 앞뒤 모두 **O(1)** 시간 복잡도로 처리 가능해서 효율적이다.

---

### 5. `for i in range(n):` vs `for _ in range(n):`

- 파이썬에서 `for`문을 쓸 때, 반복 횟수만 중요하고 **반복 변수 자체가 필요 없는 경우**,  
  관례적으로 `_`(언더스코어)를 사용한다.

#### ✅ 예시 1: 반복 변수를 사용할 때
```python
for i in range(5):
    print(i)
# 출력: 0 1 2 3 4
```

#### ✅ 예시 2: 반복 변수 안 쓸 때 (언더스코어 사용)
```python
for _ in range(5):
    print("Hello")
# 출력:
# Hello
# Hello
# Hello
# Hello
# Hello
```

> 언더스코어 `_`는 "나는 이 변수를 사용하지 않겠다"는 의미로, **가독성 향상**에 도움을 준다.

---

### 6. `sep`과 `end` 파라미터

- `print()` 함수에서 여러 값을 출력할 때, 사이사이에 들어갈 문자나 끝맺음 문자를 설정할 수 있다.

#### ✅ sep: 여러 값 사이에 들어가는 문자열
```python
print("2025", "04", "16", sep="-")
# 출력: 2025-04-16
```

#### ✅ end: 출력 끝에 들어가는 문자열 (기본은 줄바꿈)
```python
print("Hello", end=" ")
print("World")
# 출력: Hello World
```

---

### 7. `key=` 옵션 (정렬 기준 지정)

- `sorted()`나 `sort()` 함수에서 **정렬 기준을 직접 정해주는 방법**이다.
- 리스트 요소 하나하나에 함수를 적용해서, **그 리턴값을 기준으로 정렬**한다.

#### ✅ 왜 필요할까?

| 개념       | 설명 |
|----------|------|
| `key=함수` | 정렬 기준을 직접 정해주는 방법. 리스트 요소 하나하나에 함수를 적용해서, 그 리턴값을 기준으로 정렬 |
| Why?     | 그냥 `sorted()` 쓰면 전체 요소로 비교해서 제대로 안 될 수 있음. 원하는 부분만 기준으로 삼고 싶을 때 `key` 사용 |

#### ✅ 예시: 문자열 길이 기준으로 정렬
```python
words = ["banana", "pie", "apple"]
sorted_words = sorted(words, key=len)
print(sorted_words)
# 출력: ['pie', 'apple', 'banana']
```

#### ✅ 예시: lamda 사용
```python
array = [('바나나', 2), ('사과', 5), ('당근', 3)]
result = sorted(array, key=lambda x: x[1])
print(result)
# 출력: [('바나나', 2), ('당근', 3), ('사과', 5)]
```

---

### 8. `set()` – 집합 자료형

- `set()`은 **중복을 자동으로 제거**하고, **순서가 없는 자료형**이다.
- 리스트나 문자열 등을 넣으면, **중복 없이 유일한 값들만 저장**된다.

#### ✅ 기본 사용법
```python
nums = [1, 2, 2, 3, 4, 4]
unique = set(nums)
print(unique)  # 출력: {1, 2, 3, 4}
```

#### ✅ 주요 특징
- 순서가 없어서 인덱싱 불가능 (`set[0]` 같은 거 안 됨)
- 중복 제거에 매우 유용
- `in` 연산으로 포함 여부 빠르게 확인 가능

#### ✅ 집합 연산 (교집합, 합집합, 차집합 등)
```python
a = set([1, 2, 3])
b = set([2, 3, 4])

print(a & b)  # 교집합: {2, 3}
print(a | b)  # 합집합: {1, 2, 3, 4}
print(a - b)  # 차집합: {1}
```

---

### 9. `isalpha()` & `isdigit()` – 문자열 검사 메서드

- 문자열이 **전부 알파벳인지**, 또는 **전부 숫자인지** 확인할 때 사용한다.

#### ✅ `isalpha()`: 전부 알파벳이면 `True`
```python
s = "hello"
print(s.isalpha())  # 출력: True

s2 = "hello123"
print(s2.isalpha())  # 출력: False
```

#### ✅ `isdigit()`: 전부 숫자면 `True`
```python
n = "12345"
print(n.isdigit())  # 출력: True

n2 = "123a"
print(n2.isdigit())  # 출력: False
```

> 문자열이 비어 있거나, 공백이 섞여 있으면 둘 다 `False` 나옵니다!

---

### 10. `combinations()` & `combinations_with_replacement()` – 조합 만들기

- `itertools` 모듈에 있는 함수로, **리스트에서 특정 개수만큼 원소를 뽑는 조합**을 만들어준다.

#### ✅ `combinations(iterable, r)`
- **중복 없이**, 순서 상관 없이 r개를 뽑는 모든 조합을 반환

```python
from itertools import combinations

items = ['a', 'b', 'c']
result = list(combinations(items, 2))
print(result)  # 출력: [('a', 'b'), ('a', 'c'), ('b', 'c')]
```

#### ✅ `combinations_with_replacement(iterable, r)`
- **중복을 허용해서**, r개를 뽑는 모든 조합을 반환

```python
from itertools import combinations_with_replacement

items = ['a', 'b', 'c']
result = list(combinations_with_replacement(items, 2))
print(result)  # 출력: [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')]
```

> 두 함수 모두 반환값은 **튜플의 리스트** 형태

---

### 11. `copy()` vs `deepcopy()` – 얕은 복사 vs 깊은 복사

- 리스트나 딕셔너리처럼 **참조형 자료**를 복사할 때, 단순 대입은 같은 메모리를 공유하기 때문에 문제가 생길 수 있다.  
- 이럴 때 `copy()` 또는 `deepcopy()`를 사용해 복사한다.

#### ✅ `copy()` – 얕은 복사 (shallow copy)
- **바깥쪽 객체만 새로 만들고**, 그 안의 **내부 객체는 같은 걸 참조**

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)
b[0][0] = 99

print(a)  # 출력: [[99, 2], [3, 4]]
print(b)  # 출력: [[99, 2], [3, 4]]
```

#### ✅ `deepcopy()` – 깊은 복사 (deep copy)
- **바깥쪽 객체는 물론 내부 객체까지 전부 새로 복사**

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0][0] = 99

print(a)  # 출력: [[1, 2], [3, 4]]
print(b)  # 출력: [[99, 2], [3, 4]]
```

> `copy()`는 껍데기만 복사,  
> `deepcopy()`는 속까지 전부 복사!


