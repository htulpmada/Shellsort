0

def main():
    a = []
    index = 0
    gaps = []
    fname = ['gaps.txt']
    swaps = 0
    comps = 0
    for i in fname:
        with open(i) as f:
            line = f.readline()
            line = line.split()
            gaps.append(0)
            for l in line:
                gaps.append(int(l))
        
        index+=1
        gaps.reverse()
    print(gaps)
    with open('input.txt')as file:
        for i in range(0,5000,1):
            try:
                t = file.readline()
                a.append(int(t.rstrip()))
            except ValueError:
                break

    #loop for each sequence
    for k in range(0,len(gaps),1):


        #for each gap
        for gap in gaps:
            #for each item in list
            for j in range(gap, len(a), 1):
                comps += 1
                if a[j]<a[j-gap]:
                    a[j],a[j-gap] = a[j-gap],a[j]
                    swaps += 1
                    for p in range(j,0,-(gap)):
                        try:
                            comps += 1
                            if a[p]<a[p-gap]:
                                swaps += 1
                                a[p],a[p-gap] = a[p-gap],a[p]
                        except IndexError:
                            break
    print(a)
    f = open('output.txt','w')
    for i in range(0,len(a)):
            f.write(str(a[i]))
            f.write('\n')
    f.close()
    f = open('Comparison.doc','w')
    f.write('comparisons = ')
    f.write(str(comps))
    f.write('\n')
    f.write('swaps = ')
    f.write(str(swaps))
    f.close
    print('comps =', comps,'\n','swaps =', swaps)
main()
