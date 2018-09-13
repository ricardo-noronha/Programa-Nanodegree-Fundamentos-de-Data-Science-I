def create_groups(items, n):
    """Splits items into n groups of equal size, although the last one may be shorter."""
    groups = []
    try:
        # determine the size each group should be
        size = len(items) // n  # this line could cause a ZeroDivisionError exception

        # create each group and append to a new list
        for i in range(0, len(items), size):
            groups.append(items[i:i + size])
    except ZeroDivisionError:
        print("WARNING: Returning empty list. Please use a nonzero number.")
    finally:
        # print the number of groups and return groups    
        print("{} groups returned.".format(n))
    return groups

print("Creating 6 groups...")
for group in create_groups(range(32), 6):
    print(list(group))

print("\nCreating 0 groups...")
for group in create_groups(range(32), 0):
    print(list(group))