from collections import deque

def check_is_palindrome(text: str ):
    is_palindrome = True
    a = deque()
    for c in text.lower():
        if c.isalpha():
            a.append(c)
            # print(c)
            
    for i in range(len(a)// 2):
        if  a.pop() != a.popleft():
           is_palindrome = False 
    return is_palindrome
