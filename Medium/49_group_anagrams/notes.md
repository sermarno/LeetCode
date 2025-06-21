# Concepts Covered

- Anagrams
- sorted()
- Dictionary
- list() With .values()

### Key:
- ❣️ Inner Concept
- 🦋 Example
- 👉 Comment
- ✅ Output

## Anagrams
- Two strings are anagrams if 1. they have the same length and 2. if they contain exactly the same chars with same freq.
    🦋 Sort both strings
    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
