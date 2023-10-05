#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv
dbTraining = []

#reading the training data in a csv file
with open('weather_training.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         dbTraining.append (row)

#transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
X = []
for object in dbTraining:
        row = []
        col=0
        for value in object:
            if col==1:
                if value == 'Sunny':
                    row.append(1)
                elif value == 'Overcast':
                    row.append(2)
                else:
                    row.append(3)
            elif col == 2:
                if value == 'Hot':
                    row.append(1)
                elif value == 'Mild':
                    row.append(2)
                else:
                    row.append(3)
            elif col == 3:
                if value == 'High':
                    row.append(1)
                else:
                    row.append(2)
            elif col == 4: 
                if value == 'Strong':
                    row.append(1)
                else:
                    row.append(2)
            col=col+1
        X.append(row)  

#transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]

Y = []
for object in dbTraining:
  val = object[-1]
  if val == 'Yes':
    Y.append(1)
  else:
    Y.append(2)

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the test data in a csv file
dbTest = []
with open('weather_test.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         dbTest.append (row)

#printing the header os the solution
print('[Day | Outlook | Temperature | Humidity | Wind | PlayTennis Confidence]')

#use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
#--> add your Python code here
for object in dbTest:
        row = []
        col=0
        for value in object:
            if col==1:
                if value == 'Sunny':
                    row.append(1)
                elif value == 'Overcast':
                    row.append(2)
                else:
                    row.append(3)
            elif col == 2:
                if value == 'Hot':
                    row.append(1)
                elif value == 'Mild':
                    row.append(2)
                else:
                    row.append(3)
            elif col == 3:
                if value == 'High':
                    row.append(1)
                else:
                    row.append(2)
            elif col == 4: 
                if value == 'Strong':
                    row.append(1)
                else:
                    row.append(2)
            col=col+1
        prediction = clf.predict_proba([row])[0]
        if(max(prediction)>=0.75):
            if(prediction[0]>prediction[1]):
                row.append("No - Confidence "+str(prediction[0]))
            else:
                row.append("Yes - Confidence "+str(prediction[1]))
            print(row)
        


