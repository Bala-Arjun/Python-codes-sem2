d={"Chandhu":99,"Eesha":74,"Dhanush":86,"Fanindra":67,"Bharath":44,"Abhi":56}
"""l=list(d)
l.sort()
k=[]
for i in d.values():
    k.append(i)
print(l)"""
"""for i in range(0, len(l)):
    print(f"{l[i]}:{k[i]}")"""
l=list(d.items())
l.sort()
"d=dict(l)"
""""for i in range(0,len(l)):
    print(l[i])"""
for k,v in l:
    print(f"{k}:{v}")