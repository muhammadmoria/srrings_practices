"""1. Write a program that accepts a string from user. Your program should count and display number of 
vowels in that string. """
def vowe(string):
    vowels = ["a" ,"e", 'i', "o", "u", "A", "E", "I", "O", "U" ]
    count = 0 
    for char in string:
        if char in vowels:
            count += 1
    print(count)
    
#Example

vowe("""1. Write a program that accepts a string from user. Your program should count and display number of 
vowels in that string. """)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#  2. Write a program that reads a string from keyboard and display: 
# * The number of uppercase letters in the string 
# * The number of lowercase letters in the string 
# * The number of digits in the string 
# * The number of whitespace characters in the string 
def str1(strings):
    uppercase = 0
    lowercase = 0
    digits = 0
    spaces = 0
    for char in strings:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1
    print(f""" 
                    upper : {uppercase}
                    lower : {lowercase}
                    digits : {digits}
                    spaces:   {spaces}
    """)

str1("""1. Write a program that accepts a string from user. Your program should count and display number of 
vowels in that string. """)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#  3. Write a Python program that accepts a string from user. Your program should create and display a new string where the first and last characters have been exchanged.For example if the user enters the string 'HELLO' then new string would be 'OELLH 
sts = input("ENTER YOUR STRING HERE :")
new_sts = ''
new_sts = sts[-1]+sts[1:-1]+sts[0]
print(new_sts)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#  4. Write a Python program that accepts a string from user. Your program should create a new string in reverse of first string and display it. For example if the user enters the string 'EXAM' then new string would be 'MAXE' 

str1 = input("ENTER YOUR STRING HERE :")
new_str = str1[::-1]
print(new_str)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
# 5. Write a Python program that accepts a string from user. Your program should create a new string by shifting one position to left. For example if the user enters the string 'examination 2021' then new string would be 'xamination 2021e' 

str11 = input("ENTER YOUR STRING HERE :")
neww_str = str11[1:]+str11[0]
print(neww_str)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
# 6. Write a program that asks the user to input his name and print its initials. Assuming that the user always types first name, middle name and last name and does not include any unnecessary spaces. For example, if the user enters Ajay Kumar Garg the program should display A. K. G. Note:Don't use split() method

str2 = input("ENTER YOUR STRING HERE :")
initials = ''
for char in str2:
    if char.isupper():
        initials += char + '.'
print(initials)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
# 7. A palindrome is a string that reads the same backward as forward. For example, the words dad, madam and radar are all palindromes. Write a programs that determines whether the string is a palindrome. Note: do not use reverse() method 


palindrome = input("ENTER YOUR PALINDROME WORD HERE :")
if palindrome == palindrome[::-1]:
    print("PALINDROME")
else:
    print("NOT PALIONDRME")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
# 8. Write a program that display following output: 
# SHIFT 
# HIFTS 
# IFTSH 
# FTSHI 
# TSHIF 
# SHIFT 


def show():
    print("SHIFT")
    print("HIFTS")
    print("IFTSH")
    print("FTSHI")
    print("TSHIF")
    print("SHIFT")
show()
