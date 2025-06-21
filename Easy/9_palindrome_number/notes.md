# Concepts Covered

- Palindrom
- str()
- String Slicing

### Key:
- ❣️ Inner Concept
- 🦋 Example
- 👉 Comment
- ✅ Output

## Palindrome
- A word, number, phrase, or sequence that reads the same forwards and backwards.

    🦋 Examples
    Words:
        - "madam" -> same backwards: "madam"
        - "level" ...
    Numbers:
        - 121 -> same backwards: 121

    ❣️ If s is a string:
        s == s[::-1] 👉 Checks if s is a palindrome

## str()
- Converts value into a string, no matter the data type

    🦋 Using str() to concatenate
    age = 25
    print("I am " + str(age) + " years old.")
    ✅ Output: I am 25 years old.

## String Slicing
- Allows you to access a subset (slice) or a string:
    - string[start:end:step]
    👉 start: index where slice starts (inclusive)
    👉 end: index where slice ends (exclusive)
    👉 step: how many chars to skip (default = 1)

    🦋 Slicing a string in different ways
    text = "Hello, world!"
    text[0:5] ✅ Output: 'Hello'
    text[7:12] ✅ Output: 'world'
    text[:5] ✅ Output: 'Hello'
    text[7:] ✅ Output: 'world!'
    text[:] ✅ Output: 'Hello, world!" 👉 Full string
    text[::2] ✅ Output: 'Hlo ol!" 👉 Skips every other char
    text[::-1] ✅ Output: '!dlrow ,olleH" 👉 Reverses string