x = str(input("String: "))
def palindrome(x):
    rev = ''.join(reversed(x))
    if (x == rev):
        return True 
    return False
    
ans = palindrome(x)
if (ans):
    print("This world is palindrome")
else:
        print("This world is not a palindrome")
