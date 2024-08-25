def collatz(number):
    if number % 2 == 0:
        r = number // 2
        print(r)
    elif number % 2 == 1:
        r = 3*number + 1
        print(r)
    return r

print("Enter number:")
try:
    num = int(input())
    r = num
    while r!=1:
        r = collatz(r)


except:
    print("ValueError Found, enter an integer value")
