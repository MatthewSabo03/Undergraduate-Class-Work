'''I had to throw everything into 1 file because of issues of borrowing between 2 questions
    No Idea why this happened
'''

from abc import ABC, abstractmethod
import math
import random
import textwrap

class Artifical_Nueron():
    def __init__(self, input, learningRate):
        self.inputs = input
        self.classification = None
        self.weights = [random.randrange(-.05,.05) for i in range(self.inputs)]
        self.bias_weight = [random.randrange(-.05, .05) for i in range(self.inputs)]
        self.learningRate = learningRate
    
    def train_data(self, expected_output, output, result):
        new_weights = []
        for weights in range(len(self.weights)):
            new_weights.append(self.weights[weights] + self.learningRate*(expected_output - output)* result)   
        self.weights = new_weights    

    def get_weights(self):
        return self.weights
    def set_weights(self, weight):
        self.weights = weight
    def get_learning_rate(self):
        return self.learningRate
    def set_learning_rate(self, newRate):
        self.learningRate = newRate
    def get_bias_weights(self):
        return self.bias_weight
    def set_bias_weights(self, new_weights):
        self.bias_weight = new_weights


''' QUESTION 1'''
class Perceptron(Artifical_Nueron):
    def __init__(self, record):
        super().__init__()
        self.inputs = record
        
    def classify(self, record):
        weightSum = 0
        for i in range(len(self.weights)):
            weightSum += self.weights[i]* record[i]
            
        for i in range(len(self.bias_weight)):
            weightSum += self.bias_weight[i]
        
        if weightSum > 0:
            return 1
        else:
            return -1
    
    def train(self, expected_output, output, record):
        return self.train_data(expected_output, output, record)
    
''' QUESTION 2 '''
class LinearUnit(Artifical_Nueron):
    def __init__(self, classification, learningRate, weights, bias_weight, inputs, record):
        super().__init__(classification, learningRate, weights, bias_weight, inputs)
        self.inputs = record
    
    def classify(self, record):
        weightSum = 0
        for i in range(len(self.weights)):
            weightSum += self.weights[i]* record[i]
            
        return weightSum
    
    def train(self, expected_output, output, record):
        # output = self.error
        # expected_output = weightSum
        # record = record
        return self.train_data(expected_output, output, record)

''' QUESTION 3 '''
class SigmoidUnit(Artifical_Nueron):
    def __init__(self, classification, learningRate, weights, bias_weight, inputs, record):
        super().__init__(classification, learningRate, weights, bias_weight, inputs)
        self.inputs = record
    
    def classify(self, record):
        weightSum = 0
        for i in range(len(self.weights)):
            weightSum += self.weights[i]* record[i]
        sigma = 1/(1+math.exp(-weightSum))
        return sigma
        
    def train(self, expected_output, output, record):
        return self.train_data(expected_output, output, record)

''' QUESTION 4 '''
class TanhUnit(Artifical_Nueron):
    def __init__(self, classification, learningRate, weights, bias_weight, inputs, record):
        super().__init__(classification, learningRate, weights, bias_weight, inputs)
        self.inputs = record
    
    def classify(self, record):
        weightSum = 0
        # Dot Function
        for i in range(len(self.weights)):
            weightSum += self.weights[i]* record[i]
        squash = math.tanh(weightSum)
        return squash
        
    
    def train(self, expected_output, output, record):
        return self.train_data(expected_output, output, record)

''' QUESTION 6 '''
def trainNueron(artificial_neuron, file, iterations):
    # iterate as many times as defined and train artifical nueron

    dataset = processFile(file)    
    # Counter Variable
    curr_iteration = 0
    '''Training Loop'''
    while curr_iteration <= iterations:
        for data in range(len(dataset)):
            # Takes off last value of list so its just yes/no/abstain
            dlist = dataset[data][0:(len(dataset[data])-1)]
            # Calls train function of nueron where Democrat = 1
            artificial_neuron.train(dataset[data][len(dataset[data])-1], artificial_neuron.classify(dlist), dlist)
            
        curr_iteration+=1
            
    return artificial_neuron

def processFile(file):
    # Opens specified file
    f = open(file, "r")
    
    vote_data = []
    
    # loops through every line until end of file and checks for comments
    for x in f:
        line = f.readline()
        if line[:2] == "//":
            # Comment in file detected, skip to next line
            pass
        else:
            # Comment not found, split line into parts of 2, add them to list to be further processed
            vote_data.append(textwrap.wrap(line, 2))
    
    # Closes the file since we no longer need to access it
    f.close()
    
    # Main Dataset that will be processed and passed into Artifical Nueron
    dataset = [[] for i in range(len(vote_data))]
    
    # Access entire list and adds up each instance of a action so it can be read
    '''Dataset Process Loop'''
    for m in range(len(vote_data)):
        # iterate over internal list
        for n in range(len(vote_data[m])):
            match vote_data[m][n]:
                # Yes = 1
                # No = -1
                # Abstain = 0
                case "10":
                    # Yes
                    dataset[m].append(1)
                case "01":
                    # No
                    dataset[m].append(-1)
                case "11":
                    # Abstain
                    dataset[m].append(0)
                case "1":
                    # Democrat
                    dataset[m].append(1)
                case "0":
                    # Republican
                    dataset[m].append(-1)
    return dataset

''' QUESTION 8 '''
dem_dataset = processFile("vote-dem.txt")
rep_dataset = processFile("vote-rep.txt")
gen_dataset = processFile("vote-gen.txt")
iterations = 25
dem_nueron = Perceptron(dem_dataset)
rep_nueron = Perceptron(rep_dataset)
gen_nueron = Perceptron(gen_dataset)

trainNueron(dem_nueron, "vote-dem.txt", iterations)
trainNueron(rep_nueron, "vote-rep.txt", iterations)
trainNueron(gen_nueron, "vote-gen.txt", iterations)

def testNueron(nueron, dataset):
    counter = 0
    total = 0
    for data in range(len(dataset)):
        dlist = dataset[data][0:(len(dataset[data])-1)]
        total += nueron.classify(dlist)
        counter +=1
    return (total/counter)*100

test_dem = testNueron(dem_nueron, gen_dataset)
test_rep = testNueron(rep_nueron, gen_dataset)
test_gen = testNueron(gen_nueron, gen_dataset)

print("The accuracy of nueron trained on vote-dem.txt is:", test_dem, "%")
print("The accuracy of nueron trained on vote-rep.txt is:", test_rep, "%")
print("The accuracy of nueron trained on vote-gen.txt is:", test_gen, "%")
