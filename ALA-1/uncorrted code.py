print("reverse number program")
num = int(input("Enter a number: "))
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
    print("reverse: ", reverse)
    print("digit count: ", count)
    print("sum digits: ", sum_digits)
    if reverse = original:
        print("palindrome number")
    else:
        print("not palindrome")
        if sum_digits % 2 == 0:
            print("even sum")
            else:
            print("odd sum")