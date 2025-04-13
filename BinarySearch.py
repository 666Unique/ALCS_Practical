'''
# pseudocode(declaration omitted)
# myList = [2, 3, 4, 7, 8, 9, 12, 17, 21, 34] # must be sorted first
upperBound <-- 9
lowerBound <-- 0
OUTPUT "Please enter item to be found"
INPUT item
found <-- FALSE
REPEAT
	index <-- INT((upperBound + lowerBound)/2)
	IF item = myList[index] 
		THEN
			found <-- TRUE
	ENDIF
	IF item > myList[index] 
		THEN
			lowerBound <-- index + 1
	ENDIF
	IF item < myList[index] 
		THEN
			upperBound <-- index - 1
	ENDIF
UNTIL(found = TRUE) OR (lowerBound > upperBound)
IF found
	THEN
		OUTPUT "Item found"
	ELSE
		OUTPUT "Item not found"
ENDIF
'''
myList = [2, 3, 4, 7, 8, 9, 12, 17, 21, 34]
upperBound = 9
lowerBound = 0
item = int(input("Please enter item to be found "))
found = False
while found != True and lowerBound <= upperBound:
	index = int((lowerBound + upperBound)/2)
	if item == myList[index]:
		found = True
	if item > myList[index]:
		lowerBound = index + 1
	if item < myList[index]:
		upperBound = index - 1
if found:
	print("Item found")
else:
	print("Item not found")

