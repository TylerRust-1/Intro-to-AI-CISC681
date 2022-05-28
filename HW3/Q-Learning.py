#USED THE FOLLOWING RESOURCE TO HELP CONSTRUCT THIS CODE
#https://colab.research.google.com/drive/1E2RViy7xmor0mhqskZV14_NUj2jMpJz3#scrollTo=X25vn4VKw2as

import numpy as np
import random
import math

random.seed(1)

#First four numbers of input are, in order, two goals, forbidden square, wall square
#Fourth index is either a p or q.
#If p, print the optimal policy for every square.
#if q, print the four Q-values associated with each of the four possible actions in the following state
tempInput = "15 12 8 6 p"
#tempInput = "15 12 8 6 q 11"
#tempInput = "10 8 9 6 p"
#tempInput = "10 8 9 6 q 2"
#tempInput = "12 7 5 6 p"
#tempInput = "12 7 5 6 q 3"
#tempInput = "13 11 16 5 p"
#tempInput = "13 11 7 15 p"

#tempInput = input()

#initialize the exploration probability
epsilon = .5
#Living reward
step = -0.1
#discount factor
gamma = 0.1
#learning rate
alpha = 0.3

def q(string):
    qState=-1
    temp=string.split()
    g1=int(temp[0])-1
    g2=int(temp[1])-1
    forbidden=int(temp[2])-1
    wall=int(temp[3])-1
    char=temp[4]
    if(char=="q"):
        qState=int(temp[5])-1
        
    
    #This properly configures the rewards for spaces.
    env_rows=4
    env_cols=4
    q_values=np.zeros((env_rows,env_cols,4))
    rewards = np.full((env_rows, env_cols), 0)
    rewards[math.floor(g1/4),(g1%4)] = 100
    rewards[math.floor(g2/4),(g2%4)] = 100
    rewards[math.floor(forbidden/4),(forbidden%4)] = -100
    
    #Get coords of wall, done like a degenerate because I don't feel like putting more time in to it
    wall_row = math.floor(wall/4)
    wall_col = (wall%4)
    if(wall_row==0):
        wall_row=3
    elif(wall_row==1):
        wall_row=2
    elif(wall_row==2):
        wall_row=1
    elif(wall_row==3):
        wall_row=0

    #I had to flip the matrix horizontally because of the way the homework labels the matrix
    rewards=np.flip(rewards,0) 
    #print(rewards)
    
    actions = ["up","right","down","left"] #Will be determined by random int 0-3
    
    for i in range(100000):
        #if i==100000:
         #   epsilon=0
        #Declare starting space for each iteration of Q-learning
        row_index = 3
        col_index = 1
        
        #while not in a goal/forbidden state, continue exploring
        while not isTerminalState(row_index,col_index, rewards):
            action_index = nextAction(row_index, col_index, q_values)

            #perform chosen action, transition to the next state
            old_row_index, old_col_index = row_index, col_index #store the old row and column indexes
            row_index, col_index = nextLocation(row_index, col_index, action_index, actions, wall_row, wall_col)
            
            #receive reward for moving to new state, calculate temporal difference
            #Living reward only applies when not in a terminal state.
            if (isTerminalState(row_index,col_index, rewards)):
                reward = rewards[row_index, col_index]
            else:
                reward = rewards[row_index, col_index]-.1
                
            old_q_value = q_values[old_row_index, old_col_index, action_index]
            temporal_difference = reward + (gamma * np.max(q_values[row_index, col_index])) - old_q_value

            #update the Q-value for the previous state and action pair
            new_q_value = old_q_value + (alpha * temporal_difference)
            q_values[old_row_index, old_col_index, action_index] = new_q_value
    
    if(qState!=-1):
        qState_row = math.floor(qState/4)
        qState_col = (qState%4)
        if(qState_row==0):
            qState_row=3
        elif(qState_row==1):
            qState_row=2
        elif(qState_row==2):
            qState_row=1
        elif(qState_row==3):
            qState_row=0
        
    if(char=="p"):
        count=1
        for i in reversed(range(4)):
            for j in range(4):
                if(rewards[i][j]==100):
                    print(count,"goal")
                    count+=1
                    continue
                if(rewards[i][j]==-100):
                    print(count,"forbid")
                    count+=1
                    continue
                if(i==wall_row and j==wall_col):
                    print(count, "wall-square")
                    count+=1
                    continue
                best_value = -100
                best_index = 0
                for k in range(4): 
                    if (q_values[i,j][k])>best_value:
                        best_value=q_values[i,j][k]
                        best_index=k
                if(best_index==0):
                    print(count,"up")
                if(best_index==1):
                    print(count,"right")
                if(best_index==2):
                    print(count,"down")
                if(best_index==3):
                    print(count,"left")
                count+=1
                    
    elif(char=="q"):
        print("up ", round(q_values[qState_row,qState_col][0],2))
        print("right ", round(q_values[qState_row,qState_col][1],2))
        print("down", round(q_values[qState_row,qState_col][2],2))
        print("left", round(q_values[qState_row,qState_col][3],2))

def isTerminalState(row_index, col_index, rewards):
    if (rewards[row_index,col_index]==100 or rewards[row_index,col_index]==-100):
        return True
    else:
        return False

def nextAction(row_index,col_index, q_values):
    if np.random.random() < epsilon:
        return np.argmax(q_values[row_index,col_index])
    else:
        return np.random.randint(4)
    
def nextLocation(row_index,col_index,action_index, actions, wall_row, wall_col):    
    if(actions[action_index]=="up" and row_index > 0):
        if(row_index-1 != wall_row or col_index!=wall_col):
            row_index-=1
    elif(actions[action_index]=="right" and col_index < 4-1):
        if(row_index != wall_row or col_index+1 != wall_col):
            col_index+=1
    elif(actions[action_index]=="down" and row_index < 4-1):
        if(row_index+1 != wall_row or col_index!=wall_col):
            row_index+=1
    elif(actions[action_index]=="left" and col_index > 0):
        if(row_index != wall_row or col_index-1 != wall_col):
            col_index-=1
    return row_index,col_index


    
q(tempInput)