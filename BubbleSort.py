'''
# pseudocode(declaration omitted)
# myList = [4,2,8,17,9,3,7,12,34,21]
upperBound <-- 10
lowerBound <-- 1

FOR times <-- lowerBound TO upperBound
	FOR index <-- lowerBound TO upperBound - 1
		IF myList[index] > myList[index + 1] THEN
			temp <-- myList[index]
			myList[index] <-- myList[index + 1]
			myList[index + 1] <-- temp
		ENDIF
	NEXT index
NEXT times
'''
myList = [4,2,8,17,9,3,7,12,34,21]
upperBound = 9
lowerBound = 0
for times in range(len(myList)):
	for index in range(upperBound):
		if myList[index] > myList[index + 1]:
			temp = myList[index]
			myList[index] = myList[index + 1]
			myList[index + 1] = temp
print(myList)

