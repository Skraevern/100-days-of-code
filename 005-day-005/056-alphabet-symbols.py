
# Made this to not have to type in every character in every list in password calculator.

alphabet = "abcdefghijklmnopqrstuvwxyz"
symbols = "~`!@#$%^&*/()_-+=}{][|:;,<>.?"



alphabet_list = []
alphabet_list_upper = []
symbols_list = []

for i in range(0, len(alphabet)):
     alphabet_list.append(alphabet[i])
for i in range(0, len(alphabet)):
     alphabet_list_upper.append(alphabet[i].upper())
for i in range(0, len(symbols)):
    symbols_list.append(symbols[i])




print(alphabet_list, "\n")
print(alphabet_list_upper, "\n")
print(symbols_list, "\n")