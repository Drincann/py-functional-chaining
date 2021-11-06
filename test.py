from funcChaining import Type

ls = Type.List(range(1, 11)).filter(lambda num: num % 2 == 0)

print(ls)
