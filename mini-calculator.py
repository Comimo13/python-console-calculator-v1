def choice():
    a = int(input("1-son: "))
    b = int(input("2-son: "))
    return a, b
def plus(x, y): #Plyus qilish
    return x + y
def minus(x, y): #Minus qilish
    return x - y
def multiply(x, y): #Ko'paytirish
    return x * y
def divide(x, y): #Bo'lish
    return x / y
def power(x , y): #Daraja topish
    return x ** y
def floor_divide(x, y): #Qoldiqsiz bo'lish
    return x // y
def main():
    running = True
    while running:
        try:
            try:
                action = int(input("1.Plyus\n2.Minus\n3.Ko'paytirish\n4.Bo'lish\n5.Qoldiqsiz Bo'lish\n6.Sonni darajasini topish\n7.Chiqish\nNima qilamiz:"))
            except ValueError: #Xato inputdan himoya
                print("Xato! Qayta urunib ko'ring")
                continue
            if action == 1: #Plyus qilish
                    a , b = choice()
                    result = plus(a, b)
                    print("Javob:",result)

            elif action == 2: #Minus qilish
                    a , b = choice()
                    result = minus(a, b)
                    print("Javob:",result)

            elif action == 3: #Ko'paytirish
                    a , b = choice()
                    result = multiply(a, b)
                    print("Javob:",result)

            elif action == 4: #Bo'lish
                try:
                    a , b = choice()
                    result = divide(a, b)
                    print("Javob:",result)
                except ZeroDivisionError:
                    print("Xato! Qayta urunib ko'ring")

            elif action == 5: #Qoldiqsiz bo'lish
                    a, b = choice()
                    result = floor_divide(a, b)
                    print("Javob:",result)

            elif action == 6: #Daraja topish
                    a , b = choice()
                    result = power(a, b)
                    print("Javob:",result)

            elif action == 7: #Chiqish
                running = False

        except ValueError:
            print("Xato! Qayta urunib ko'ring")
main()

