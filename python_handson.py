
#Day 27-June-204

#1 Problem:

# In this challenge, the user enters a string and a substring. You have to print the number 
# of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.


def count_substring(string, sub_string):
    count = 0
    len_ss = len(sub_string)  # Length of the substring
    
    # Iterate through the string in steps of the length of the substring
    for i in range(len(string) - len_ss + 1):
        # Check if the substring matches the slice of the string
        if string[i:i+len_ss] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

#2 Problem:

# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

# Hello firstname lastname! You just delved into python.


def print_full_name(first, last):
     print(f"Hello {first_name} {last_name}! You just delved into python.")
    
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

# Date 28-June
#Problem 3

# Ms. Gabriel Williams is a botany professor at District College. One day, she asked her 
# student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

def average(array):
    #your code goes here
    sum=0
    arr= set(array)
    n= len(arr)
    for i in arr:
        sum=sum+i   
    return sum/n

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#29 June

# Problem 4:
# In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

def a(s):
    if any(char.isalnum() for char in s):
        print("True")
    else:
        print("False")

def b(s):  
    if any(char.isalpha() for char in s):
        print("True")
    else:
        print("False")

def c(s):  
    if any(char.isdigit() for char in s):
        print("True")
    else:
        print("False")

def d(s):   
    if any(char.islower() for char in s):
        print("True")
    else:
        print("False")

def e(s):  
    if any(char.isupper() for char in s):
        print("True")
    else:
        print("False")

if __name__ == '__main__':
    s = input("")
    a(s)
    b(s)
    c(s)
    d(s)
    e(s)

#01 July
#problem 5
#Given an integer, , print the following values for each integer  from  to :

# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary

def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        dec = i
        octa = oct(i)[2:]
        dexa = hex(i)[2:].upper()
        bina = bin(i)[2:]
        print(f"{dec:>{width}} {octa:>{width}} {dexa:>{width}} {bina:>{width}}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#problem 6
# Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .
# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

n = int(input())
integer_list = map(int, input().split())
t = tuple(integer_list)
print(hash(t))
###Problm 7
# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be X. ( is an odd natural number, and  is  times .)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.

def print_door_mat(N, M):
    pattern = [('.|.'*(2*i + 1)).center(M, '-') for i in range(N//2)]
    welcome_line = 'WELCOME'.center(M, '-')
    mat = pattern + [welcome_line] + pattern[::-1]
    for line in mat:
        print(line)

# Example usage:
N = 7
M = 3 * N
print_door_mat(N, M)

# P8: Nested Lists
# link - https://www.hackerrank.com/challenges/nested-list/problem

list_=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    list_.append([name,score])
second=sorted(list(set([score for name,score in list_])))[1]
print('\n'.join(sorted(list(set([name for name,score in list_ if score==second])))))













