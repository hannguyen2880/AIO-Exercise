def character_count(word):
    dic = {}
    for ch in word:
        if ch in dic:
            dic[ch] += 1
        else:
            dic[ch] = 1
    return dic

#MAIN Program
assert character_count ("Baby") == {'B': 1 , 'a': 1 , 'b': 1 , 'y': 1}
print (character_count('smiles'))
