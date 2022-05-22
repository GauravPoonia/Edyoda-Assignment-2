# to sort the list of tuples with second value


l = []
print("Need element ? 'Y/N' : ")
ch=str(input())

while(ch=='Y') :
    print("Enter the tuple elements two at a time (eg - 12) : ")
    i=(input())
    l.append(tuple(i))
    print("Need element ? 'Y/N' : ")
    ch=str(input())


print("List of Tuple before sorting : " + str(l))


listLen = len(l); 
for i in range(0, listLen):
    for j in range(0, listLen - i - 1):
        if(l[j][-1] > l[j + 1][-1]):
            swap = l[j]
            l[j] = l[j + 1]
            l[j + 1] = swap


print("List of Tuple after sorting : " + str(l))
