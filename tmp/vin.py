#coding:utf-8


f = open(r'vin.txt')

fd = f.readlines()

cf = []

l = []

for i in fd:
    if i in l:
        cf.append(i)
    else:
        l.append(i)

print(len(cf))
print(cf)
for i in set(cf):
    print(i.strip())

f.close()

