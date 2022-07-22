inputowners =  {
'Input.txt': 'Randy',
'Code.py': 'Stan',
'Output.txt': 'Randy'
}
dist2 ={}
list1 = list(inputowners.values())
dist_owner =list(set(list1))
for a in dist_owner:
    dist2[a] =list()
for i,value in inputowners.items():
    if value in dist2.keys():
         dist2[value].append(i)
        

print(dist2)

