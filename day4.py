def securecontainer(low, high):
    possiblepasswords = []
    for x in range(low, high+1):
        stringvalue = str(x)
        firstdigit = stringvalue[0]
        seconddigit = stringvalue[1]
        thirddigit = stringvalue[2]
        fourthdigit = stringvalue[3]
        fifthdigit = stringvalue[4]
        sixthdigit = stringvalue[5]
        if digitchecker(firstdigit, seconddigit) and  digitchecker(seconddigit, thirddigit) and digitchecker(thirddigit, fourthdigit) and  digitchecker(fourthdigit, fifthdigit) and digitchecker(fifthdigit, sixthdigit) and doublesomewhere(stringvalue):
            possiblepasswords.append(stringvalue)   
    return possiblepasswords

def digitchecker(predigit, postdigit):
    if postdigit >= predigit:
        return True
    else:
        return False

def doublesomewhere(value):
    if strictdoublesomewhere(value):
        return True
    else:
        return False

#triple case
def stricttripleoddchecker(value):
    
    if value[0] == value[2] and value[0] != value[3]:
        return False
    if value[1] == value[3] and value[1] != value[4] and value[0] != value[3]:
        return False
    if value[2] == value[4] and value[2] != value[5]:
        return False
    if value[3] == value[5] and value[2] != value[5]:
        return False

    return True

#quintuple case
def strictquintupleoddchecker(value):
    if value[0] == value[2] and value[2] == value[4] and value[0] != value[5]:
        return False
    if value[1] == value[3] and value[3] == value[5]:
        return False
    else:
        return True

def strictdoublesomewhere(value):
    if value[0] == value[1]:
        return uniquecode(value)
    if value[1]==value[2]:
        return uniquecode(value)
    if value[2] == value[3]:
        return uniquecode(value)
    if value[3] == value[4]:
        return uniquecode(value)
    if value[4]==value[5]:
        return uniquecode(value)
    return False
    
def uniquecode(value):
    if value[0] == value[1] and value[0] != value[2]:
        return True
    if value[1] == value[2] and value[1] != value[3] and value[0] != value[2]:
        return True
    if value[2] == value[3] and value[2] != value[4] and value[2] != value[1]:
        return True
    if value[3] == value[4] and value[3] != value[5] and value[2] != value[4]:
        return True
    if value[4] == value[5] and value[5] != value[3]:
        return True
    
    return False


    

#print(stricttripleoddchecker("555566"))
#print(strictdoublesomewhere("113344"))
#print(uniquecode("555888"))
print(len(securecontainer(138307, 654504)))
