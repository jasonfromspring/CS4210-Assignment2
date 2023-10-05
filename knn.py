#-------------------------------------------------------------------------
# AUTHOR: Jason Phan
# FILENAME: knn.py
# SPECIFICATION: LOO-CV error rate for 1NN
# FOR: CS 4210- Assignment #2
# TIME SPENT: 14 minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)


total = 0
wrong = 0
#loop your data to allow each instance to be your test set
for object in db:
    #add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]. Convert each feature value to
    # float to avoid warning messages
    #--> add your Python code here
    X = []
    for objects in db:
        if(object != objects):
            X.append([int(objects[0]), int(objects[1])])

    #transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]. Convert each
    #  feature value to float to avoid warning messages
    #--> add your Python code here
    Y = []
    for objects in db:
        if(object != objects):
            Y.append(1 if objects[2]=='+' else 2)

    #store the test sample of this iteration in the vector testSample
    #--> add your Python code here
    testSample = [[int(object[0]), int(object[1])]]

    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    #--> add your Python code here
    class_predicted = clf.predict(testSample)[0]
    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here
    if class_predicted != (1 if object[2]=='+' else 2):
        wrong += 1
    
    total += 1


print("The error rate is: "+str((wrong/total)*100)+"%")
