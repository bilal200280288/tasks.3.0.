smooth = input("Напишите строку любого формата: ")
list_1=list(smooth.strip())
if list_1[::1]==list_1:
    print("Это Полидром")
else:
    print("Не полидром")