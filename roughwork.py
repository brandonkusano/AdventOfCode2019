print(-1103/100000)

def getinstruction(value):
    valueinstruction = value/10000
    valueinstruction = str(valueinstruction)
    opcode = valueinstruction[-2:]
    firstparametermode = valueinstruction[-3]
    secondparametermode = valueinstruction[-4]
    thirdparametermode = valueinstruction[-6]
    return thirdparametermode

def keycheck(dictvalue, key):
    if key in dictvalue.keys():
        return True
    else:
        return False

def createadictionary():
    listofinputs = []
    inputs={}
    f = open("day6practicefile.txt", "r")
    f1 = f.readlines()
    for x in f1:
        x = x.rstrip()
        holder = x.split(')')
        listofinputs.append(holder[0])
        listofinputs.append(holder[1])
    f.close()
    valuelist = []
    for x in range(0, len(listofinputs), 2):
        #if key exists, append it to the value list, values = []
        if keycheck(inputs, listofinputs[x]):
            valuelist = inputs[listofinputs[x]]
            valuelist.append(listofinputs[x+1])
            inputs[listofinputs[x]] = valuelist
        else:
            inputs[listofinputs[x]] = [listofinputs[x+1]]
    return inputs

print(createadictionary())
#print(getinstruction(-3))
