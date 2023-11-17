print("Bài toán tìm số lớn nhất và nhỏ nhất.")
a=eval(input("Nhập số a:"))
b=eval(input("Nhập số b:"))
c=eval(input("Nhập số c:"))
d=eval(input("Nhập số d:"))
e=0
f=0
while(e<a)or(e<b)or(e<c)or(e<d):
    e+=1
f=e
while(f>a)or(f>b)or(f>c)or(f>c):
    f-=1
print("max =",e)
print("min =",f)       