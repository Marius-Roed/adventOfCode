test = open("./day2.test", "r")
input = open("./day2.input", "r")

splits = input.read().split("\n")


def compare(num1, num2):
    return int(num1) - int(num2)


def prob1():
    safe = 0

    for x in range(len(splits) - 1):
        line = splits[x]
        searching = False
        numbers = []
        for i in range(len(line.split(" "))-1):
            char = line.split()
            temp = compare(char[i], char[i+1])
            if temp < -3 or temp == 0 or temp > 3:
                searching = True
                continue
            numbers.append(temp)

        if numbers[0] < 0:
            for num in numbers:
                if num > 0:
                    searching = True
                    continue
        else:
            for num in numbers:
                if num < 0:
                    searching = True
                    continue
        if searching:
            continue

        safe = safe + 1

    print(safe)


def prob2():
    safe = 0
    first = True

    for x in range(len(splits) - 1):
        if not first:
            continue
        line = splits[x]
        searching = False
        numbers = []
        first = True
        for i in range(len(line.split()) - 1):
            char = line.split()
            temp = compare(char[i], char[i+1])
            if first and temp < -3 or temp == 0 or temp > 3:
                numbers.append(temp)
                first = False
                continue
            elif not (temp < -3 or temp == 0 or temp > 3):
                numbers.append(temp)
                continue

        if numbers[0] < 0:
            for num in numbers:
                if num > 0:
                    searching = True
                    continue
        else:
            for num in numbers:
                if num < 0:
                    searching = True
                    continue
        if searching:
            first = True
            continue

        safe = safe + 1

    print(safe)


if __name__ == "__main__":
    prob1()
    prob2()
