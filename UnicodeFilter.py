def unicodeFilter(readFile):
    o=open(readFile,"r")
    text=o.read()
    o.close()
    w=open("OutputText.txt","w")
    for i in text:
        try: 
            i.encode("ascii")
            w.write(i)
        except UnicodeEncodeError:
            continue
    w.close()
        
unicodeFilter("test_unicode.txt")
