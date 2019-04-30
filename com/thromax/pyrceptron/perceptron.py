"""
    @author: Thromax
    @version: 1.0
"""


class perceptron:
    
    l_rate = 0
    weights = []
    
    def __init__(self, l_rate, n_inputs):
        # Learning rate initialization
        self.l_rate = l_rate
        print("Learning rate set to: ", self.l_rate)
        
        # Weights initialization
        print("Number of inputs set to: ", n_inputs, " inputs")
        for i in range(0, n_inputs):  # @UnusedVariable
            self.weights.append(0)
        
    def activation(self, data):
        """
        Being w = weight and x = input
        z = w1x1 + w2x2 + ... + wnxn
        """
        z = 0
        for i in range(len(self.weights)):
            z += self.weights[i] * data[i]
        
        # Result normalization (Binary Step - Activation function)
        if z > 0:
            return 1
        else:
            return 0
    
    def predict (self, data):
        # Provides estimation after training of given inputs
        for d in data:
            print("Input: ", end="")
            for i in range(len(d)):
                print(d[i], end=" ")
            print("\tResult: ", self.activation(d))
    
    def training (self, data):
        """
        Being 'w' = 'weight', 'label' = 'real result' and 'predicted' = 'perceptron result'
        w += l_rate * (label - predicted) * input 
        """
        prediction = 0
        for c_data in data:
            prediction = self.activation(c_data)
            for i in range(len(self.weights)):
                self.weights[i] += self.l_rate * (c_data[(len(c_data) - 1)] - prediction) * c_data[i]
            
            # Printing weight updating
            print ("Input: ", end="")
            for i in range(len(c_data)):
                if not i is (len(c_data) - 1):
                    print(c_data[i], end=" "),
            print("")
            print("Predicted: ", prediction, " Expected: ", c_data[len(c_data) - 1])
            print("Weights set to: ", end="")
            for i in range(len(self.weights)):
                print(self.weights[i], end=" ")
            print("\n")
