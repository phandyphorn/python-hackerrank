# ======Exercise One =======
arrayWords = eval(input("Enter Word: "))
arrayCharSort = []
for word in arrayWords:
    for char in word:
        if char not in arrayCharSort:
            arrayCharSort.append(char)
arrayCharSort.sort()
print(arrayCharSort)


# ======Exercise Two =======
oldArray = eval(input("Enter List Of Nums: "))
newArray = []
def getMinimumNumber(oldArray):
    minNumber = oldArray[0]
    numberIndex = 0
    for index in range(1,len(oldArray)):
        if minNumber > oldArray[index]:
            minNumber = oldArray[index]
            numberIndex = index # position of minNumber
            # change value from minNumber to oldArray[index] because we want to find min number in the list
    return numberIndex
while oldArray: #it works when oldArray have element.
    numberIndex = getMinimumNumber(oldArray)
    newArray.append(oldArray[numberIndex])
    oldArray.pop(numberIndex)
print(newArray)


# =======Exercise Three ======
def findIndexOfSeven(array):
    for index in array:
        if index == 7:
            array.remove(index)
    return array
array = eval(input("Enter Numbers: "))
result = findIndexOfSeven(array)
print(result)


# =======Exercise Four ======
array = eval(input("Enter Numbers most 7: "))
for value in array:
    for element in range(len(value)):
        if value[element]== 7 :
            value[element] = 8
print(array)


# =======Exercise Five ======
array = eval(input("Enter number: "))
storageNumber = []
stringNum = ""
for number in array:
    if number not in storageNumber:
        storageNumber.append(number)
for num in storageNumber:
    stringNum += str(num) + " "
print(stringNum)


# =========================================

# ==========Exercise One ===========
def numberOfEight(array):
    count8 = 0
    for num in array:
        if num == 8:
            count8 += 1
    return count8
array = eval(input("Enter Nums Here: "))
result = ""
for value in array:
    isHas8 = numberOfEight(array)
    if isHas8 >= 1:
        result = isHas8
    else:
        result = "NOT FOUND"
print(result)


# ========Exercise Two ========
listOfNames = eval(input("Enter Names: "))
name = input("Enter Name: ")
index = int(input("Enter position Of index: "))
listOfNames.insert(index,name)
print(listOfNames)


# =========Exercise Three ========
numbers = eval(input("Enter Numbers: "))
oddNums = []
for index in range(len(numbers)):
    if numbers[(index*-1)-1] % 2 == 1:
        oddNums.append(numbers[(index*-1)-1])
print(oddNums)


# ==========Exercise Four ========
def splitBySpace(text):
    listOfEachWord = []
    eachWord = ""
    for word in text:
        if word == " ":
            listOfEachWord.append(eachWord)
            eachWord = ""
        else:
            eachWord += word
    if eachWord:
        listOfEachWord.append(eachWord)
    return listOfEachWord
text = input("Enter sentence: ")
print(splitBySpace(text))



# ===========Exercise Five ========
def getMinIndex(numbers):
    maxNum = numbers[0]
    for index in range(1,len(numbers)):
        if maxNum < numbers[index]:
            maxNum = numbers[index]
    return maxNum
    #find max number in numbers
numbers = eval(input("Enter Numbers: "))
for index in range(len(numbers)):
    maxNumForMinNumInNumbers = getMinIndex(numbers)
    if numbers[index] < 5:
        numbers[index] = maxNumForMinNumInNumbers
    #find min number which little than 5 to change to max number 
print(numbers)


# ===============================
# ==========Number One============
array = eval(input())
arrayTwoD = []
for value in array:
    arrayChar = []
    for element in value:
        arrayChar.append(element.upper())
    arrayTwoD.append(arrayChar)
print(arrayTwoD)

# ========Number Two===============
arrayTwoD = eval(input())
arrayOneD = []
for row in arrayTwoD:
    maxNum = row[0]
    for element in range(1,len(row)):
        if maxNum < row[element]:
            maxNum = row[element]
    arrayOneD.append(maxNum)
