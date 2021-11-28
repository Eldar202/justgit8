def sort_sentence(sentence):
    words = sentence.split()
    t = sorted(words, key=len)
    k = ' '.join(t)
    return(k.capitalize())





