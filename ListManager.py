def AddRem(list, item):
    if item in list:
        list.remove(item)
    else:
        list.append(item)

def maxmin(list):
    if len(list) == 0:
        return None, None
    max_val = list[0]
    min_val = list[0]
    for item in list:
        if item > max_val:
            max_val = item
        if item < min_val:
            min_val = item
    return max_val, min_val

def remdup(list):
    return set(list)

list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print("Original list:", list)
item = int(input("Enter an item to add/remove: "))
AddRem(list, item)
print("Updated list:", list)

max_val, min_val = maxmin(list)
print("Maximum value:", max_val)
print("Minimum value:", min_val)

list = remdup(list)
print("List with duplicates removed:", list)
