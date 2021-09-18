

vess=float(input("Введите ваш вес: "))
print("Ваш вес равен: ", vess)
for i in range(0,16):
    vess += i
    print(i+1, "год - ", "%.2f" % (vess*0.165))

