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
<br/>

## kwargs 뜻
	keyword = 특정값의 형태로 함수 안에 작성
	kwargs는 dictionary의 형태로 전달됨

```python3
def name_age(**kwargs):
	print(kwargs)
    
name_age(name="홍길동", age="100")

### 출력값 ###
{'name': '홍길동', 'age': '100'}
```
<br/>

## mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기
`*주소`

### mutable
`mutable`은 값이 변할 수 있다. - 데이터만 바뀐다
예시) int, float string, tuple 
예를들어 데이터를 변경하려 한다면 원래 사용하던 데이터 주소안에 데이터를 넣을 수 있다.
<br/>

### immutable
`immutable`은 값이 변할 수 없다. - 주소 데이터 다 바꾸어야함
예시) list, dictionar
예를들면 데이터를 변경하려 한다면 이전 데이터 주소 지우고 새로운 주소를 만들고 데이터를 넣어주어야 한다.
<br/>

## DB Field에서 사용되는 Key 종류와 특징 서술하기
- FK : Foreign Key의 약자이며, 다른 테이블을 참조 할 때 사용된다.
- UK : Unique Key의 약자이며, 중복 값을 허용하지 않는다.
- PK : Primary Key의 약자이며, 테이블에서 반드시 한개 존재해야 한다.
<br/>


## django에서 queryset과 object는 어떻게 다른지 서술하기
