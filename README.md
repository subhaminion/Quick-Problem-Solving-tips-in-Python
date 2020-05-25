## Quick tips for problem solving

#### Formning keys for array of string and numbers
suppose you want to form keys for each element in array of string or numbers like example below:

```python
arr = [1,2,3,4,5]
dictionary = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0
}
string = "subham"
dictionary = {
    's': 0,
    'u': 0,
    'b': 0,
    'h': 0,
    'a': 0,
    'm': 0
}
```
what we can do to achive above is `dict.formkeys(arr/string, value)`
```python
arr = [1,2,3,4,5]
hash_table = {}
hash_table = hash_table.formkeys(arr, 0)
print(hash_table)

#Output
dictionary = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0
}

string_hash_table = {}
string_hash_table = string_hash_table.formkeys(arr, 0)
print(string_hash_table)
string = "subham"
dictionary = {
    's': 0,
    'u': 0,
    'b': 0,
    'h': 0,
    'a': 0,
    'm': 0
}
```

#### Splitting numbers one by one mathematicly
there are situations where we may want to split a number one by one to run some caculations in each numbers like from `123` to `1`, `2`, `3`

```python
number = 1234
first_split = number // 10
print(first_split)

#Output
# 123

second_split = first_split // 10
print(second_split)

#Output
# 12

third_split = second_split // 10
print(third_split)

#Output
# 1
```

#### spongebob_mocking.py
#### A Python Script to Generate SpongeBob Mocking Texts


```python

#Input:  "I love Python"
#Output: "I lOvE pYtHoN"

```
