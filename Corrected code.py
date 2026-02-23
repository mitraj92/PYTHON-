print("Reverse Number Program")
num = int(input("Enter number: "))
original = num
reverse = 0
count = 0
sum_digits = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    sum_digits = sum_digits + digit
    count = count + 1
    num = num // 10

print("Reverse:", reverse)
print("Digit Count:", count)
print("Sum of digits:", sum_digits)

if reverse == original:
    print("Palindrome number")
else:
    print("Not palindrome")

if sum_digits % 2 == 0:
    print("Even sum")
else:
    print("Odd sum")