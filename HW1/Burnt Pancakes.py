# input should consist of pairs of four digits and one character, a hyphen,
# and one last character (#C#C#C#C-X), a for A* and b for BFS
input = "1b2b3w4b-a"
#givenStack=input()
#startingInput=input[0:8] #Needed this to reverse BFS

#heuristic = ID of largest pancake still out of place
#int g indicates cost (#of pancakes flipped)

queue=[]
costTracker=[] #used for a*
g=[]
h=[]

visited=[]
path=[]
formattedPath=[]


startingInput=""
class node: 
    def __init__(self, pancakes, parent, heuristic, cost): 
        self.pancakes=pancakes
        self.parent = parent
        self.heuristic=heuristic
        self.cost=cost

def pancakeSort(input):
    global startingInput
    startingInput=input[0:8] #Needed this to reverse BFS
    if(input[9]=='a'): # A* search
        print("A*")
        pancakes=input[0:8] #Now we have just the pancakes
        #queue.append(pancakes)
        #visited.append(pancakes)
        while(pancakes!="1w2w3w4w"): # Terminates when sorted
            pancakes=aStar(pancakes)
            print(queue)
            print(costTracker)
            print(g)
            print(h)
        print("Complete")
        
    elif(input[9]=='b'): # BFS search
        #print("BFS")
        pancakes=input[0:8] #Now we have just the pancakes
        #queue.append(pancakes)
        #visited.append(pancakes)
        while(pancakes!="1w2w3w4w"): # Terminates when sorted
            pancakes=BFS(pancakes)
            if (len(queue)>0):
                queue.pop(0)
            
        #print("Complete")
        #So now I have the result after all my BFS, but you need to find the path.
        #My thought process - if I BFS backwards with the solution, I find a node I have visited add to path.
        #visited.reverse() #=visited[::-1]
        #print(visited)
        while(pancakes!=startingInput):
            pancakes=bfsPath(pancakes) #This was initially the solution, reverse BFSing for path
            #print(path)
        #path.pop(0)
        formattedPath.append("1w2w3w4w")
        #print("PATH: ")
        for i in formattedPath:
            print(i)
        
            
    else:
        print("Please check your input")
    #print(input)
    
