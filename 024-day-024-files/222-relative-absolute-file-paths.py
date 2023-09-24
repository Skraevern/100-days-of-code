#   Absolute file path
# /     root
# /work/project/talk.ppt

# This file
# /Users/skraevern/Coding/100-days-of-code/024-day-024-files/222-relative-absolute-file-path.py

#   Relative file path
# ./222-relative-absolute....
# File in same directory

# ../ herfra == /Users/skraevern/Coding/100-days-of-code/  altså en opp

with open("/Users/skraevern/Desktop/my_file2.txt") as file:
    contents = file.read()
    print(contents)  # Ehllo

with open("../../../Desktop/my_file2.txt") as file:
    contents = file.read()
    print(contents)  # Ehllo
