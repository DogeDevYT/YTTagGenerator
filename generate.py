from PyDictionary import PyDictionary

dictionary = PyDictionary()

def generate():
    print("Loading defaulttags.txt...")
    words = []
    with open('defaulttags.txt', 'r') as defaultTags:
        extractedDefaultTags = defaultTags.read().split(",")
        words += extractedDefaultTags
    print("Default tags loaded successfully")

    numOfInputs = int(input("How many different \"words\" do you have in your tags: "))

    for num in range(numOfInputs):
        temp = input("Enter word/phrase: ")
        words.append(temp)

    finalList = []

    for num in range(len(words)):
        temp = words[num]
        try:
            synonym = (dictionary.synonym(words[num])[1])
            finalList.append(synonym)
        except TypeError:
            pass
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
    with open('tags.txt', 'w') as tags:
        for item in finalList:
            print(item + ", ", end="")
            tags.write(item + ", " + '\n')

if __name__ == "__main__":
    generate()