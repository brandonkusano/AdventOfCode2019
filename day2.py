def readinput():
    inputs = []
    f = open("day2file.txt", "r")
    f1 = f.read()
    inputs = f1.split(",")
    print(inputs)
    counter = 0
    for a in inputs:
        inputs[counter] = int(a)
        counter += 1
    inputs[1] = 31
    inputs[2] = 46
    f.close
    return inputs

def programalarm(inputs):
    counter = 0

    while inputs[counter]!=99:
        if(inputs[counter]==1):
            inputs[inputs[counter+3]] = inputs[inputs[counter+1]] + inputs[inputs[counter+2]]
            counter += 4
        elif inputs[counter]==2:
            inputs[inputs[counter+3]] = inputs[inputs[counter+1]] * inputs[inputs[counter+2]]
            counter += 4
    
        else:
            print('Error')
            return
    
    return inputs

print(programalarm(readinput()))
#print(readinput())