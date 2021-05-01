print("Dictionary comprehension")
print("1. Print Key and Value")
print("2. Finding Squares")
print("3. upper and Lower String")
print("4. Lamda and Map functions")
print("5. Nested If")

Dict = int(input("Enter the number to play with Dictionary : "))

if Dict == 1:
    # printing Keys and values
    keys = ['a', 'b', 'c', 'd', 'e']
    values = [1, 2, 3, 4, 5]
    Dict = {k: v for (k, v) in zip(keys, values)}
    print(Dict)
elif Dict == 2:
    # Finding Square
    myDict = {x: x**2 for x in [1, 2, 3, 4, 5]}
    print(myDict)
elif Dict == 3:
    4  # Upper String
    sDict = {x.upper(): x*3 for x in 'coding '}
    print(sDict)
    # Lower String
    sDict = {x.lower(): x*3 for x in 'CODING '}
    print(sDict)
elif Dict == 4:
    # Lamda and Map functions
    fahrenheit = {'t1': -30, 't2': -20, 't3': -10, 't4': 0}
    celsius = list(map(lambda x: (float(5)/9)*(x-32), fahrenheit.values()))
    celsius_dict = dict(zip(fahrenheit.keys(), celsius))
    print(celsius_dict)
elif Dict == 5:
    # Nested If
    dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    Nest = {k: v for (k, v) in dict1.items() if v > 2 if v % 2 == 0}
    print(Nest)
