def convert(input):
    return tuple(input.split(";"))


def getInput():
    puzzleInput = open("./input.txt").read().replace(
        ": ", ";").replace(
        " ", ";").replace(
        "-", ";").split()

    return [convert(i) for i in puzzleInput]


def findValidPasswords(input):
    validPasswords = []
    for tuple in input:
        password = tuple[3]
        secretChar = tuple[2]

        charForFirstIndex = password[int(tuple[0]) - 1]
        chartForSecondIndex = password[int(tuple[1]) - 1]

        if charForFirstIndex != chartForSecondIndex:
            if charForFirstIndex == secretChar or chartForSecondIndex == secretChar:
                validPasswords.append(password)

    return validPasswords


if __name__ == "__main__":
    puzzleInput = getInput()
    passwords = findValidPasswords(puzzleInput)
    print(len(passwords))
