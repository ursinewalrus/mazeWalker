import Cell as C
import numpy as np
import math
def fontViewProto(object,distance):  
	distance = min(5,distance)

def compressRow(row,distance):#compresses along row or X axis only
	originalLen = len(row)
	newRow = ''
	lastChar = ''
	currentChar = ''
	sequential = 1
	for char in row:
		lastChar = currentChar
		currentChar = char
		if lastChar == currentChar:
			sequential += 1
		elif sequential>1:
			trimmed = int(sequential*(1-(distance*.2)))# for each increment of distance, shrink by 1/5th
			newRow += lastChar*trimmed
			sequential = 1
		else:
			newRow+=lastChar
	if sequential>1 or currentChar!=lastChar:  #got to end and last char part of sequentail string and needs to be added OR last char is non sequential and needs adding
		trimmed = int(round(math.ceil((sequential*(1-(distance*.2)))),1))# for each increment of distance, shrink by 1/5th
		newRow += currentChar*trimmed
	padding = int((originalLen - len(newRow))/2)
	newRow = list(newRow)
	newRow =  np.lib.pad(newRow,(padding,padding),'constant',constant_values=(0,0))#padding with empty string
	newRow = [' ' if x=='' else x for x in newRow]
	return newRow

def resizer(cellView,distance):
	xShrunk = []
	yShunk = []
	# compressRow(cellView[1],distance)
	# die()
	for row in cellView:
		newRow = compressRow(row,distance)
		xShrunk.append(newRow)
	xShrunk = np.rot90(xShrunk)#rotate 90 to allow vertical squash
	for row in xShrunk:
		yShunk.append(compressRow(row,distance))
	resized = np.rot90(yShunk,3)#rotate 270 to get back to original position
	return resized

# print fontViewProto(cell,3)
# 15 spaces, 50 #
# print ("               ##################################################\n"*25)[:-1]
# print ("               ##################################################\n"*25)[:-2]
#View / BaseCell
#50 wide at 0
#25 tall

#40 wide at 1
#20 tall

#30 wide at 2
#15 tall

#20 wide at 3
#10 tall

#10 wide at 4
#5 tall

#0 wide at 5 + 
#0 tall


cell = C.Cell()
cellView = cell.baseShapeAt0
# print "BEFORE"
for row in cellView:
	print ''.join(c for c in row)
shrunk  = resizer(cellView,3)
for row in shrunk:
	print ''.join(c for c in row)


