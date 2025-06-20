# CONCEPTS COVERED

.SPLIT()
LEN()
NEGATIVE INDEXING

# .SPLIT()
- Breaks a string into a list of substrings based on a separator (default = whitespace)

    🦋 Splitting Words String
    s = "Hello world"
    print(s.split()) ✅ Output: ['Hello', 'world']

    🦋 Splitting by Custom Character
    s = 'roses,peonys,orchids"
    print(s.split(',')) ✅ Output: ['apple', 'banana', 'cherry']

    🦋 Max Split
    s = 'one two three four'
    print(s.split(" ", 2)) ✅ Output: ['one', 'two', 'three four']

# LEN()
- Returns the number of items in an object (list, string, tuple, etc.)

    🦋 String length
    s = "hello"
    print(len(s)) ✅ Output: 5

    🦋 List length
    my_list = [1, 2, 3, 4]
    print(len(my_list)) ✅ Output: 4

# NEGATIVE INDEXING
- Count indices backwards from the end

    🦋 Accessing last element in list
    letters = ['a', 'b', 'c', 'd', 'e']
    print(letters[-1]) ✅ Output: 'e'

