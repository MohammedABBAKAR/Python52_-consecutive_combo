
# todo Combined Consecutive Sequence
# ? Write a function that returns True if two arrays, when combined, form a consecutive sequence. 
# ? A consecutive sequence is a sequence without any 
# ? gaps in the integers, e.g. 1, 2, 3, 4, 5 is a consecutive sequence, but 1, 2, 4, 5 is not.

# * Examples
# * consecutive_combo([7, 4, 5, 1], [2, 3, 6]) ➞ True

# * consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) ➞ False

# * consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]) ➞ False

# * consecutive_combo([44, 46], [45]) ➞ True
# ! Notes
# ! The input lists will have unique values.
# ! The input lists can be in any order.



def consecutive_combo(lst1, lst2):
    lst1.extend(lst2)
    lst1.sort()
    nummax =max(lst1)
    nummin =min(lst1)
    newlst = [item for item in range(nummin,nummax+1)]
    if lst1 == newlst:
     return True
    else:
       return False
print(consecutive_combo([7, 4, 5, 1], [2, 3, 6]))
print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]))
print(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]))



# ! ////////////////////////////////////////////////////////////////

def consecutive_combo(lst1, lst2):

    lst1.extend(lst2)
    
    
    lst1.sort()
    
    # Create a new list with the expected consecutive numbers
    newlst = list(range(min(lst1), max(lst1) + 1))
    
    # Check if the sorted list matches the consecutive list
    return lst1 == newlst


print(consecutive_combo([7, 4, 5, 1], [2, 3, 6]))  
print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]))  
print(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]))  
print(consecutive_combo([44, 46], [45]))  



# ! ////////////////////////////////////////////////////////////////


def consecutive_combo(lst1, lst2):
    # Combine both lists
    combined = lst1 + lst2
    
    # Sort the combined list
    combined.sort()
    
    # Check for consecutive sequence
    for i in range(1, len(combined)):
        if combined[i] != combined[i-1] + 1:
            return False
    
    return True

# Test cases
print(consecutive_combo([7, 4, 5, 1], [2, 3, 6]))  # ➞ True
print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]))  # ➞ False
print(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]))  # ➞ False
print(consecutive_combo([44, 46], [45]))  # ➞ True
