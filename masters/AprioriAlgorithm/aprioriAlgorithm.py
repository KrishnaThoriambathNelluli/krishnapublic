import csv
import sys
from decimal import *
import itertools
from collections import Counter
finalItemSet=dict()
finalRemoveList=dict()
finalResult=dict()
def loadFile():
with open(&#39;electronics.csv&#39;) as csvfile: #Opens and reads the dataset
reader = csv.reader(csvfile)
data = list(reader)
for x in range(0,len(data)):
del data[x][0] # Removing transaction
Number from the dataset
transactionNumber = len(data) # Counts the number of
lines or number of transactions in a dataset.
return data,transactionNumber
def flatList(currentItemSet): # Function converts Array
of array list into a flat list of data [[1],[2]] =&gt; [1,2]
itemList = [([x] if isinstance(x,str) else x) for x in currentItemSet]
flatList=list(itertools.chain(*itemList)) # Helps in reading entire
string rather than a character from a string.
flatList=set(flatList) # Removes duplicate
elements from the list by using set
flatList=list(flatList) # Converting a SET to LIST
of values.
return flatList
def formatData(data): # Function used to remove
unwanted spaces in the data for a CSV file.
flatList = [item for sublist in data for item in sublist] # converts a
data into flatlist.

while &#39;&#39; in flatList:
flatList.remove(&#39;&#39;)
return flatList
def findSupportItem(supportValue,support,transactionNumber): # Function
identifies the SUPPORT% of each item.
currentItemSet=[]
currentRemoveList=[]

for key, value in supportValue.iteritems(): # Reads a
dictionary list by reading its key and value.
transactionNumber=Decimal(transactionNumber)

if ((value/transactionNumber)*100&gt;=support): #Condition to
check minimum SUPPORT %
finalItemSet[key]=value #Frequent Item
dictionary dataset
currentItemSet.append(key) # Maintains
current item data set.
else:
finalRemoveList[key]=value # Maintains
all remove list dataset
currentRemoveList.append(key) # Current item
remove list.
return finalItemSet,finalRemoveList,currentItemSet,currentRemoveList
def findSupportValue(flatListData): #find the counts of each item
counts=dict(Counter(flatListData)) # Dictionary COUNTER identifies
number of counts for each item.
return counts
def combinationListValue(currentItemSet,x): # Function helps in
identifying combinations of data
combinationList=list(itertools.combinations(currentItemSet,x)) #
Creates a list from COMBINATIONS of data.
return combinationList
def findSupportOccurances(combinationList1,data,supportOccurances): #
Finds the occurrences of subset of data for finding support values.
for x in range(0,len(data)):
for y in range(0,len(combinationList1)):
if (set(combinationList1[y]).issubset(set(data[x]))==True):
#Checks that if the current data is subset of Main Combination list
supportOccurances.append(combinationList1[y])
return supportOccurances
def calculateConfidence(finalSupportSet,confidence,mainKey,subKey): #
Fucntion to calculate % Value of confidence from a set of values.
associationList = [e for e in mainKey if e not in subKey]
if(float(finalSupportSet.get(mainKey))*100/finalSupportSet.get(subKey)&gt;=flo
at(confidence)): #To identify or filter %values with the accepted
confidence.
#print str(subKey) +&#39; -&gt; &#39;+ str(associationList) +&#39;
&#39;+str(float(finalSupportSet.get(mainKey))*100/finalSupportSet.get(subKey))

finalKey=str(subKey) +&#39; -&gt; &#39;+ str(associationList)
# Designing the data based on association rules generated.
finalConfidence=round((finalSupportSet.get(mainKey)/float(finalSupportSet.g
et(subKey)))*100,1) #Gets the data directly from Final frequent dataset
item to calculate the values
finalSupport=round((finalSupportSet.get(mainKey)/float(transactionNumber))*
100,1)
finalList=[]
finalList.append(finalSupport)
finalList.append(finalConfidence)
#Creating final list of support and confidence values.
finalResult[finalKey]=finalList

def findConfindence(finalSupportSet,confidence): # Function to
create confidence sets and identify the confidence values.
finalConfidenceList=dict()
finalSupportList=dict()
for mainKey, mainValue in finalSupportSet.iteritems(): #Iterating
finalSupportItemSet dictionary to identify the confidence.
if not isinstance(mainKey, str):
for subKey,subValue in finalSupportSet.iteritems():
#Iterating finalSupportItemSet dictionary to search for subset values to
identify the confidence,
if isinstance(subKey,str): # To
check identify whether current item is a string or a list &#39;ORANGE&#39; is a
string , [[ORANGE,APPLE]] is a list.
key=[]
key.append(subKey)
subKey=key
if(set(subKey).issubset(set(mainKey))):
calculateConfidence(finalSupportSet,confidence,mainKey,subKey[0])
else:
if(set(subKey).issubset(set(mainKey)) and subKey !=
mainKey): # Identifies the subset values for lists, and identifies
confidence set.
calculateConfidence(finalSupportSet,confidence,mainKey,subKey) # Calling
function to calculate confidence.

if __name__ == &#39;__main__&#39;:
support = input(&quot;Enter % Support\n&quot;) #Enter Support Percentage
(eg:20)
confidence=input(&quot;Enter % Confidence\n&quot;) #Enter Confidence % (eg : 50)
data,transactionNumber=loadFile() # Call function to Load
file
flatListData=formatData(data) # call function to
format Data
supportValue=findSupportValue(flatListData) #Call function identify
the SUPPORT for initial set of data.
itemSet1,removelist1,currentItemSet,currentRemoveList=findSupportItem(suppo
rtValue,support,transactionNumber) #Returning results of current Item
set.
print &quot;\nFREQUENT 1-ITEM SET &quot;
print &quot;``````````````````````&quot;

print str(currentItemSet)+&quot;\n&quot;

x=2
while True:
#Loops until the current frequent items is Zero or Null
currentItemSet=flatList(currentItemSet)
combinationList=combinationListValue(currentItemSet,x)
# Find combination list of item.
supportOccurances=[]
supportOccurances=findSupportOccurances(combinationList,data,supportOccuran
ces) # find the number of occurrences of support
datasets.
counts=findSupportValue(supportOccurances)
finalSupportSet,removelist1,currentItemSet,currentRemoveList=findSupportIte
m(counts,support,transactionNumber) # Returns value of final data set and
current data set.
print &quot;FREQUENT &quot;+str(x)+&quot;-ITEM SET &quot;
print &quot;``````````````````````````&quot;
print str(currentItemSet)+&quot;\n&quot;
if (len(currentItemSet)&lt;=1):
#If currentItemSet has no data or just one data it will exit the loop.
break
x=x+1
print &quot;\nFREQUENT ITEM SETS&quot;
print &quot;````````````````````&quot;
print str(finalSupportSet)+&quot;\n&quot;
findConfindence(finalSupportSet,confidence)
with open(&#39;output.csv&#39;, &#39;w+&#39;) as csvfile: #
Export the results in the csv file.
fieldnames = [&#39;ASSOCIATION RULE&#39;, &#39;SUPPORT&#39;,&#39;CONFIDENCE&#39;] #
Creating title of the csv file.
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()
print &quot;\n ASSOCIATION RULE &quot;
print &quot;``````````````````````&quot;

for key,value in finalResult.iteritems():
# Writes finalItemSet results to csv file.
chars_to_remove = [&#39;[&#39;, &#39;]&#39;, &quot;&#39;&quot;]
print key.translate(None, &#39;&#39;.join(chars_to_remove)) + &#39; : &#39; +
str(value)
writer.writerow({&#39;ASSOCIATION RULE&#39;: key.translate(None,
&#39;&#39;.join(chars_to_remove)), &#39;SUPPORT&#39;: value[0],&#39;CONFIDENCE&#39;: value[1]}) #
Writes data to csv file
