def levenshtein_distance(token1, token2):
    # distances = [[0]*(len(token2)+1) for i in range(len(token1)+1)]
    dist = [[0] * (len(token2) + 1) for i in range(len(token1) + 1)]
    for i in range(len(token1) + 1):
        dist[i][0] = i
    for i in range(len(token2) + 1):
        dist[0][i] = i

    for i in range(1, len(token1) + 1):
        for j in range(1, len(token2) + 1):
            if (token1[i - 1] == token2[j - 1]):
                dist[i][j] = dist[i - 1][j - 1]
            else:
                dist[i][j] = min([dist[i][j - 1], dist[i - 1][j], dist[i - 1][j - 1]]) + 1
    
    distance = dist[len(token1)][len(token2)]
    return distance
            
assert levenshtein_distance("hi", "hello") == 4.0
print (levenshtein_distance(" hola", " hello"))