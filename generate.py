

def generate():
    numOfInputs = int(input("How many different \"words\" do you have in your tags: "))

    words = []

    for num in range(numOfInputs):
        temp = input("Enter word/phrase: ")
        words.append(temp)

    finalList = []

    for num in range(len(words)):
        temp = words[num]
        finalList.append(temp)

    for num in range(0, len(words), 2):
        try:
            temp = words[num] + words[num + 1]
            finalList.append(temp)
        except IndexError:
            break

    for num in range(0, len(words), 3):
        try:
            temp = words[num] + words[num + 1] + words[num + 2]
            finalList.append(temp)
        except IndexError:
            break

    print("Your tags are: ")
    for item in finalList:
        print(item + ", ", end="")

if __name__ == "__main__":
    generate()