print(arrayOneD)

# =========Number Three =============
arrayTwoD = eval(input())
rowColShow = []
for row in range(len(arrayTwoD)):
    numbers = arrayTwoD[row]    # take each array to loop to find 7.
    for col in range(len(numbers)):
        if numbers[col] == 7:
            rowColShow.append(row)
            rowColShow.append(col)
print(rowColShow)

# ==========Number Four============
array2D = eval(input())
for row in range(len(array2D)):
    numbers = array2D[row]
    for num in range(len(numbers)):
        if numbers[num] == 7:
            numbers[num] = 8
print(array2D)

# =============================================
# ==========Number One==============
array2D = eval(input())
array1D = []
for value in array2D:
    oneWord = ""
    for element in value:
        oneWord += element
    array1D.append(oneWord.lower())
print(array1D)


# =========Number Two ===========
array2D = eval(input())
allSumOfCol = []
numberOfRows=  len(array2D)
elementInRowsButAsCol = len(array2D[0])
for col in range(elementInRowsButAsCol):
#col meam ponmarn leg vea sum bonng. Ex [2,3,4,1] so col del trov sum mean 4 dea.
    sumEachCol = 0
    for row in range(numberOfRows):
        sumEachCol += array2D[row][col]
    allSumOfCol.append(sumEachCol)
print(allSumOfCol)


# ===========Number Three===========
array2D = eval(input())
numberOfRows = len(array2D)
elementInRowsButAsCol = len(array2D[0])
arrayOfMinNum = []
for col in range(elementInRowsButAsCol):
    minNumber = array2D[0][col]
    for row in range(1,numberOfRows):
        if minNumber>array2D[row][col]:
            minNumber = array2D[row][col]
    arrayOfMinNum.append(minNumber)
print(arrayOfMinNum)


# =========Number Four==============
people = eval(input())
age = int(input())
for value in people:
    for element in value:
        if element == age:
            print(value[0])


# =========================================
# =========Number One ============
array2D = eval(input())
countOddNums = []
for value in array2D:
    countOddNum = 0
    for element in value:
        if element % 2 == 1:
            countOddNum += 1
    countOddNums.append(countOddNum)
print(countOddNums)


# ============Number Two ============
array2D = eval(input())
arrayOfAverage = []
numberOfRows = len(array2D)
numberOfColsInARow = len(array2D[0])
for cols in range(numberOfColsInARow):
    eachSumCol = 0
    eachEverage = 0
    for rows in range(numberOfRows):
        eachSumCol += array2D[rows][cols]
    eachEverage  = int(eachSumCol/numberOfRows)
    arrayOfAverage.append(eachEverage)
print(arrayOfAverage)


# ============Number Three ============
array2D = eval(input())
numberOfColumnIndex = int(input())
result = "Out of range"
numberOfRows = len(array2D)
numberOfColInARow = len(array2D[0])
for row in range(numberOfRows):
    for col in range(numberOfColInARow):
        if col == numberOfColumnIndex:
            array2D[row][col] = "*"
            result = array2D
print(result)


# =================Number Four==========
def hasMonsterOnCell(monsterPosition,cellX,cellY):
    result = False
    for num in range(len(monsterPosition)):
        if monsterPosition[num][0] == cellX and monsterPosition[num][1] == cellY:
            result = True
    return result
value = eval(input())
grid = ""
for y in range(5):
    for x in range(5):
        if hasMonsterOnCell(value,x,y):
            grid += "*"
        else:
            grid += "0"
    grid += "\n"
print(grid)

# =================================================

# =======Number One========
dictionaryOfTeachers = eval(input())
result = "No teacher here!"
averageOfAge = 0
numberOfTeachers = len(dictionaryOfTeachers)
sumAgeOfTeachers = 0
if len(dictionaryOfTeachers) > 0:
    for key in dictionaryOfTeachers:
        sumAgeOfTeachers += dictionaryOfTeachers[key]
        averageOfAge = sumAgeOfTeachers/numberOfTeachers
        result = averageOfAge
