# Concepts Covered

- DICTIONARY
- FOR LOOP
- BOOLEAN

### Key:
- ❣️ Inner Concept
- 🦋 Example
- 👉 Comment
- ✅ Output

## DICTIONARY
- Collection of key-value pairs, where:
    - Keys: unique identifiers (e.g. 'name')
    - Values: corresponding data (e.g. 'Serra')

    🦋 Iterating through Keys
    person = {
        'name': 'Serra',
        'age': 23,
        'is_student': False
    }
    for key in person:
        print(key) 
        ✅ Output: name
                   age
                   is_student

    🦋 Iterating through Values
    for val in person.values():
        print(val)
        ✅ Output: Serra
                   23
                   False