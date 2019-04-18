squares = []
for value in range(1, 11):
    #square = value**2
    #squares.append(square)
    squares.append(value**2)

print("The list named squares is:")
print(squares)

squares2 = [i**2 for i in range(1, 11)]
print("The list named squares2 is:")
print(squares2)
