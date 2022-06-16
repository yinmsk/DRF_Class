# DRF_Class

0615 과제
 1. args, kwargs를 사용하는 예제 코드 짜보기
 3. mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기
 4. DB Field에서 사용되는 Key 종류와 특징 서술하기
 5. django에서 queryset과 object는 어떻게 다른지 서술하기
<br/>

## args 뜻
	복수의 인자를 함수로 받고자 할 때 사용
	args의 타입은 tuple
args를 사용하는 예제 코드 짜보기

예제 1
```python3
def age_list(*args):
 print(args)
 
age(10, 20, 30)

# 출력값 #
(10, 20, 30)
```

예제 2
```python3
def age_list(*args):
    result = 0
    for i in args:
        result += i
    print(result)
    
add(1, 10, 20)
add(10, 20, 30)
add(10)

# 출력값 #
31
60
10
```

## kwargs
	keyword = 특정값의 형태로 함수 안에 작성
	kwargs는 dictionary의 형태로 전달됨
kwargs를 사용하는 예제 코드 짜보기

```python3
def name_age(**kwargs):
	print(kwargs)
    
name_age(name="홍길동", age="100")

### 출력값 ###
{'name': '홍길동', 'age': '100'}
```

## mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기
mutable는 값이 변한다
immutable는 불변

## DB Field에서 사용되는 Key 종류와 특징 서술하기
- FK : Foreign Key의 약자이며, 다른 테이블을 참조 할 때 사용된다.
- UK : Unique Key의 약자이며, 중복 값을 허용하지 않는다.
- PK : Primary Key의 약자이며, 테이블에서 반드시 존재해야 한다.

## django에서 queryset과 object는 어떻게 다른지 서술하기
