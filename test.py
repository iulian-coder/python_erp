

def word_lengt(sentence):
    words = sentence.split()
    return [len(i) for i in words]


print(word_lengt("Ce faci ?"))
