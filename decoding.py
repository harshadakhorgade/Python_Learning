str = input(" enter string :")
coding = int(input( " 1 for coding and 0 for decoding :"))

coding == True if coding == 1 else False
words =str.split()
if (coding):
    nw =[]
    for word in words:
            if len(word) >= 3:
                r1 ="ads"
                r2 ="fgd"
                newword = r1+ word[1:] + word[:1] + r2
                nw.append(newword)
            else:
                nw.append(word[::-1])
    print(" ".join(nw))

else:
    nw =[]
    for word in words:
            if len(word) >= 3:
                newword = word[-4] + word[3:-4] 
                nw.append(newword)
            else:
                nw.append(word[::-1])
    print(" ".join(nw))


     
  

