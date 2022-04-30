'''
LETTER AND SPACE COUNTER
This program takes a word, prase or sentence from users and outputs the number of vowels, consonants and spaces.
'''
'''
print("-" * 60)
print("LETTER AND SPACE COUNTER")
print("-" * 60)
word = input("Enter a word, phrase or sentence: ").lower()
vowel_count = 0
cons_count = 0
space_count = 0
vowel_list = ['a', 'e', 'i', 'o', 'u']
cons_list = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
for letter in word:
    if letter in vowel_list:
        vowel_count += 1
    elif letter == ' ':
        space_count += 1
    elif letter in cons_list:
        cons_count += 1
    else:
        pass 

print(f'There are:\n{vowel_count} vowels\n{cons_count} consonants\n{space_count} spaces')
'''

print("-" * 60)
print("GENDER COUNTER")
print("-" * 60)

num = int(input("ENTER THE TOTAL NUMBER OF PEOPLE: "))
male = 0
female = 0
n = 1
print(n)
while n <= num:
    print(n)
    gender = input("ENTER YOUR GENDER: ").lower()
    #while True:
    if gender == 'm':
        male += 1
    elif gender == 'f':
        female += 1
    else:
        print("INVALID!! Please enter M for male or F for female")
        n -= 1
    n += 1
print(male, female)

