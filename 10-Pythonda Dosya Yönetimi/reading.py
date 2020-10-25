# try:
#     file = open("newfile.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("dosya okuma hatası")
# finally:
#     print("dosya kapandı")
#     file.close()


file = open("newfile.txt","r",encoding="utf-8")

# for i in file:
#     print(i,end="")

# ************* READ() FONKSİYONU ********************

# content1 = file.read()

# print("içerik 1")
# print(content1)

# content2 = file.read()

# print("içerik 2")
# print(content2)

# content = file.read(5)
# content = file.read(3)
# content = file.read(3)

# print(content)

# ************* READLINE() FONKSİYONU ********************

# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")

# ************* READLINE() FONKSİYONU ********************

liste = file.readlines()

print(liste)
print(liste[0])
print(liste[1])
print(liste[2])


file.close()


