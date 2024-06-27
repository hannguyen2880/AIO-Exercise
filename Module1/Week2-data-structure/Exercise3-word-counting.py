def preprocess_text(sentence):
    sentence = sentence.lower()
    sentence = sentence.replace('.', '').replace(',', '')
    words = sentence.split()
    return words

def word_counting(path_file):
    with open(path_file, 'r') as f:
        data = f.read()

    words = preprocess_text(data)
    
    word_counter = {}
    for word in words:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1

    return word_counter

# MAIN PROGRAM
path_file = 'D:\APCS\AIO-Exercise\Module1\Week2-data-structure\P1_data.txt'
word_counting(path_file)
result = word_counting(path_file)
assert result['who'] == 3
print(result['man'])