# error handling => hata yönetimi

# try:
#    x = int(input('x: '))
#    y = int(input('y: '))
#    print(x/y)
# except ZeroDivisionError:
#     print("y için 0 girilemez")
# except ValueError:
#     print("x ve y için sayısal değer giriniz")


# try:
#    x = int(input('x: '))
#    y = int(input('y: '))
#    print(x/y)
# except (ZeroDivisionError,ValueError) as e:
#     print("yanlış bilgi girdiniz")
#     print(e)

while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except Exception as exc:
        print("yanlış bilgi girdiniz", exc)
    else:
        break
    finally:
        print("try except sonlandı")
