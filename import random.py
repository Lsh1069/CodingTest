import random

a = random.randint(1,100)
n = 0
print("컴퓨터의 렘덤 숫자를 알아 맞혀보세요.(1~100 사이)") #print("") 수정
q = 0 #추가
while a != q:
    q = int(input("1~100 숫자 입력:")) #int( input("") ) 수정
    if q < a:
        print("up")
    elif a < q:
        print("down")
    n += 1
print("정답입니다.")
print("걸린 순서: "+str(n)) # n -> str(n) 수정