ma_variable = 55

a = 123
b = a  # passage par référence


a = 12

print("a : ", a)
print("b : ", b)


print("id de a: ", id(a))
print("id de b: ", id(b))
