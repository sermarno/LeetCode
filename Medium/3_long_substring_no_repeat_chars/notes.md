# CONCEPTS COVERED

- CHOOSING THE RIGHT DATA STRUCTURES
- SET()
- RANGE()
- LEN()
- .ADD()
- .REMOVE()
- COUNTER
- WHILE LOOP
- ARRAY
- SLIDING WINDOW


# FIGURING OUT DATA STRUCTURE FOR PROBLEMS
5-Step Guide to Choosing the Right Tools:

1. What is the input and output?
    - tells you data type you'll be working with
        🦋 Ex. "Given a list of numbers and a target..."
        - input is a list, probably loop through it

2. Do I need to remember past values or check for something that already happend?
    - Use a dictionary (hash map)
        🦋 Ex. "Return indices of two numbers that add up to target."
        - Need to remember what I've seen: use dictionary to store previous values

3. Am I filtering or counting?
    - Use loop with conditionals, or dictionary/counter.
        🦋 Ex. "Count how many times a letter appears."
        - Use for loop + dict or collections.Counter

4. Do I need to return or track multiple things at once?
    - Might need a list of tuples, two pointers, or dict of lists.
        🦋 Ex. "Ground of strings that are anagrams."
        - Need a dictionary where key is sorted version of string, and value is a list of matching words.

5. Does order matter? Do I need to sort or compare elements?
    - tells you whether you need indexes, or need to use a loop with range(), or sort beforehand.

# For This Problem
    # step 1: what is input/output?
        # input: string ( s = "ardhhgit")
        # output: integer representing length of longest substring, no dups

    # step 2: what are check tracking/checking?
        # keep track of characters seen
        # need to slide through string and track chars inside curr window
        ❣️ sliding window technique = using tow pointers (start and end) to define
        # the window of a subset of elements

    # step 3: do we need to look back at prev chars?
        # yes, if char is already in substring (to avoid dups),
        # where you last saw it (to know where to move window to avoid repeats)

    # step 4: what tools to track unique values quickly?
        # set -> stores chars in curr substring and check for dups
        # dict -> to store char positions for faster lookup 
        # two pointers -> to track start and end of substring window


# SET()

- unordered collection of unique elements (box of things where no dups allowed)

    🦋 Printing out each word in list
    my_set = set()
    my_set.add("apple")
    my_set.add("banana")
    my_set.add("apple")

    print(my_set) ✅ Output: {"apple", "banana"}
    ❣️ len(my_set) = tells how many unique items are in a set

    🦋 Find all unique letters in a word
    word = "hello"
    unique_letters = set(word)
    print(unique_letters) ✅ Output: {'h', 'e', 'l', 'o'}

    🦋 Finding unique characters in a string
    def is_unique(s):
        seen = set()
        for char in s:
            if char in seen:
                return False
            seen.add(char)
        return True

    is_unique("apple") ✅ Output: False

    🦋 Finding length of longest substring with no repeating chars
    def longest_start_unique(s):
        seen = set()
        count = 0
        for char in s:
            if char in seen:
                break
            seen.add(char)
            count += 1
        return count 

    longest_start_unique("abcabcbb") ✅ Output: 3