def aStar(pancakes): #f(n)=g(n)+h(n) cost+heuristic, expands that node
    #def __init__(self, pancakes, parent, heuristic, cost): 
    global visited
    global g
    global h
    #print(pancakes)
    #print(pancakes[0],pancakes[2],pancakes[4],pancakes[6])
    #print(queue)
    stack=[]
    reverseColor=[] #Allows me to compute the 4 derivations of each stack
    found=0 #if the combination is found in visited or queue, do not add to queue.
    stack.append(pancakes[0:2]) #first in the stack
    stack.append(pancakes[2:4]) #second in the stack
    stack.append(pancakes[4:6]) #third in the stack
    stack.append(pancakes[6:8]) #fourth in the stack
    for l in stack:
        if(l[1]=="w"):
            l=l.replace("w", "b")
            reverseColor.append(l)
        elif(l[1]=="b"):
            l=l.replace("b", "w")
            reverseColor.append(l)
    
    test=[]
    one_total=0
    two_total=0
    three_total=0
    four_total=0
    
    
    one = reverseColor[0]+stack[1]+stack[2]+stack[3]
    priorityOne=one
    one_h=0
    
    two= reverseColor[1]+reverseColor[0]+stack[2]+stack[3]
    priorityTwo=two
    two_h=0
    
    three= reverseColor[2]+reverseColor[1]+reverseColor[0]+stack[3]
    priorityThree=three
    three_h=0
    
    four= reverseColor[3]+reverseColor[2]+reverseColor[1]+reverseColor[0]
    priorityFour=four
    four_h=0
    
    if(one[6]!="4"):
        one_h=4
    elif(one[4]!="3"):
        one_h=3
    elif(one[2]!="2"):
        one_h=2
    else:
        one_h=0
    one_total=one_h+1
      
    
    if(two[6]!="4"):
        two_h=4
    elif(two[4]!="3"):
        two_h=3
    elif(two[2]!="2"):
        two_h=2
    else:
        two_h=0
    two_total=two_h+2
    
    if(three[6]!="4"):
        three_h=4
    elif(three[4]!="3"):
        three_h=3
    elif(three[2]!="2"):
        three_h=2
    else:
        three_h=0
    three_total=three_h+3
    
    if(four[6]!="4"):
        four_h=4
    elif(four[4]!="3"):
        four_h=3
    elif(four[2]!="2"):
        four_h=2
    else:
        four_h=0
    four_total=four_h+4
    
    ### Helper Function
    ### Returns the cost of a given order of pancakes, heuristic+cost
    def get_total(string):
        cost=0
        string_h=0
        string_total=0
        
        if(string==four):
            cost=4
        elif(string==three):
            cost=3
        elif(string==two):
            cost=2
        elif(string==one):
            cost=1
        
        if(string[6]!="4"):
            string_h=4
        elif(string[4]!="3"):
            string_h=3
        elif(string[2]!="2"):
            string_h=2
        else:
            string_h=0
        #print(string_h,cost)
        string_total=string_h+cost
        return string_total
    
    if(two_total<one_total):
        priorityOne=two
        priorityTwo=one
    if(two_total==one_total):
        if(tiebreak(two)>tiebreak(one)):
            priorityOne=two
            priorityTwo=one
    
    
    if(three_total<get_total(priorityOne)):
        priorityThree=priorityTwo
        priorityTwo=priorityOne
        priorityOne=three
    elif(three_total==get_total(priorityOne)):
        if(tiebreak(three)>tiebreak(priorityOne)):
            priorityThree=priorityTwo
            priorityTwo=priorityOne
            priorityOne=three
        else:
            priorityThree=priorityTwo
            priorityTwo=three
    elif(three_total<get_total(priorityTwo)):
        priorityThree=priorityTwo
        priorityTwo=three
    elif(three_total==get_total(priorityTwo)):
        if(tiebreak(three)>tiebreak(priorityTwo)):
            priorityThree=priorityTwo
            priorityTwo=three
     
    
    if(four_total<get_total(priorityOne)):
        priorityFour=priorityThree
        priorityThree=priorityTwo
        priorityTwo=priorityOne
        priorityOne=four
    elif(four_total==get_total(priorityOne)):
        if(tiebreak(four)>tiebreak(priorityOne)):
            priorityFour=priorityThree
            priorityThree=priorityTwo
            priorityTwo=priorityOne
            priorityOne=four
        else:
            priorityFour=priorityThree
            priorityThree=priorityTwo
            priorityTwo=four
    elif(four_total<get_total(priorityTwo)):
        priorityFour=priorityThree
        priorityThree=priorityTwo
        priorityTwo=four
    elif(four_total==get_total(priorityTwo)):
        if(tiebreak(four)>tiebreak(priorityTwo)):
            priorityFour=priorityThree
            priorityThree=priorityTwo
            priorityTwo=four
        else:
            priorityFour=priorityThree
            priorityThree=four
    elif(four_total<get_total(priorityThree)):
        priorityFour=priorityThree
        priorityThree=four
    elif(four_total==get_total(priorityThree)):
        if(tiebreak(four)>tiebreak(priorityThree)):
            priorityFour=priorityThree
            priorityThree=four
    
    
    ### THIS IS A HORRIBLE IMPLEMENTATION, AND I AM A HORRIBLE CODER
    ### I am using multiple lists to keep track of cost and heuristic
    queue.append(priorityOne)
    costTracker.append(get_total(priorityOne))
    if(priorityOne==one):
        g.append(1)
        h.append(one_h)
    elif(priorityOne==two):
        g.append(2)
        h.append(two_h)
    elif(priorityOne==three):
        g.append(3)
        h.append(three_h)
    elif(priorityOne==four):
        g.append(4)
        h.append(four_h)

    queue.append(priorityTwo)
    costTracker.append(get_total(priorityTwo))
    if(priorityTwo==one):
        g.append(1)
        h.append(one_h)
    elif(priorityTwo==two):
        g.append(2)
        h.append(two_h)
    elif(priorityTwo==three):
        g.append(3)
        h.append(three_h)
    elif(priorityTwo==four):
        g.append(4)
        h.append(four_h)
    
    queue.append(priorityThree)
    costTracker.append(get_total(priorityThree))
    if(priorityThree==one):
        g.append(1)
        h.append(one_h)
    elif(priorityThree==two):
        g.append(2)
        h.append(two_h)
    elif(priorityThree==three):
        g.append(3)
        h.append(three_h)
    elif(priorityThree==four):
        g.append(4)
        h.append(four_h)
        
        
    queue.append(priorityFour)
    costTracker.append(get_total(priorityFour))
    if(priorityFour==one):
        g.append(1)
        h.append(one_h)
    elif(priorityFour==two):
        g.append(2)
        h.append(two_h)
    elif(priorityFour==three):
        g.append(3)
        h.append(three_h)
    elif(priorityFour==four):
        g.append(4)
        h.append(four_h)
    
    
    

    print(one, one_total)
    print(two, two_total)
    print(three, three_total)
    print(four, four_total)
    print("Priority 1: ", priorityOne)
    print("Priority 2: ", priorityTwo)
    print("Priority 3: ", priorityThree)
    print("Priority 4: ", priorityFour)
    return ("1w2w3w4w")