print(result)


# =======Number Two=====
arrayDictionary = eval(input())
countFruit = 0
countMeat = 0
for value in arrayDictionary:
    for key in value:
        if key == "fruit":
            countFruit += 1
        if key == "meat":
            countMeat += 1
result = ("Fruit:"+ str(countFruit) + "\n" + "Meat:" + str(countMeat))
print(result)


# =======Number Three========
def getMax(arr):
    # Write your code here
    maxNum = array[0]
    for value in array:
        if value > maxNum:
            maxNum = value
    return maxNum

def getMin(arr):
    # Write your code here
    minNum = array[0]
    for value in array:
        if value < minNum:
            minNum = value
    return minNum

def getAvg(arr):
    # Write your code here
    avgNum = (getMax(array) + getMin(array))/2
    return avgNum

# your input here
array = eval(input())
dictionaryOfMinMaxAvg = {}
dictionaryOfMinMaxAvg["max"] = int(getMax(array))
dictionaryOfMinMaxAvg["min"] = int(getMin(array))
dictionaryOfMinMaxAvg["avg"] = int(getAvg(array))
print(dictionaryOfMinMaxAvg)


# ======Number Four========
studentsData = eval(input())
result = "No result"
score = 76
if len(studentsData) > 0:
    for key in range(len(studentsData)):
        if studentsData[0]["score"] < studentsData[key]["score"]:
            result = studentsData[key]["name"]
        elif studentsData[0]["score"] > studentsData[key]["score"]:
            score = studentsData[key]["score"]
    if score < 75:
        print("The best student is " + result)
    else:
        print("The best student is " + studentsData[key]["name"])
        print("All students have more than 75")
else:
    print(result)

# ========================================================
# ===>Number one
array2D = eval(input())
columnIndex = int(input())
result = "column error"
numberOfRows = len(array2D)
countNumInCol = len(array2D[0])
if len(array2D) > 0:
    for row in range(numberOfRows):
        for col in range(countNumInCol):
            if col == columnIndex:
                array2D[row][col] = "*"
                result = array2D
print(result)

#===>Number two
array2D = eval(input())
rowIndex = int(input())
for value in range(len(array2D)):
    if value == rowIndex:
        for element in range(len(array2D[value])):
            array2D[value][element] = "*"
print(array2D)


#===>Number three
oldArray = eval(input())
result = ""
count = 0
if oldArray[-1] != "X":
    for num in range(len(oldArray)):
        if oldArray[num] == "X":
            count = num + 1
            oldArray[num] = "0"
    oldArray[count] = "X"
    result = oldArray
    print(result)
else:
    print(oldArray)


#One more way
numbers = eval(input())
isNotFoundX = True
index = 0
while isNotFoundX and index<len(numbers)-1:
    if numbers[index] == "X":
        isNotFoundX = False
        numbers[index] = "0"
        numbers[index+1] = "X"
    index += 1
print(numbers)

#===>Number Four
peopleInRoom = eval(input())
newPersonRow = int(input())
newPersonColumn = int(input())
numberOne = 0
ifNotEqual = False
for row in range(len(peopleInRoom)):
    for col in range(len(peopleInRoom[row])):
        if peopleInRoom[row][col] == 0:
            if newPersonRow == row and newPersonColumn == col:
                ifNotEqual = True
        elif peopleInRoom[row][col] == 1:
            numberOne += 1
if ifNotEqual and numberOne < 3:
    result = "CAN ADD"
else:
    result = "CANNOT ADD"
print(result)


#One more way
peopleInRoom = eval(input())
newPersonRow = int(input())
newPersonColumn = int(input())
count = 0
for value in peopleInRoom:
    for element in value:
        if element == 1:
            count += 1
if count<3 and peopleInRoom[newPersonRow][newPersonColumn] == 0:
    print("CAN ADD")
else:
    print("CANNOT ADD")


