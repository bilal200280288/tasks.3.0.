age=int(input("Введите возраст: "))
if age%2 ==0:
    for i in range(0,age+1):
        if i %2 ==0:
            print(i)
elif age%2 == 1:
    for b in range(0, age+1):
        if b % 2 !=0:
            print(b)