### Helper Function
### Returns the numerical equivalent of a tiebreaker to help decide queue order
def tiebreak(string):
    temp=""
    for i in range(0,8):
        if(string[i]=="w"):
            temp=temp+"1"
        elif(string[i]=="b"):
            temp=temp+"0"
        else:
            temp=temp+string[i]
    return (int(temp))       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def bfsPath(pancakes): #Reverse this shenanigans through the power of BFS (I hope)
    global visited
    #print(visited)
    #print(pancakes)
    found = 0
    stack=[]
    reverseColor=[] #Allows me to compute the 4 derivations of each stack
    stack.append(pancakes[0:2]) #first in the stack
    stack.append(pancakes[2:4]) #second in the stack
    stack.append(pancakes[4:6]) #third in the stack
    stack.append(pancakes[6:8]) #fourth in the stack
    for l in stack:
        if(l[1]=="w"):
            l=l.replace("w", "b")
            reverseColor.append(l)
        elif(l[1]=="b"):
            l=l.replace("b", "w")
            reverseColor.append(l)

    four= reverseColor[3]+reverseColor[2]+reverseColor[1]+reverseColor[0]
    if(four==startingInput):
        temp=reverseColor[3]+reverseColor[2]+reverseColor[1]+reverseColor[0]+"|"
        found=1
        path.insert(0,four)
        formattedPath.insert(0,temp)
        return(path[0])
            
    three= reverseColor[2]+reverseColor[1]+reverseColor[0]+stack[3]
    #print(three)
    if(three==startingInput):
        temp=reverseColor[2]+reverseColor[1]+reverseColor[0]+"|"+stack[3]
        path.insert(0,three)
        formattedPath.insert(0,temp)
        return(path[0])

    two= reverseColor[1]+reverseColor[0]+stack[2]+stack[3]
    #print(two)
    if(two==startingInput):
        temp=reverseColor[1]+reverseColor[0]+"|"+stack[2]+stack[3]
        path.insert(0,two)
        formattedPath.insert(0,temp)
        return(path[0])
            
    one = reverseColor[0]+stack[1]+stack[2]+stack[3]
    #print(one)
    if(one==startingInput):
        temp=reverseColor[0]+"|"+stack[1]+stack[2]+stack[3]
        path.insert(0,one)
        formattedPath.insert(0,temp)
        return(path[0])

    #print(one, two, three, four)
    temp = ""
    for f in visited:
        #print(f)
        if(one==f):
            #print("ONE")
            temp=reverseColor[0]+"|"+stack[1]+stack[2]+stack[3]
            found=1
            path.insert(0,one)
            formattedPath.insert(0,temp)
            break
        elif(two==f):
            #print("TWO")
            temp=reverseColor[1]+reverseColor[0]+"|"+stack[2]+stack[3]
            found=1
            path.insert(0,two)
            formattedPath.insert(0,temp)
            break
        elif(three==f):
            #print("THREE")
            temp=reverseColor[2]+reverseColor[1]+reverseColor[0]+"|"+stack[3]
            found=1
            path.insert(0,three)
            formattedPath.insert(0,temp)
            break
        elif(four==f):
            #print("FOUR")
            temp=reverseColor[3]+reverseColor[2]+reverseColor[1]+reverseColor[0]+"|"
            found=1
            path.insert(0,four)
            formattedPath.insert(0,temp)
            break
            #print(path)
    if (found==1):
        return(path[0])

    
    
    #print(path)
    #return(path[0])
    
    
