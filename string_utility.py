def count_vowels(s):
    count = 0
    for i in s:
        if i in "aeiouAEIOU":
            count += 1
    print(f"Total vowels {count}")


#reverse string
def reverse_string(s):
    return s[::-1]
    


def is_palindrome(s):
    if s == s[::-1]:
        print(" It's palindromic")
    else:
        print( "It's  not palindromic")

