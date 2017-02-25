def countVowel(word) :
    nbVowel = 0

    for letter in word:
        if letter in ['a','e','i','o','u','y']:
            nbVowel += 1

    return nbVowel

cntNbVowel = countVowel("Combien de voyelles ?")

print(cntNbVowel)
