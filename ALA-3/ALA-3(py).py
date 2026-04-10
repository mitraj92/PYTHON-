n = 121
orig = n
rev = 0

while n != 0:
    rem = n % 10
    rev = rev * 10 + rem
    n = n // 10   # integer division

if orig == rev:
    print("Palindrome")
else:
    print("Not Palindrome")