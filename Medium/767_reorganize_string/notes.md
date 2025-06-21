# Concepts Covered

- Counter()
- .values()
- Worst-Case Spacing Between Characters Formula
- .items()
- sorted()
- key= With sorted()
- lambda
- Greedy Algorithm (Strategy)

## Counter()
- Creates a special dict where:
    - Keys are items counted (e.g. chars, nums, etc.)
    - Values are how many times each item apears
    ❣️ Best for counting dups, freqencies, histograms

## .values()
- Used on dictionaries to see all values without the keys
    🦋 Accessing values in dict
    fruit_counts = {
        'apple': 3,
        'banana': 5,
        'orange': 2
    }

    for count in fruit_count.values():
        print(count)
        ✅ Output: 3
                   5
                   2

## Worst-Casing Spacing Between Characters Formula
- How many times can one char appear without forcing it to be adjacent to itself?
    🦋 String "aaab"
    - Avoid "aa" sitting next to each other
    - Place most frequent letters in every other spot
    - Length of string is n
    - Max num of non-adjacent positions:
        - (n + 1) // 2

## .items()
- Dictionary method that returns a view object, which displays a list of dictionary's key-value pairs as tuples
    🦋 General syntax
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    for key, value in my_dict.items():
        print(key, value) 
        ✅ Output: a 1
                   b 2
                   c 3
- Lets you acces both character (key) and frequency (value)
    🦋 In this problem
    s = "aabbc"

    from collections import Counter
    count = Counter(s)
    👉 count = {'a': 2, 'b': 2, 'c': 1}

    count.items() 👉 dict_items([('a', 2), ('b', 2), ('c', 1)])
    ┌──────────┬───────┐
    │  Letter  │ Count │ 👉 Each row is represented as a tuple
    ├──────────┼───────┤
    │    a     │   2   │ 👉 ('a', 2)
    │    b     │   2   │ 👉 ('b', 2)
    │    c     │   1   │ 👉 ('c', 1)
    └──────────┴───────┘


## sorted()
- Takes an iterable (e.g. list, tuple, string, dict keys) and returns a new sorted list, but doesn't modify the original data
    🦋 Sorting list of numbers (lowest to highest)
    nums = [4, 1, 3, 2]
    sorted_nums = sorted(nums)
    print(sorted_nums) ✅ Output: [1, 2, 3, 4]

    🦋 Sorting Strings Alphabetically
    words = ['hot', 'cold', 'warm']
    print(sorted(words)) ✅ Output: ['cold', 'hot', 'warm']

## key= With sorted()
    🦋 Sorting with key= - For Custom Rules
    ❣️ key= lets you control how things are sorted
    words = ['apple', 'banana', 'kiwi']
    sort_by_len = sorted(words, key=len)
    print(sort_by_len) ✅ Output: ['kiwi', 'apple', 'banana']

    🦋 Sorting List of Tuples with key=
    items = [('a', 3), ('b', 5), ('c', 1)]
    sorted_items = sorted(items, key=lambda x: x[1]) 
    👉 lambda x: x[1] means sort by 2nd element in each tuple
    print(sorted_items) ✅ Output: [('c', 1), ('a', 3), ('b', 5)]

## Lambda
- A shorthad way to create small anonymous functions (functions without a name)
- Like writing a simple one-line function without using def

## Greedy Algorithm (Strategy)
- Solves a problem by making the locally optimal choice at each step with hopes that it leads to a globally optimal solution.

    🦋 Activity Selection Problem
    - Given start and end times, find max num of activities that don't overlap.

    def max_activities(start, end):
        activities = sorted(zip(start, end), key=lambda x: x[1])
        count = 1
        last_end = activities[0][1]

        for i in range(1, len(activities)):
            if activities[i][0] >= last_end:
                count += 1
                last_end = activities[i][1]

        return count