

def word_lengt(sentence):
    words = sentence.split()
    lista = []
    for i in words:
        lista.append(len(i))
    return lista


print(word_lengt("Ce faci ?"))
