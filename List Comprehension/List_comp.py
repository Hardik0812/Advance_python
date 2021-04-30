print("List comprehension")
print("1. Append list")
print("2. Delete list")
print("3. Square of list")
print("4. Nested if statement")
print("5. Matrix list")


Dolist = int(input("Enter the number to play with list : "))

if Dolist == 1:
    temp = int(input("Please enter the number to add to list: "))
    Dolist1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    Dolist2 = [x for x in Dolist1 if temp == x]
    print(Dolist2)
elif Dolist == 2:
    temp = int(input("Please enter the number to delete from list: "))
    Dolist1 = range(100)
    Dolist2 = [x for x in Dolist1 if x != temp]
    print(Dolist2)
elif Dolist == 3:
    temp = int(input("Please enter the number to find the square of  list: "))
    Dolist1 = [x for x in range(100) if x % temp == 0]
    print(Dolist1)
elif Dolist == 4:
    Dolist1 = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
    print(Dolist1)
elif Dolist == 5:
    matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
    transpose = [[row[i] for row in matrix] for i in range(2)]
    print(transpose)
