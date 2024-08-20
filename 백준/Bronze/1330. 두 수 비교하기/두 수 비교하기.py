a, b = map(int,input().split())
if a>b:
    print(">")
elif a<b:
    print("<")
elif a==b:
    print("==")

#if : 조건문을 시작하는 첫 번째 조건. if 뒤에 오는 조건이 참일 경우, 
    해당 블록의 코드를 실행 (print(">")
#elif (=else if) : 앞선 if조건이 거짓일 때 다른 조건을 검사. 여러 개의 조건을 순차적으로 검사.

#a==b
#==는 비교 연산자로, 두 값이 같은지를 검사한다.
