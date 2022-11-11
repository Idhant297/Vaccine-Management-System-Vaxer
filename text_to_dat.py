import pickle
f=open('vaccines_text.txt', 'r')
f1=open('vaccines.dat', 'wb')
rows=f.readlines()
for row in rows:
    words=row.split()
    new=[]
    for i in range(len(words)):
        new.append(words[i].replace('_', '  '))
    pickle.dump(new,f1)
f.close()
f1.close()
