import numpy as np

def P(features, y_values):
    w=np.array((0.0,0.0))
    print("weights: ", w)
    print("features: \n", features)
    print("y_values: ", y_values)
    print();
    for i in range(100):
        for i,p in enumerate(features):
            if sum(w * p) >= 0:
                if y_values[i] == -1:
                    w = w - p

            else:
                if y_values[i] == 1:
                    w = w + p
    return(w)


def sigmoid(w,xi):
    return 1/(1+np.exp(-np.inner(w,xi)))

def L(features, y_values):
    alpha = 0.1
    w=np.array((0.0,0.0))
    for i in range(100):
        for i, p in enumerate(features):
            y=1
            if y_values[i]==-1:
                y=0
            g = sigmoid(w,p)
            w += alpha * (y-g) * p
            
    prob=[]
    for i in range(len(features)):
        current_data = features[i]
        prob.append(sigmoid(w,current_data))
    prob = np.array(prob)
    #print(prob)
    return prob
    

    
#userInput = "P (0, 2,+1) (2, 0, -1) (0, 4,+1) (4, 0, -1)"    # -2 0
#userInput = "P (2, 0, -1) (5, 2, +1) (0, 4,+1) (4, 0, -1) (6, 1, -1)"
#userInput = "P (0, 2,+1) (2, 0, -1) (0, 4, -1) (4, 0, +1) (0, 6, -1) (6, 0, +1)"  # 0 -2

userInput = "L (0, 2,+1) (2, 0, -1) (0, 4, -1) (4, 0, +1) (0, 6, -1) (6, 0, +1)"

data=[]
if userInput[0]=="P":
    userInput=userInput[2:]
    userInput=userInput.replace(','," ")
    userInput=userInput.replace('('," ")
    userInput=userInput.replace(')'," ")
    #print(userInput)
    data=userInput.split()

    triples=[]
    y_values=[]
    for i in range(len(data)):
        if i%3==0:
            triples.append((int(data[i]),int(data[i+1])))
            y_values.append(int(data[i+2]))
    features=np.array(triples)
    result = (P(features, y_values))
    print()
    print(result[0], result[1])


elif userInput[0]=="L":
    userInput=userInput[2:]
    userInput=userInput.replace(','," ")
    userInput=userInput.replace('('," ")
    userInput=userInput.replace(')'," ")
    data=userInput.split()

    features=[]
    y_values=[]
    for i in range(len(data)):
        if i%3==0:
            features.append((int(data[i]),int(data[i+1])))
            y_values.append(int(data[i+2]))
    features=np.array(features)
    
    result = (L(features, y_values))
    for i in range(len(result)):
        print(round(result[i],2), end=" ")
