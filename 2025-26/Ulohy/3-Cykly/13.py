word = input("zadajte slovo: ")

for i in range(len(word)):
    print(word[i] * (i + 1))