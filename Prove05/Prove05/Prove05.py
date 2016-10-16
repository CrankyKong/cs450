from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split

import random
import sys

iris = datasets.load_iris()

class Node(object):
	def __init__(self, value, weights):
		self.value = value
		self.weight = weights

	def display(self):
		print 'Value:', self.value, ' Weights:', self.weight

def classify(classifications):
	there_can_only_be_one, maybe_this_one = 0,0
	for each_class in classifications:
		there_can_only_be_one += each_class
		if each_class == 1:
			this_one = maybe_this_one
		maybe_this_one += 1

	if there_can_only_be_one != 1:
		print 'Weights need some changing'
	else:
		print iris.target_names[this_one]


		

def predict(input_values, num_output_nodes, weights):
	#create input nodes
	input_nodes = []
	bias_node = Node(-1,weights[0])
	input_nodes.append(bias_node)
	

	for i in range(0,len(input_values)):
		new_node = Node(input_values[i], weights[i+1])
		input_nodes.append(new_node)
		
	for eachnode in input_nodes:
		eachnode.display()

	#calculate nodes
	classifications = []
	for i in range(0,num_output_nodes):
		total = 0
		for eachnode in input_nodes:
			#print eachnode.value, ' * ', eachnode.weight[i]
			total += eachnode.value * eachnode.weight[i]
			#print total
	
		if total >= 0:
			total = 1
		else:
			total = 0
		classifications.append(total)	
	print "Classification=", classifications

	classify(classifications)

	#update weights
	return weights

def create_weight_table(rows, columns):
	weight = []
	weightrow = []
	for i in range(0,rows):
		for j in range(0,columns):
			weightrow.append(float("{0:.1f}".format(random.uniform(-2,2))))
		weight.append(weightrow)
		weightrow = []
	
	print 'Weight Table'
	for x in weight:
		print x
	print '\n'
	return weight


def main(argv):
	
	
	X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target,
    test_size=0.30, random_state=12345)
	print "X_Train[0]:", X_train[0]
	print "y_Train[0]:", y_train[0]


	#the next layer of nodes is hardcoded to 3 right now
	num_output_nodes = 3
	weights = create_weight_table(len(X_train[0]) + 1, num_output_nodes)

	for values in X_train:
		weights = predict(values, num_output_nodes, weights)



if __name__ == "__main__":
    main(sys.argv)