def BFS(pancakes): #Each pancake stack can be flipped 4 different ways
    #separate thine pancakes
    #print(pancakes)
    #print(queue)

    visited.append(pancakes)
    stack=[]
    reverseColor=[] #Allows me to compute the 4 derivations of each stack
    found=0 #if the combination is found in visited or queue, do not add to queue.
    stack.append(pancakes[0:2]) #first in the stack
    stack.append(pancakes[2:4]) #second in the stack
    stack.append(pancakes[4:6]) #third in the stack
    stack.append(pancakes[6:8]) #fourth in the stack
    for l in stack:
        if(l[1]=="w"):
            l=l.replace("w", "b")
            reverseColor.append(l)
        elif(l[1]=="b"):
            l=l.replace("b", "w")
            reverseColor.append(l)
    #print(stack, reverseColor)
    
    one = reverseColor[0]+stack[1]+stack[2]+stack[3]
    #print("Top: " + stack[0]+"|"+stack[1]+stack[2]+stack[3])
    #print(one)
    if(one=="1w2w3w4w"):
        return one
    else:
        for f in visited:
            if(one==f):
                found=1
                break
        for h in queue:
            if(one==h):
                found=1
                break
        if (found==0):
            queue.append(one)
    
    found=0
    two= reverseColor[1]+reverseColor[0]+stack[2]+stack[3]
    #print("Top two: " + stack[0]+stack[1]+"|"+stack[2]+stack[3])
    #print(two)
    if(two=="1w2w3w4w"):
        return two
    else:
        for f in visited:
            if(two==f):
                found=1
                break
        for f in queue:
            if(two==f):
                found=1
                break
        if (found==0):
            queue.append(two)
            
    
    found=0
    three= reverseColor[2]+reverseColor[1]+reverseColor[0]+stack[3]
    #print("Top three: " + stack[0]+stack[1]+stack[2]+"|"+stack[3])
    #print(three)
    if(three=="1w2w3w4w"):
        return three
    else:
        for f in visited:
            if(three==f):
                found=1
                break
        for f in queue:
            if(three==f):
                found=1
                break
        if (found==0):
            queue.append(three)
    
    found=0
    four= reverseColor[3]+reverseColor[2]+reverseColor[1]+reverseColor[0]
    #print("All: " + stack[0]+stack[1]+stack[2]+stack[3])
    #print(four)
    if(four=="1w2w3w4w"):
        return four
    else:
        for f in visited:
            if(four==f):
                found=1
                break
        for f in queue:
            if(four==f):
                found=1
                break
        if (found==0):
            queue.append(four)
    #print(queue)

    return (queue[0])
    #print(one)
    #print(two)
    #print(three)
    #print(four)

pancakeSort(input)
#tiebreak("1w2b3w4b")
#pancakeSort(givenStack)