from collections import defaultdict
def funWithAnagrams(str):
    anagrams = defaultdict(dict)

    for i in str:
        word = sorted(list(i))
        sorted_word = ''.join(word)
        if sorted_word not in anagrams:
            anagrams[sorted_word] = i

    return sorted(list(anagrams.values()))