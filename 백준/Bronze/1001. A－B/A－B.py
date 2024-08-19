A, B = input().split()
print(int(A)-int(B))

#해당 코드를

A,B = map(int,input().split())
print(A-B)

#이렇게도 바꿀 수 있는데
#map(function, iterable) 함수는 iterable의 각 요소에 function을 적용하여 새로운 iterable을 만들어준다.
