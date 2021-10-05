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


