from abc import ABC, abstractmethod
import math
import random

class Artifical_Nueron():
    def __init__(self, input, learningRate):
        self.inputs = input
        self.classification = None
        self.weights = [random.uniform(-.05,.05) for i in range(len(self.inputs))]
        self.bias_weight = [random.uniform(-.05, .05) for i in range(len(self.inputs))]
        self.learningRate = learningRate
    
    def train_data(self, expected_output, output, result):
        new_weights = []
        for weights in range(len(self.weights)):
            new_weights.append(self.weights[weights] + self.learningRate*(expected_output - output)* result[weights])   
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
    