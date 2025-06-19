# CONCEPTS COVERED

CLASS
DICTIONARY
FOR LOOP
ENUMERATE

# CLASS

✅ writing a solution to find two numbers that add up to a target
  by calling a method
+-------------------------------------+
|               Class                 |  ← Big circle/container (e.g., Solution)
|                                     |
|   +----------------------------+    |  
|   |       Method 1 (twoSum)    |    |  ← Algorithms or functions inside
|   +----------------------------+    |
|                                     |
|   +----------------------------+    |
|   |       Method 2 (other stuff) |   |
|   +----------------------------+    |
|                                     |
|   Variables/attributes (data)        |  ← Stored values related to the class
|                                     |
+-------------------------------------+

    ❣️ __init__ = setup method ran once per new object: gives object initial values (e.g. name, age, size, etc.)

    🦋 Ex. class Dog:
            def __init__(self, name, breed):
                self.name = name 👉 assigning name to object
                self.breed = breed 👉 assigning breed to object
        my_dog = Dog("Buddy", "Pitbull")
        print(my_dog.name) ✅ Output: Buddy 

    🦋 Ex. class Person:
            def __init__(self, name):
                self.name = name 
            def say_hello(self):
                print("Hello, my name is " + self.name + "!")

        p = Person("Serra"")
        p.say_hello() ✅ Output: Hello, my name is Serra! 

# DICTIONARY

❣️ key-value pairs that store a key (e.g. string, number, etc.)
  and a value (e.g. number, string, list, another dictionary, etc.)

    🦋 Counting characters in string
    sentence = "Hello"
    char_count = {}

    for char in sentence:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    print(char_count) ✅ Output: {'H': 1, 'e': 1, 'l': 2, 'o': 1} 

    🦋 Mapping keys to numeric values
    grades = {
        "Anna": 95,
        "Ben": 88,
        "Claire": 92
    }

    print(grades["Ben"]) ✅ Output: 88

    🦋 Inverting a dictiorary
    original = {
        "a": 1,
        "b": 2,
        "c": 3
    }

    ❣️ .items(): returns each key-value pair in dictionary as tuples
    
    inverted = {v: k for k, v in original.items()} 
    👉 for each k, v, create a new dictionary where the key is v and the value is k
        👉 original.items() == [('a', 1), ('b', 2), ('c', 3)]

    print(inverted) ✅ Output: {1: 'a', 2: 'b', 3: 'c'}

    🦋 Grouping keys by common value
    fruits = {
        'apple': 2,
        'banana': 2,
        'orange': 3,
        'grape': 1
    }

    grouped = {} 👉 empty dict to group by values

    for key, value in fruits.items():
        👉 fruits.items() == [('apple', 2), ('banana', 2), ...]
        if value in grouped:
            grouped[value].append(key)
        else:
            grouped[value] = [key]

    print(grouped) ✅ Output: {2: ['apple', 'banana'], 3: ['orange'], 1: ['grape']}

# FOR LOOP

❣️ used for iterating over a sequence (e.g. list, tuple, dictionary, set, or a string)

    🦋 Printing each item in list
    nuts = ['cashew', 'pistachio', 'almond']
    for x in nuts:
        print(x)
        nuts = ['cashew', 'pistachio', 'almond']
    for x in nuts:
        print(x) 
        ✅ Output: cashew
                   pistachio
                   almond

    🦋 Nested for loops: print all pairs
    colors = ['red', 'blue']
    shapes = ['circle', 'square']

    for color in colors:
        for shape in shapes:
            print(color, shape)
            ✅ Output: red circle
                       red square
                       blue circle
                       blue square

    🦋 Looping with enumerate()
    animals = ['dog', 'cat', 'rabbit']
    for i, animal in enumerate(animals):
        print(f"{i}: {animal}")
        ✅ Output: 0: dog
                   1: cat
                   2: rabit

    🦋 Looping with Conditions: print only even #s
    nums = [1, 2, 3, 7, 8, 10]
    for num in nums:
        if num % 2 == 0:
            print(num)
            ✅ Output: 2
                       8
                       10

    🦋 Modifying list in loop: create new list with squared numbers
    nums = [1, 2, 3, 4, 5]
    squares = []

    for num in nums:
        ❣️ .append(): add a single item to the end of a list
        squares.append(num ** 2)
    print(squares) ✅[1, 4, 9, 16, 25]