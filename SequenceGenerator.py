
def makeHibbard(H):
    h = [1]
    i = 0
    while(h[i]<H):
        h.append((2**i)-1)
        i += 1
    f = open("Hibbard.txt",'w')
    h = h[2:]
    h.sort()
    index = 0
    while h[index]<H:
        index +=1
    h = h[:index]
    for i in h:
        f.write(str(i))
        f.write(' ')
    f.close
#    print('hib',h)


def makeSedgewickA(H):
    h = [0]
    i = 0
    while(h[i]<H):
        h.append(((4**i)+3*2**(i-1))+1)
        i += 1
    h[1] = 1
    h = h[1:]
    h.sort()
    index = 0
    while h[index]<H:
        index +=1
    h = h[:index]
    f = open("SedgewickA.txt",'w')
    for i in h:
        f.write(str(i))
        f.write(' ')
    f.close
#    print('sedgea',h)
    
def makeSedgewickB(H):
    h = [0]
    i = 0
    while(h[i]<H):
        h.append(4**(i+1)-6*2**(i)+1)
        i += 1
    i = 0
    while(h[i]<H):
        h.append(9*(4**(i-1)-2**(i-1))+1)
        i += 1
    h.sort()
    index = 0
    while h[index]<H:
        index +=1
    h = h[3:index]
    f = open("SedgewickB.txt",'w')
    for i in h:
        f.write(str(i))
        f.write(' ')
    f.close
#    print('sedgeb',h)      
    
def makePratt(H):
    h = [0]
    p = [0]
    q = [0]
    i = 0
    j = 0
    while(p[i]<H):
        p.append(2**i)
        i += 1
    while(q[j]<H):
        q.append(3**j)
        j += 1
    h = p+q
    h.sort()
  #  print('p=',p,'\nq=',q,'\nh=',h)
    for i in range(0,len(p)):
        for j in range(0,len(q)):
            temp = (p[i]*q[j])
            if temp not in h:
                h.append(temp)
    h.sort()
    index = 0
    while h[index]<H:
        index +=1
    h = h[3:index]
    f = open("Pratt.txt",'w')
    for i in h:
        f.write(str(i))
        f.write(' ')
    f.close
#    print('prat',h)
    
    

def main():


    H = int(input('what is the largest gap value desired?'))
    h = makeHibbard(H)
    p = makePratt(H)
    s1 = makeSedgewickA(H)
    s2 = makeSedgewickB(H)
    
main()
