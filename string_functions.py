def word_count(text):
    wordlist = text.split()
    wc={}
    for word in wordlist:
        if word in wc:
            wc[word]+=1
         else:
            wc[word] = 1
    return wc



if __name__ == '__main__':
    long_text  = '''
    the qick brown fox jumps over the lazy dog and attracts the chicken with a flying kick . This is real  life story about a fox , that could kick and jump . if you are really interseted in this story , then keep reading . The end'''
    