with open("newfile.txt","r",encoding="utf-8") as file:
    content = file.read(10)
    print(content)
    file.seek(0) #cursor konumu nereye gitsin
    print(file.tell()) #cursor konumu nerede
    content2 = file.read(10)
    print(content2)


