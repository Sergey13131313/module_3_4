# Напишите функцию single_root_words, которая принимает
# одно обязательное слово в параметр root_word, а далее
# неограниченную последовательность в параметр *other_words.
# Функция должна составить новый список same_words только
# из тех слов списка other_words, которые содержат root_word
# или наоборот root_word содержит одно из этих слов. После
# вернуть список same_words в качестве результата своей работы.

def singleRootWords(rootWord, *otherWords)->[]:
    sameWords = []

    for x in range(len(otherWords)):
        if otherWords[x].lower() in rootWord.lower():
            sameWords.append(otherWords[x])
        elif rootWord.lower() in otherWords[x].lower():
            sameWords.append(otherWords[x])

    return  sameWords



sameWords1 = singleRootWords('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
sameWords2 = singleRootWords('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(sameWords1)
print(sameWords2)