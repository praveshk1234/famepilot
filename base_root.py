import math
listdata = list()
def find_root(a,b,c):
    b_root =  b **2 - 4 * a * c
    sq_root = math.sqrt(b_root)
    pos_root = (sq_root - b)/(2 *a)
    neg_root = (-sq_root -b)/ ( 2 * a)
    listdata.append(int(pos_root))
    listdata.append(int(neg_root))
    data = tuple(listdata)
    return data


a=find_root(2,10,8)
print(a)
