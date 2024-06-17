def preprocess_text(sentence):
    sentence = sentence.lower()
    sentence = sentence.replace('.', '').replace(',', '')
    words = sentence.split()
    return words

def count_word(path_file):
    with open(path_file, 'r') as f:
        data = f.read()

    words = preprocess_text(data)
    
    counter = {}
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1

    return counter

# MAIN PROGRAM
file_path = 'D:\APCS\AIO-Exercise\Module1\Week2-data-structure\P1_data.txt'
result = count_word(file_path)
assert result['who'] == 3
print(result['man'])