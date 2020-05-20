#IBM: Introduction to Deep Learning & Neural Networks with Keras
#Riya Philip 2020
#Lab 1



#creating the forward propagation process in neural networks, numpy library.

#creating NN for inputs=2. Randomly initializing weights and biases in the network.
import numpy as np

weights= np.around(np.random.uniform(size=6), decimals=5)
biases= np.around(np.random.uniform(size=3), decimals=5)
print(weights)
print(biases)

# now putting in the inputs (x1,x2)
x1= 0.5967
x2= 0.9283
print("The chosen inputs are: {} and {}".format(x1,x2))

# computing the weighted sum (z11) at node of first hidden layer
z11= (x1*weights[0] + x2*weights[1] + biases[0])
print("The weighted sum of inputs at the first node of the hidden layer is: {}".format(np.around((z11), decimals=5)))

# computing the weighted sum (z12) at node of first hidden layer
z12= (x1*weights[2] + x2*weights[3] + biases[1])
print("The weighted sum of inputs at the second node of the hidden layer is: {}".format(np.around((z12), decimals=5)))

#now computing a11. Definition:
a11= 1.0/(1.0+ np.exp(-z11))
print("The activation of the first node in the hidden layer is: {}".format(np.around((a11), decimals=5)))

#computing a12. Definition:
a12= 1.0/(1.0+ np.exp(-z12))
print("The activation of the second node in the hidden layer is: {}".format(np.around((a12), decimals=5)))

#computing z2
z2= (a11*weights[4] + a12*weights[5] + biases[2])
print("The weighted sum of inputs at the node in the output layer is: {}".format(np.around(z2), decimals=5))

#creating the activation function
a2= 1.0/(1.0+np.exp(-z2))
print("The output of the network for x1=0.5967 and x2= 0.9283 is: {}".format(np.around(a2), decimals=5))


#formally define structure of network:
#number of inputs
n=2
#number of hidden layers
num_hidden_layers= 2
#number of nodes in each hidden layer
m = [2,2]
#number of nodes in hidden layers
num_nodes_hidden=2
#number of nodes in output layer
num_nodes_output=1

#initializing random weights and biases
#num of nodes in the previous layer
num_nodes_previous= n 
network= {} 

#loop through each layer and randomly initialize the weights and biases associated with each node
#add 1 to the number of hidden layers in order to include the output layer
for layer in range(num_hidden_layers + 1):
    #determine name of layer

    if layer == num_hidden_layers:
        layer_name == "Output"
        num_nodes = num_nodes_output
    else:
        layer_name= 'layer_{}'.format(layer+1)
        num_nodes = m[layer]

#initialize weights and biases in each node of the current layer
    network[layer_name] = {}
    for node in range(num_nodes):
        node_name = 'node_{}'.format(node+1)
        network[layer_name][node_name] = {
            'weights' : np.around(np.random.uniform(size = num_nodes_previous), decimals=5),
            'bias' : np.around(np.random.uniform(size = 1), decimals=5),
        } 

    num_nodes_previous = num_nodes

print(network)

def initialize_network(num_inputs, num_hidden_layers, num_nodes_hidden, num_nodes_output):
    network = {}
    num_nodes_previous = num_inputs #no. nodes in previous layer
#loop through each layer, initialize weights and biases randomly
for layer in range(num_hidden_layers+1):
    if layer == num_hidden_layers:
        layer_name= "Output" 
        num_nodes = num_nodes_output
    else:
        layer_name = "layer_{}".format(layer+1) #otherwise give a layer number
        num_nodes = num_nodes_hidden[layer]
#initialize weights and biases for each node
    network[layer_name] = {}
    for node in range(num_nodes):
        node_name = "node_{}".format(node+1)
        network[layer_name][node_name] = {
        
            'weights': np.around(np.random.uniform(size=num_nodes_previous), decimals=5),
            'bias' : np.around(np.random.uniform(size = 1), decimals=5)

    }

    num_nodes_preious = num_nodes
print(network)

def forward_propagate(network, inputs):
    layer_inputs = list(inputs) # start with the input layer as the input to the first hidden layer
    for layer in network:
        layer_data = network[layer]
        layer_outputs = [] 
        for layer_node in layer_data:
            node_data = layer_data[layer_node]
            # compute the weighted sum and the output of each node at the same time 
            node_output = node_activation(compute_weighted_sum(layer_inputs, node_data['weights'], node_data['bias']))
            layer_outputs.append(np.around(node_output[0], decimals=4))
            
        if layer != 'output':
            print('The outputs of the nodes in hidden layer number {} is {}'.format(layer.split('_')[1], layer_outputs))
    
        layer_inputs = layer_outputs # set the output of this layer to be the input to next layer

    network_predictions = layer_outputs
    return network_predictions

my_network = initialize_network(5, 3, [2, 3, 2], 3)
inputs = np.around(np.random.uniform(size=5), decimals=5)
predictions = forward_propagate(my_network, inputs)
print('The predicted values by the network for the given input are {}'.format(predictions))
#end
