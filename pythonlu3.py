# 1zad lu3- max stojnost
n=int(input('n= '))
max_num=0
while n:
#for i in range(1,n+1):
    num=int(input('enter number: '))
    if max_num<num:
        max_num=num
    n-=1
print()
print(max_num)
