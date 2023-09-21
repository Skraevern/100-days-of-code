piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

print(piano_keys[2:5])  # ['c', 'd', 'e'] From up to. Not including 5
print(piano_keys[:5])  # ['a', 'b', 'c', 'd', 'e'] Up to. Not including 5
print(piano_keys[2:5:2])  # ['c', 'e'] Up to. Steps of 2.
print(piano_keys[::2])  # ['a', 'c', 'e', 'g'] From 0 to end. Skip every second one
print(piano_keys[::-1])  # ['g', 'f', 'e', 'd', 'c', 'b', 'a'] Revert.


piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

print(piano_tuple[2:5])  # ('mi', 'fa', 'so') From up to. Not including 5
print(piano_tuple[:5])  # ('do', 're', 'mi', 'fa', 'so') Up to. Not including 5
print(piano_tuple[2:5:2])  # ('mi', 'so') Up to. Steps of 2.
print(piano_tuple[::2])  # ('do', 'mi', 'so', 'ti') From 0 to end. Skip every second one
print(piano_tuple[::-1])  # ('ti', 'la', 'so', 'fa', 'mi', 're', 'do') Revert.
