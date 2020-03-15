"""
https://py.checkio.org/en/mission/all-the-same/

In this mission you should check if all elements in the given list are equal.

Input: List.

Output: Bool.

Example:

all_the_same([1, 1, 1]) == True
all_the_same([1, 2, 1]) == False
all_the_same(['a', 'a', 'a']) == True
all_the_same([]) == True

"""


from typing import List, Any


def all_the_same(n) -> bool:
    
    if (len(n) < 2):
        return True 
        
    for i in range(1, len(n)):
        if n[i] != n[i-1]:
            return False
    
    return True

# Points: 10

# Tests
if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True