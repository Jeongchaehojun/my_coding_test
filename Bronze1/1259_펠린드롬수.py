#2025.05.22
#b1
while True:
    num = input()
    if num == "0":
        break
    elif num == num[::-1]:
        print("yes")
    else:
        print("no")