m_dict={}
books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
for book in books:
    count = 0
    liste = []
    for bchar in book:
        count +=1
        if bchar not in liste:
          liste.append(bchar)
        else:
          pass

    m_dict[book] = (count,len(liste),(count+len(liste))/2)

print(m_dict)
