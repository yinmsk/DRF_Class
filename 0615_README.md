# DRF_Class

 1. args, kwargs를 사용하는 예제 코드 짜보기
 3. mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기
 4. DB Field에서 사용되는 Key 종류와 특징 서술하기
 5. django에서 queryset과 object는 어떻게 다른지 서술하기
<br/>
## args를 사용하는 예제 코드 짜보기
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
## kwargs를 사용하는 예제 코드 짜보기
```python3

```


## mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기
## DB Field에서 사용되는 Key 종류와 특징 서술하기
## django에서 queryset과 object는 어떻게 다른지 서술하기
