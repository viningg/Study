# 1330. 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

# map 함수로 A랑 B 압력 받기
A,B = map(int,input().split())

# A가 B보다 큰 경우에는 '>'를 출력한다.
if (A > B):
    print(">")
# A가 B보다 작은 경우에는 '<'를 출력한다.
elif (A < B):
    print("<")
# A와 B가 같은 경우에는 '=='를 출력한다.
else:
    print("==")