#===> Number Five
list1 = eval(input())
list2 = eval(input())
if len(list1) == len(list2):
    message = "equal"
    for num in range(len(list1)):
        if list1[num] != list2[num]:
            message = "not equal"
else:
    message = "not equal"
print(message)

#===> Number Six
# Tac toc tic
#   @param grid   (an array 2D)
#   @param rowIndex  (integer)
#   @param sign  (string)
#   @return True if the ROW at the given rowIndex is composed ONLY of the given sign
def signOnRow(grid, rowIndex, sign):
    isHasSign = True
    for i in grid[rowIndex]:
        if i != sign:
            isHasSign = False
    return isHasSign
    

#   @param grid   (an array 2D)
#   @param columnIndex  (integer)
#   @param sign  (string)
#   @return True if the ROW at the given columnIndex is composed ONLY of the given sign
def signOnCol(grid, colIndex, sign):
    # TODO !!
    isHasSign = True
    for i in range(len(grid)):
        if grid[i][colIndex] != sign:
            isHasSign = False
    return isHasSign

#   @param grid   (an array 2D)
#   @param sign  (string)
#   @return True if a DIAGONAL is composed ONLY of the given sign
def signOnDiagonal(grid, sign):
     # TODO !!   
    isHasSign = True
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if i == j and grid[i][j] != sign:
                isHasSign = False
    if not isHasSign:
        isHasSign = True
        for n in range(1,len(grid[0])+1):
            for l in range(len(grid)):
                if n-1 == l and grid[-n][l] != sign:
                    isHasSign= False
    return isHasSign
#   @param grid   (an array 2D)
#   @param sign  (string)
#   @return True if the given sign has WON
def hasSignWon(grid, sign):
    # TODO ! 
    isHasSign = False
    if signOnDiagonal(grid,sign):
        isHasSign = True
    elif not isHasSign:
        for i in range(len(grid)):
            if signOnRow(grid,i,sign):
                isHasSign = True
            if signOnCol(grid,i,sign):
                isHasSign = True
    return isHasSign
    #  It true if : 
    #  - one of the 2 diagonal is composed of this sign
    #  - or if 1 of the 3 rows is composed of this sign
    #  - or if 1 of the 3 columns is composed of this
    
    
# MAIN PROGRAM (nothing to change here !)
grid = eval(input())
if hasSignWon(grid, "A"):
    print("A WON")

elif hasSignWon(grid, "B"):
    print("B WON")

else:
    print("NO WINNER")


# =============================================
#===> Number One
names = eval(input())
namesDictionary = {}
for index in range(len(names)):
    namesDictionary[names[index]] = index
print(namesDictionary)

#===> Number Two
studentsDictionary = eval(input())
for key in studentsDictionary:
    result = "Class " + str(key) + " has " + str(studentsDictionary[key]) + " students"
    print(result)


#===> Number Three
studentsDictionary = eval(input())
newStudentsNumber= int(input())
newStudentsClass = input()
result = ""
# Enter your code here. Read input from STDIN. Print output to STDOUT
for key in studentsDictionary:
    if key == newStudentsClass:
        studentsDictionary[key] += newStudentsNumber
    result += ("Class "+ key +" has "+ str(studentsDictionary[key])+" students" + "\n")
if newStudentsClass not in studentsDictionary:
    result += ("Class "+ str(newStudentsClass) +" has "+ str(newStudentsNumber)+" students" + "\n")
print(result)


#===> Number Four
studentsDic1 = eval(input())
studentsDic2 = eval(input())
# Enter your code here. Read input from STDIN. Print output to STDOUT
for key in studentsDic1:
    if key in studentsDic2:
        studentsDic2[key] += studentsDic1[key]
studentsDic1.update(studentsDic2)
print(studentsDic1)

# One more way
dic1 = eval(input())
dic2 = eval(input())
for key in dic1:
    if key in dic2:
        dic1[key] = dic1[key] + dic2[key]
    else:
        dic1[key] = dic2[key]
print(dic1)
        
