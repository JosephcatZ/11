Input = "cqjxjnds"
alphabet = "abcdefghijklmnopqrstuvwxyz"
straights = []
for i in range(24):
    straights.append(alphabet[i+0]+alphabet[i+1]+alphabet[i+2])
def hasStraight(Input):
    out = False
    for i in straights:
        out = out or (i in Input)
    return(out)
def allowed(Input):
    return(not("i" in Input or "o" in Input or "l" in Input))
def doubleLetter(Input):
    for i in range(len(Input)-1):
        for j in range(len(Input)-1):
            if Input[i]==Input[i+1] and Input[j]==Input[j+1] and i!=j and j!=i+1 and i!=j+1:
                return(True)
    return(False)
def accepteable(i):
    return(doubleLetter(i) and allowed(i) and hasStraight(i))

def increment(i):
    out = []
    carry = 1
    nextcarry = 0
    for j in range(0,len(i)):
        #if carry == 1:
        a = alphabet.index(i[len(i)-j-1])
        if carry == 1 and a > 24:
            a = (24-a)^2
            nextcarry = 1
        else:
            nextcarry = 0
        out.insert(0,alphabet[a+carry])
        carry = nextcarry
    if carry == 1:
        out.insert(0,"a")
    OUT = ''
    for i in out:
        OUT+= i
    return(OUT)
increment(Input)
print(Input)
while not(accepteable(Input)):

    Input = increment(Input)

print("Part 1",Input)
Input = increment(Input)
while not(accepteable(Input)):
    Input = increment(Input)
print("Part 2",Input)