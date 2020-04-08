def readinput():
    inputs = []
    f = open("day5file.txt", "r")
    f1 = f.read()
    #creates a list of string values from the file provided.
    inputs = f1.split(",")
    counter = 0
    #turns inputs into a list of integers
    for a in inputs:
        inputs[counter] = int(a)
        counter += 1
    f.close
    return inputs

def equalcheck(first, second):
    if first==second:
        return True
    else:
        return False

def lessthancheck(first, second):
    if first<second:
        return True
    else:
        return False

def zerocheck(value):
    if(value==0):
        return True
    else:
        return False

def nonzerocheck(value):
    if(value==0):
        return False
    else:
        return True

def getinstruction(value):
    valueinstruction = value/10000
    valueinstruction = str(valueinstruction)
    opcode = valueinstruction[5:]
    firstparametermode = valueinstruction[4]
    secondparametermode = valueinstruction[3]
    thirdparametermode = valueinstruction[2]
    print(valueinstruction)
    return firstparametermode

def getFirstParameter(value):
    valueinstruction = value/10000
    valueinstruction = str(valueinstruction)
    firstparametermode = valueinstruction[-3]
    intvalue = int(firstparametermode)
    return intvalue

def getSecondParameter(value):
    valueinstruction = value/10000
    valueinstruction = str(valueinstruction)
    secondparametermode = valueinstruction[-4]
    intvalue = int(secondparametermode)
    return intvalue

def getOpCode(value):
    valueinstruction = value/10000
    valueinstruction = str(valueinstruction)
    opcode = valueinstruction[-2:]
    return opcode

def getThirdParameter(value):
    valueinstruction = value/10000
    valueinstruction = str(valueinstruction)
    thirdparametermode = valueinstruction[-6]
    intvalue = int(thirdparametermode)
    return intvalue



def returndigits(value):
    stringversion = str(value)
    return (stringversion[0], stringversion[1], stringversion[3])


