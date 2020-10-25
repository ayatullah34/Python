# def cube():
 
#     for i in range(5):
#         yield i ** 3

# generator = cube()
# iterator = iter(generator)

# iterator = cube()

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# for i in iterator:
#     print(i)

# for i in cube():
#     print(i)

# liste = [i**3 for i in range(5)]
# print(liste)

generator = ( i**3 for i in range(5) )
print(generator)

# print(next(generator))
# print(next(generator))
# print(next(generator))

for i in generator:
    print(i)