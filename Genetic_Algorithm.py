# Genetic_N_Queen.py, Seungjun Lee, 2020.04.15
# N-Queen Genetic Algorithm

import random
import numpy as np
import matplotlib.pyplot as plt
import copy
import sys

generation = 0; # Initalized generation
n = 5 # Chess number
initPopulationNumber = 100 # Initalized Population of genes
chromoList = [] # Chromosome list
temp = []  # Temporary Chromosome list


def ChromosomeDesign(temp) :
    temp = np.random.randint(1,6,size=5).tolist()

    return temp;


def Initialization(initPopulationNumber, chromoList, temp) :
    for i in range(initPopulationNumber) :
        temp = ChromosomeDesign(temp)
        temp.extend([0]) # Add initalized score
        chromoList.append(temp)
        
    return chromoList;

def FitnessEvaluation(initPopulationNumber, chromoList, n) :
    for i in range(initPopulationNumber) :
        for j in range(n) :
            for k in range(n) :
                if(j + k + 1 < n) :
                    if(chromoList[i][j] == chromoList[i][j + k + 1]) : # Check rows
                       chromoList[i][5] += 1 # chromoList[i][5] is measure for selection
           
                    if(chromoList[i][j + k + 1] + (k + 1) <= n) :  # Check columns
                        if(chromoList[i][j] == chromoList[i][j + k + 1] + (k + 1)) :
                           chromoList[i][5] += 1
                        if(chromoList[i][j] == chromoList[i][j + k + 1] - (k + 1)) :
                           chromoList[i][5] += 1

    return chromoList;



def Selection(initPopulationNumber, chromoList, n, generation) : # Ranking Selection
    chromoList = sorted(chromoList, key =lambda g: g[5])
    del chromoList[10:initPopulationNumber]
  
    for i in range(10) :
        if(chromoList[i][5] == 0) :

           
            print("I found ",n,"-Queen solution\n")
            print("current generation : ",generation,"\n")
            print(chromoList[i]);
           
            solution = [['' for col in range(n)]for row in range(n)]

            temp = [['' for col in range(n)]for row in range(n)] # List for table 
            for j in range(n) :
                for k in range(n) :
                    if(k+1==chromoList[i][j]) :
                        solution[j][k] = 'Q'

           
            j = n-1;
            for i in range(n) :
                
                for k in range(n) :
                    temp[i][k] = solution[k][j]
                j-=1;    

           
            # Display solution table
            plt.table(cellText=temp,colWidths = [.050,.050,.050,.050,.050],rowLabels = None, colLabels= None, loc="center")
            plt.show()
            sys.exit(1);


    for i in range(10) :
        chromoList[i][5] = 0; # initialize score

    return chromoList;




def CrossOver(chromoList) : # Random single cross over
    index = 0
    crossPointList = np.random.randint(1,5,size=5).tolist() # Point for crossover

   

    chromoCopyedList= copy.deepcopy(chromoList); # Temporary copyed geneList for crossover
                                                               
    for i in crossPointList :
        for j in range(5) :
            if(j < i) :
                ta = chromoCopyedList[index][j]
                tb = chromoCopyedList[index + 1][j]
                chromoCopyedList[index + 1][j] = ta
                chromoCopyedList[index][j] = tb                                                                            
        index+=2

    return chromoCopyedList;


def Mutation(chromoList) : # 20% Mutation among crossover
   
    mutation_1 = random.sample(range(0,9),2) # Select chromosome for mutation 20%

    mutation_2 = np.random.randint(0,5,size=2).tolist() # Select gene list for mutation

    mutation_3 = np.random.randint(1,6,size=2).tolist(); # Select gene for mutation


    for i in range(2):
        chromoList[mutation_1[i]][mutation_2[i]] = mutation_3[i];

    return chromoList;



def Loop3_6(chromoList):

   

  
    chromoList = FitnessEvaluation(initPopulationNumber, chromoList, n);

    chromoList = Selection(initPopulationNumber, chromoList, n, generation);

    
    # Repeat step5,step6 until the number of children becomes initPopulationNumber
    tempList = [];
    tempList2 = copy.deepcopy(chromoList);
    tempList.extend(chromoList)
    for i in range(9) :
        tempList2 = CrossOver(chromoList);
        tempList.extend(Mutation(tempList2));

       
    return tempList;




loopList=[]; # ChromoList for repeat step 3~6
chromoList = Initialization(initPopulationNumber, chromoList, temp)


while(1) :

   
    chromoList = Loop3_6(chromoList);
   
     # step7 next generation
    generation+=1;
    # step8 back to 3)

   




