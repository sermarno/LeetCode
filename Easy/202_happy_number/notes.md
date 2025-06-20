# CONCEPTS COVERED

SET()


# SET()
- Unordered collection of unique elements
- Does not allow duplicates
- Mutable: can add or remove elements
- Like a math set: {a, b, c}

    🦋 Removing duplicates from a list
    names = ['Alice', 'Henry', 'John, 'Henry']
    unique_names = list(set(names))
    print(unique_names) 👉 ['Alice', 'Henry', 'John']

    🦋 Checking for duplicates
    nums = [1, 2, 3, 4, 1]
    seen = set()
    👉 for each value in the list (1, 2, 3, 4, 1)
    for num in nums:
        👉 condition before adding to seen set
        if num in seen:
            print('Duplicate found:", num)
        else: 
            seen.add(num)
    👉 Iteration 1:
    num = 1     |   seen = {}       |     seen = {1}
    👉 Iteration 2:
    num = 2     |   seen = {1}      |     seen = {1, 2}
    👉 Iteration 3:
    num = 1     |   seen = {1, 2}   |     seen = {1, 2} 👉 Duplicate doesn't get added
    
    