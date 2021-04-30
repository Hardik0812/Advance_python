print("Dict comprehension")
print("1. Append Dict")
print("2. Delete Dict")
print("3. Square of Dict")
print("4. Nested if statement")
print("5. Matrix Dict")

Dict = int(input("Enter the number to play with list : "))
# dictionary comprehension example
# dictionary = {key: value for vars in iterable}
if Dict == 3:
    square_dict = {num: num*num for num in range(1, 11)}
    print(square_dict)
