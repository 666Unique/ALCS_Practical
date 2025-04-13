'''
# pseudocode(declaration omitted)
# myList = [4,2,8,17,9,3,7,12,34,21]
upperBound <-- 9
lowerBound <-- 0
OUTPUT "Please enter item to be found"
INPUT item
found <-- FALSE
index <-- lowerBound
REPEAT
	IF item = myList[index] THEN
		found <-- TRUE
	ENDIF
	index <-- index + 1
UNTIL(found = TRUE) OR (index > upperBound)
IF found
	THEN
		OUTPUT "Item found"
	ELSE
		OUTPUT "Item not found"
ENDIF
'''
myList = [4,2,8,17,9,3,7,12,34,21]
upperBound = 9
lowerBound = 0
item = int(input("Please enter item to be found "))
found = False
index = 0
while found != True and index <= upperBound:
	if item == myList[index]:
		found = True
	index = index + 1
if found:
	print("Item found")
else:
	print("Item not found")

