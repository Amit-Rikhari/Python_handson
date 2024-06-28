
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