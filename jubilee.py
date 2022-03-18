#remove each string anagaram of earlier string
from collections import defaultdict

def funWithAnagrams(str):
    print('hello')
    anagrams = defaultdict("string")

    for i in str:
        word = sorted(list(i))
        if word in anagrams:
            str.remove(i)
        else:
            anagrams[word]

    return anagrams.keys()


    print(funWithAnagrams(["code", "doce", "framer", "frame"]))


#put friends code in gitignore