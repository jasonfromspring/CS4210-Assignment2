#-------------------------------------------------------------------------
# AUTHOR: Jason Phan
# FILENAME: decision_tree_2.py
# SPECIFICATION: View performance of contact lens training and test
# FOR: CS 4210- Assignment #2
# TIME SPENT: 1 hr
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']
X = []
Y = []

for ds in dataSets:

    dbTraining = []
    

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)


    #transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    # so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    # X =

    #Age: Young = 1, Prepresbyopic = 2, Presbyopic = 3
    #SP: myope = 1, hypermetrope = 2
    #AST: yes = 1, no = 2
    #TPR: Normal = 1, Reduced = 2

    for object in dbTraining:
        row = []
        col=0
        for value in object:
            if col== 0:
                if value == 'Young':
                    row.append(1)
                elif value == 'Prepresbyopic':
                    row.append(2)
                else:
                    row.append(3)
            elif col == 1:
                if value == 'Myope':
                    row.append(1)
                else:
                    row.append(2)
            elif col == 2:
                if value == 'Yes':
                    row.append(1)
                else:
                    row.append(2)
            elif col == 3: 
                if value == 'Normal':
                    row.append(1)
                else:
                    row.append(2)
            col=col+1
        X.append(row)



    #transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    for object in dbTraining:
        val = object[-1]
        if val == 'Yes':
            Y.append(1)
        else:
            Y.append(2)


#read the test data and add this data to dbTest
    #--> add your Python code here
dbTest = []

with open('contact_lens_test.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0: #skipping the header
                dbTest.append (row)

#loop your training and test tasks 10 times here
sums = []
for i in range (10):

    #fitting the decision tree to the data setting max_depth=3
    clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
    clf = clf.fit(X, Y)

    
    correct = 0
    count = 0
    for data in dbTest:
        count += 1
        row = []
        col=0
        for value in data:
            if col== 0:
                if value == 'Young':
                    row.append(1)
                elif value == 'Prepresbyopic':
                    row.append(2)
                else:
                    row.append(3)
            elif col == 1:
                if value == 'Myope':
                    row.append(1)
                else:
                    row.append(2)
            elif col == 2:
                if value == 'Yes':
                    row.append(1)
                else:
                    row.append(2)
            elif col == 3: 
                if value == 'Normal':
                    row.append(1)
                else:
                    row.append(2)
            col=col+1

        val = data[-1]
        if val == 'Yes':
            real = 1
        else:
            real = 2

        
        #transform the features of the test instances to numbers following the same strategy done during training,
        #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
        #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
        #--> add your Python code here
        class_predicted = clf.predict([row])[0]
        
        if class_predicted==real:
            correct += 1
        #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
        #--> add your Python code here
    sums.append(correct)
    correct = 0

#find the average of this model during the 10 runs (training and test set)
#--> add your Python code here
average = sum(sums)/len(sums)
average = average / count


#print the average accuracy of this model during the 10 runs (training and test set).
#your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
#--> add your Python code here

print("Final accuracy when training: "+str(average))