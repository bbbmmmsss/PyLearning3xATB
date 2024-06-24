# Print Vowels char in Alphabates
# By using filter function

vowels_char = ['a', 'e', 'i', 'o', 'u']
def print_vowels(char):

    return char in vowels_char

filtered_vowels=filter(print_vowels,vowels_char)
print(list(vowels_char))

# Without using filter function count vowels

vowels_char=['c','f','r','r','o']
for char in vowels_char:
    if char in vowels_char:
        count=+1

print(count)




