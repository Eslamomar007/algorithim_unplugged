def naive(word,text):
    w = len(word)
    t = len(text)
    pos = 1
    while pos < t-w+2:
        j = w-1
        while j>0 and word[j]== text[pos+j-1]:
            j-=1
        if j ==0:print('posdf '+str(pos))
        pos +=1



tt = 'hello world ,hello'

ww = 'hello'
naive(ww,tt)