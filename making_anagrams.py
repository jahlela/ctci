def number_needed(a, b):

    counts = {}
    for char in a:counts[char] = counts.get(char, 0) + 1

    diff = 0
    for char in b:
        if char in counts:
            counts[char] -= 1
        else:
            diff += 1

    for count in counts.values():
        diff += abs(count)

    return diff

a = raw_input('Please enter the first word: ').strip()
b = raw_input('Please enter the second word: ').strip()

print number_needed(a, b)
