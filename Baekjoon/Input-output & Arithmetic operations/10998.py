#10998. 두 정수 A와 B를 입력받은 다음, A×B를 출력하는 프로그램을 작성하시오.

# A,B 한 가지 이상을 입력 받을떄는 map 함수를 사용, 입력 받을 타입을 명시해준다.
# split() 을 이용하여 띄어쓰기를 기준으로 입력 받을 A와 B를 구분한다.
A,B = map(int,input().split())

print(A*B)