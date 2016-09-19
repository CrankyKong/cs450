from sklearn import datasets
iris = datasets.load_iris()

# Show the data (the attributes of each instance)
print(iris.data)

# Show the target values (in numeric format) of each instance
print(iris.target)

# Show the actual target names that correspond to each number
print(iris.target_names)

class HardCoded(object):
	def __init__(self,data,target,target_names):
		self.data = data
		self.target = target
		self.target_names = target_names
		self.training_set = []
		self.testing_set = []
		count = 0
		seventy_percent = len(self.data) * .7
		for i in self.data:
			if count < seventy_percent:
				self.training_set.append(i)
				count+=1
			else:
				self.testing_set.append(i)
		print len(self.training_set)
		print len(self.testing_set)
	
	def train(self):
		#Plays 'Eye of the Tiger'
		#Punches Hanging Meat
		#Runs up Stairs.
		#Holds hands up
		#ADRIAAAAAAN!!
		return

	def predict(self):
		predictions = []
		for i in self.testing_set:
			predictions.append(0)
		print len(predictions)
		return predictions
		
		
	
hardcoded = HardCoded(iris.data, iris.target, iris.target_names)
hardcoded.train()#CHU CHU
hardcoded.predict()