def intcodecomputer(inputs):
    counter = 0
    firstparametermode = 0
    secondparametermode = 0
    thirdparametermode = 0
    opcode = 0
    while inputs[counter]!=99:
        #opcode 1, 2, 3 ,4
        #determine what mode we are in
        #requires string conversion
        firstparametermode = getFirstParameter(inputs[counter])
        
        secondparametermode = getSecondParameter(inputs[counter])
        
        thirdparametermode = getThirdParameter(inputs[counter])
        opcode = getOpCode(inputs[counter])

        #opcode 1
        if opcode=="01":
            #depending on the parameters we either use position mode or immediate mode
            if firstparametermode==0:
                if secondparametermode==0:
                    if thirdparametermode==0:
                        inputs[inputs[counter+3]] = inputs[inputs[counter+1]] + inputs[inputs[counter+2]]
                    else:
                        inputs[counter+3] = inputs[inputs[counter+1]] + inputs[inputs[counter+2]]
                #second parameter immediate mode
                else:
                    if thirdparametermode==0:
                        inputs[inputs[counter+3]] = inputs[inputs[counter+1]] + inputs[counter+2]
                    else:
                        inputs[counter+3] = inputs[inputs[counter+1]] + inputs[counter+2]
            #first parameter is immediate mode 
            else:
                #second parameter is poisition mode
                if secondparametermode==0:
                    if thirdparametermode == 0:
                        inputs[inputs[counter+3]] = inputs[counter+1] + inputs[inputs[counter+2]]
                    else:
                        inputs[counter+3] = inputs[counter+1] + inputs[inputs[counter+2]]
                else:
                    if thirdparametermode==0:
                        inputs[inputs[counter+3]] = inputs[counter+1] + inputs[counter+2]
                    else:
                        inputs[counter+3] = inputs[counter+1] + inputs[counter+2]
            counter += 4

        #opcode 2
        if opcode=="02":
            #depending on the parameters we either use position mode or immediate mode
            if firstparametermode==0:
                if secondparametermode==0:
                    if thirdparametermode==0:
                        inputs[inputs[counter+3]] = inputs[inputs[counter+1]] * inputs[inputs[counter+2]]
                    else:
                        inputs[counter+3] = inputs[inputs[counter+1]] * inputs[inputs[counter+2]]
                #second parameter immediate mode
                else:
                    if thirdparametermode==0:
                        inputs[inputs[counter+3]] = inputs[inputs[counter+1]] * inputs[counter+2]
                    else:
                        inputs[counter+3] = inputs[inputs[counter+1]] * inputs[counter+2]
            #first parameter is immediate mode 
            else:
                #second parameter is poisition mode
                if secondparametermode==0:
                    if thirdparametermode == 0:
                        inputs[inputs[counter+3]] = inputs[counter+1] * inputs[inputs[counter+2]]
                    else:
                        inputs[counter+3] = inputs[counter+1] * inputs[inputs[counter+2]]
                else:
                    if thirdparametermode == 0:
                        inputs[inputs[counter+3]] = inputs[counter+1] * inputs[counter+2]
                    else:
                        inputs[counter+3] = inputs[counter+1] * inputs[counter+2]
            counter += 4

        #opcode 3
        if opcode=="03":
            #depending on the parameters we either use position mode or immediate mode
            holder = input("Give input")
            #position mode
            if(firstparametermode==0):
                inputs[inputs[counter+1]] = int(holder)
            else:
                inputs[counter+1] = int(holder)
            counter += 2
        #opcode 4
        if opcode=="04":
            if(firstparametermode==0):
                print(inputs[inputs[counter+1]])
            else:
                print(inputs[counter+1])
            counter += 2
        #opcode 5: jump if true
        if opcode=="05":
            #position mode
            if(firstparametermode==0):
                if(nonzerocheck(inputs[inputs[counter+1]])):
                    if(secondparametermode==0):
                        counter = inputs[inputs[counter+2]]
                    else:
                        counter = inputs[counter+2]
                else:
                    counter += 3
            else:
                if(nonzerocheck(inputs[counter+1])):
                    if(secondparametermode==0):
                        counter = inputs[inputs[counter+2]]
                    else:
                        counter = inputs[counter+2]
                else:
                    counter += 3

        #opcode 6: jump if false
        if opcode=="06":
            #position mode
            if(firstparametermode==0):
                if(zerocheck(inputs[inputs[counter+1]])):
                    if(secondparametermode==0):
                        counter = inputs[inputs[counter+2]]
                    else:
                        counter = inputs[counter+2]
                else:
                    counter += 3
            else:
                if(zerocheck(inputs[counter+1])):
                    if(secondparametermode==0):
                        counter = inputs[inputs[counter+2]]
                    else:
                        counter = inputs[counter+2]
                else:
                    counter += 3
        
        if opcode=="07":
            if firstparametermode == 0:
                if secondparametermode == 0:
                    if(lessthancheck(inputs[inputs[counter+1]], inputs[inputs[counter+2]])):
                        if thirdparametermode==0:
                            inputs[inputs[counter+3]] = 1
                        else:
                            inputs[counter+3] = 1
                    else:
                        if thirdparametermode == 0:
                            inputs[inputs[counter+3]] = 0
                        else:
                            inputs[counter+3] = 0
                else:
                    if(lessthancheck(inputs[inputs[counter+1]], inputs[counter+2])):
                        if thirdparametermode==0:
                            inputs[inputs[counter+3]] = 1
                        else:
                            inputs[counter+3] = 1
                    else:
                        if thirdparametermode == 0:
                            inputs[inputs[counter+3]] = 0
                        else:
                            inputs[counter+3] = 0
            else:
                if secondparametermode == 0:
                    if(lessthancheck(inputs[counter+1], inputs[inputs[counter+2]])):
                        if thirdparametermode==0:
                            inputs[inputs[counter+3]] = 1
                        else:
                            inputs[counter+3] = 1
                    else:
                        if thirdparametermode == 0:
                            inputs[inputs[counter+3]] = 0
                        else:
                            inputs[counter+3] = 0
                else:
                    if(lessthancheck(inputs[counter+1], inputs[counter+2])):
                        if thirdparametermode==0:
                            inputs[inputs[counter+3]] = 1
                        else:
                            inputs[counter+3] = 1
                    else:
                        if thirdparametermode == 0:
                            inputs[inputs[counter+3]] = 0
                        else:
                            inputs[counter+3] = 0
            counter += 4

        #opcode 8
        if opcode=="08":
            if firstparametermode == 0:
                if secondparametermode == 0:
                    if(equalcheck(inputs[inputs[counter+1]], inputs[inputs[counter+2]])):
                        if thirdparametermode==0:
                            inputs[inputs[counter+3]] = 1
                        else:
                            inputs[counter+3] = 1
                    else:
                        if thirdparametermode == 0:
                            inputs[inputs[counter+3]] = 0
                        else:
                            inputs[counter+3] = 0
                else:
                    if(equalcheck(inputs[inputs[counter+1]], inputs[counter+2])):
                        if thirdparametermode==0:
                            inputs[inputs[counter+3]] = 1
                        else:
                            inputs[counter+3] = 1
                    else:
                        if thirdparametermode == 0:
                            inputs[inputs[counter+3]] = 0
                        else:
                            inputs[counter+3] = 0
            else:
                if secondparametermode == 0:
                    if(equalcheck(inputs[counter+1], inputs[inputs[counter+2]])):
                        if thirdparametermode==0:
                            inputs[inputs[counter+3]] = 1
                        else:
                            inputs[counter+3] = 1
                    else:
                        if thirdparametermode == 0:
                            inputs[inputs[counter+3]] = 0
                        else:
                            inputs[counter+3] = 0
                else:
                    if(equalcheck(inputs[counter+1], inputs[counter+2])):
                        if thirdparametermode==0:
                            inputs[inputs[counter+3]] = 1
                        else:
                            inputs[counter+3] = 1
                    else:
                        if thirdparametermode == 0:
                            inputs[inputs[counter+3]] = 0
                        else:
                            inputs[counter+3] = 0
            counter += 4


                
            

#print(readinput())
#print(getFirstParameter(1103))
#print(getFirstParameter(-3))
#print(readinput())
print(intcodecomputer(readinput()))