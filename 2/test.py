list = [[1, 3, 4], [3, 7, 2]]
newList = []
safe = 0


def compare(num1, num2):
    if num2 is None:
        num2 = 0
    return int(num1) - int(num2)


for i in range(len(list)):
    number = list[i]
    for j in range(len(number) - 1):
        temp = compare(number[j], number[j+1])
        newList.append(temp)

    if newList[0] < 0:
        for newNums in newList:
            if newNums > 0:
                continue
    else:
        for newNums in newList:
            if newNums < 0:
                continue

    safe = safe + 1


print(newList)
print(safe)
