from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split

import random
import sys
# Show the data (the attributes of each instance)
#print(iris.data)

# Show the target values (in numeric format) of each instance
#print(iris.target)

# Show the actual target names that correspond to each number
#print(iris.target_names)

class KNN(object):
	def __init__(self, data):
		self.data = data
		self.X_train = []
		self.y_train = []

	def train(self, X_train, y_train):
		#Plays 'Eye of the Tiger'
		self.X_train = X_train
		self.y_train = y_train
		return True

	def predict(self):
		predictions = []
		for i in self.testing_set:
			predictions.append(0)
		return predictions

def loadFile(file_name):
    data_dir = "/Users/sburton/Dropbox/byui/classes/cs450/datasets/"
    data_file = data_dir + file_name

    data = pd.read_csv(data_file)
#print data
#print target

def main(argv):
	#filename = input("Input csv file path:")
	#loadfile(filename)
	iris = datasets.load_iris()
	
	X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target,
    test_size=0.30, random_state=12345)
	print "X_Train:", X_train
	print "X_test:", X_test
	print "y_Train:", y_train
	print "Y_test:", y_test

	for i in y_test:
		print iris.target_names[i]

	#target = iris.target
	#data = iris.data		
	#shuffled = zip(data, target)
	#random.shuffle(shuffled)
	#data, target = zip(*shuffled)

	homemadeClassifier = KNN(data)
	homemadeClassifier.train(X_train, y_train)#CHU CHU
	homemadeClassifier.predict()
	classifier = KNeighborsClassifier(n_neighbors=3)
	classifier.fit(X_train, y_train)
	predictions = classifier.predict(X_test)
	print predictions
	print y_test
	if predictions.all() == y_test.all():
		print "Match"

if __name__ == "__main__":
    main(sys.argv)