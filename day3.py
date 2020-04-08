def readinput():
    inputs = []
    f = open("day3file.txt", "r")
    f1 = f.readlines()
    for x in f1:
        inputs.append(x)
    f.close()
    a = inputs[0].split(",")
    b = inputs[0].split(",")
    c = [a, "THE MIDDLE IS HERE",  b]
    return c


practiceinputone = ["R8","U5","L5","D3"]
practiceinputtwo = ["U7","R6","D4","L4"]

def checkvalues(firstwire, secondwire):
    if firstwire[0] - firstwire[1] == secondwire[0] - secondwire[1] and firstwire[2] - firstwire[3] == secondwire[2] - secondwire[3]:
        print(firstwire)
        return True
    else:
        return False

#return every value of [0, 0, 0, 0]


def wirevalues(firstwire, secondwire):
    #R, L, U, D
    count = [0,0,0,0]
    counttwo = [0,0,0,0]
    pointsofintersection = []

    for x in firstwire:
        right = 0
        left = 0
        up = 0
        down = 0
        y = 0
        if x[0] == "R":
            right = int(x[1])
            while y < right:
                count[0] = count[0] + 1
                y += 1
                for second in secondwire:
                    print(second)
                    secondright = 0
                    secondleft = 0
                    secondup = 0
                    seconddown = 0
                    secondy = 0
                    if second[0] == "R":
                        secondright = int(second[1])
                        while secondy < secondright:
                            counttwo[0] = counttwo[0] + 1
                            secondy += 1
                            print(count)
                            print(counttwo)
                            print(checkvalues(count, counttwo))
                            if(checkvalues(count, counttwo)):
                                pointsofintersection.append(counttwo)
                
                    
                
        #left
                    elif second[0] == "L":
                        secondleft = int(second[1])
                        while secondy < secondleft:
                            counttwo[1] = counttwo[1] + 1
                            secondy += 1 
                            print(counttwo)
                            if(checkvalues(count, counttwo)):
                                pointsofintersection.append(counttwo)
        #up
                    elif second[0] == "U":
                        secondup = int(second[1])
                        while secondy < secondup:
                            counttwo[2] = counttwo[2] + 1
                            secondy += 1
                            if(checkvalues(count, counttwo)):
                                pointsofintersection.append(counttwo)

        #down
                    else:
                        seconddown = int(second[1])
                        while secondy < seconddown:
                            counttwo[3] = counttwo[3] + 1
                            secondy += 1 
                            if(checkvalues(count, counttwo)):
                                pointsofintersection.append(counttwo)
                    
                counttwo = [0,0,0,0]

        #left
        elif x[0] == "L":
            left = int(x[1])
            while y < left:
                count[1] = count[1] + 1
                y += 1 
                for second in secondwire:
                    secondright = 0
                    secondleft = 0
                    secondup = 0
                    seconddown = 0
                    secondy = 0
                    if second[0] == "R":
                        secondright = int(second[1])
                        while secondy < secondright:
                            counttwo[0] = counttwo[0] + 1
                            secondy += 1
                            if(checkvalues(count, counttwo)):
                                pointsofintersection.append(counttwo)
                
                    
                
        #left
                    elif second[0] == "L":
                        secondleft = int(second[1])
                        while secondy < secondleft:
                            counttwo[1] = counttwo[1] + 1
                            secondy += 1 
                            if(checkvalues(count, counttwo)):
                                pointsofintersection.append(counttwo)
        #up
                    elif second[0] == "U":
                        secondup = int(second[1])
                        while secondy < secondup:
                            counttwo[2] = counttwo[2] + 1
                            secondy += 1
                            if(checkvalues(count, counttwo)):
                                pointsofintersection.append(counttwo)

        #down
                    else:
                        seconddown = int(second[1])
                        while secondy < seconddown:
                            counttwo[3] = counttwo[3] + 1
                            secondy += 1 
                            if(checkvalues(count, counttwo)):
                                pointsofintersection.append(counttwo)
        #up     
                counttwo = [0,0,0,0]

        elif x[0] == "U":
            up = int(x[1])
            while y < up:
                count[2] = count[2] + 1
                y += 1 
                for second in secondwire:
                    secondright = 0
                    secondleft = 0
                    secondup = 0
                    seconddown = 0
                    secondy = 0
                    if second[0] == "R":
                        secondright = int(second[1])
                        while secondy < secondright:
                            counttwo[0] = counttwo[0] + 1
                            secondy += 1
                            if(checkvalues(count, counttwo)):
                                pointsofintersection.append(counttwo)
                
                    
                
        #left
                    elif second[0] == "L":
                        secondleft = int(second[1])
                        while secondy < secondleft:
                            counttwo[1] = counttwo[1] + 1
                            secondy += 1 
                            if(checkvalues(count, counttwo)):
                                pointsofintersection.append(counttwo)
        #up
                    elif second[0] == "U":
                        secondup = int(second[1])
                        while secondy < secondup:
                            counttwo[2] = counttwo[2] + 1
                            secondy += 1
                            if(checkvalues(count, counttwo)):
                                pointsofintersection.append(counttwo)

        #down
                    else:
                        seconddown = int(second[1])
                        while secondy < seconddown:
                            counttwo[3] = counttwo[3] + 1
                            secondy += 1 
                            if(checkvalues(count, counttwo)):
                                pointsofintersection.append(counttwo)
                counttwo = [0,0,0,0]
        #down
        else:
            down = int(x[1])
            while y < down:
                count[3] = count[3] + 1
                y += 1 
                for second in secondwire:
                    secondright = 0
                    secondleft = 0
                    secondup = 0
                    seconddown = 0
                    secondy = 0
                    if second[0] == "R":
                        secondright = int(second[1])
                        while secondy < secondright:
                            counttwo[0] = counttwo[0] + 1
                            secondy += 1
                            if(checkvalues(count, counttwo)):
                                pointsofintersection.append(counttwo)
                
                    
                
        #left
                    elif second[0] == "L":
                        secondleft = int(second[1])
                        while secondy < secondleft:
                            counttwo[1] = counttwo[1] + 1
                            secondy += 1 
                            if(checkvalues(count, counttwo)):
                                pointsofintersection.append(counttwo)
        #up
                    elif second[0] == "U":
                        secondup = int(second[1])
                        while secondy < secondup:
                            counttwo[2] = counttwo[2] + 1
                            secondy += 1
                            if(checkvalues(count, counttwo)):
                                pointsofintersection.append(counttwo)

        #down
                    else:
                        seconddown = int(second[1])
                        while secondy < seconddown:
                            counttwo[3] = counttwo[3] + 1
                            secondy += 1 
                            if(checkvalues(count, counttwo)):
                                pointsofintersection.append(counttwo)
                counttwo = [0,0,0,0]
    
    return pointsofintersection



countprac = [0,0,0,0]
countprac2 = [0,0,0,0]

print(wirevalues(practiceinputone, practiceinputtwo))
#print(readinput())