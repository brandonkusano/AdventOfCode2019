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

def countdirectorbits(dictionary):
    counter = 0 
    for x in dictionary:
        counter += len(dictionary[x])
    return counter

def iskey(dictionary, value):
    if value in dictionary.keys():
        return True
    else:
        return False

def countindirectorbits(dictionary):
    counter = 0
    
   
#dictionary = createadictionary()
#print(keycheck(dictionary, 'L'))
print(countdirectorbits(createadictionary()))
print(createadictionary())