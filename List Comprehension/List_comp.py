print("List comprehension")
print("1. Append list")
print("2. Delete list")
print("3. Length of list")
print("4. Timing comparision")

Dolist = int(input("Enter the number to play with list : "))


temp = int(input("Please enter the number to have square of it: "))
Dolist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Dolist2 = [temp for temp in Dolist if temp % 2 == 0]
print(Dolist2)
