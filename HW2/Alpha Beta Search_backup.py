#testInput = "2 4 13 11 1 3 3 7 3 3 2 2"
testInput = "1 3 8 2 4 6 5 4 3 2 5 6"

inputList = (testInput.split(' '))


for i in range(len(inputList)):
    inputList[i]=int(inputList[i])

def alphaBeta():
    print(inputList)    
    index=0
    alpha=-999999999999
    beta=  999999999999
    pruned = []
    skip=0
    v=-99999999999
    for i in range(6):
        if index%4==0:
            v=-99999999999
        if(index>=12):
            break
        if skip==1:
            skip=0
            index+=2
            continue
        if i==0:
            tempAlpha=-9999999999
            tempBeta=99999999999
            num1=inputList[index]
            num2=inputList[index+1]
            if num1>beta:
                pruned.append(index+1)
            if num1>tempAlpha:
                tempAlpha=num1
            if num2>tempAlpha:
                tempAlpha=num2
            if tempAlpha<tempBeta:
                tempBeta=tempAlpha
            if tempBeta<beta:
                beta=tempBeta
            alpha=beta
            index+=2
        else:
            print("beta",beta)
            #print(index)
            tempAlpha=-9999999999
            tempBeta=99999999999
            num1=inputList[index]
            num2=inputList[index+1]
            if index%4!=0:
                if num1>=v:
                    pruned.append(index+1)
                    index+=2
                    continue
                if num1>beta and v<beta:
                    pruned.append(index+1)
                    index+=2
                    continue
                if num1>tempAlpha:
                    tempAlpha=num1
                if num2>tempAlpha:
                    tempAlpha=num2
                if beta<v and v<tempAlpha:
                    beta=v
                elif tempAlpha<v and tempAlpha>beta:
                    beta=tempAlpha
                
                index+=2
            else:
                if num1>tempAlpha:
                    tempAlpha=num1
                if num2>tempAlpha:
                    tempAlpha=num2
                if tempAlpha<=beta:
                    pruned.append(index+2)
                    pruned.append(index+3)
                    index+=2
                    skip=1
                    continue
                else: #if tempAlpha>beta
                    v=tempAlpha
                index+=2
                
            
    print(pruned)
            
    
alphaBeta()