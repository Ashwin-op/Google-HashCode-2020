# More Pizza
# Solution for the Practice Round of Google Hash Code 2020
# 17-FEB-2020


def solve(MAX, inputList):
    solutionIndexList = []  # To store the best solution indexes
    solutionValueList = []  # To store the best solution values
    currentIndexList = []  # To store the current solution indexes
    currentValueList = []  # To store the current solution values

    fullSize = len(inputList)

    maxScore = 0  # Stores the maximum score achieved

    startIndex = fullSize  # Stores the index from where the solution generation should start

    sum = 0

    # Solution generating starts from the last element of the inputList
    # If first element of currentIndexList becomes 0 that means solution generating is finished

    while (len(currentIndexList) > 0 and currentIndexList[0] != 0) or len(currentIndexList) == 0:

        startIndex = startIndex - 1

        for i in range(startIndex, -1, -1):  # Used to traverse from end to start of the inputList
            currentValue = inputList[i]

            tempSum = sum + currentValue

            if tempSum == MAX:  # If the temporary sum is equal to target that means the perfect solution is found
                sum = tempSum
                currentIndexList.append(i)  # Add current Pizza index to the solution
                currentValueList.append(currentValue)  # Add current Pizza value to the solution
                break

            elif tempSum > MAX:  # If the temporary sum is greater than target
                continue  # Try next value

            elif tempSum < MAX:  # If the temporary sum is lesser than target
                sum = tempSum
                currentIndexList.append(i)  # Add current Pizza index to the solution
                currentValueList.append(currentValue)  # Add current Pizza value to the solution
                continue  # Try next value

        if maxScore < sum:  # If currently generated solution has the best score
            maxScore = sum  # Save its value

            solutionIndexList = []
            solutionValueList = []

            for i in currentIndexList:
                solutionIndexList.append(i)  # Save the current best solution indexes
            for i in currentValueList:
                solutionValueList.append(i)  # Save the current best solution values

        if maxScore == MAX:  # If current solution is the perfect solution, stop
            break

        if len(currentValueList) != 0:
            lastVal = currentValueList.pop()  # Remove the last element from current values
            sum = sum - lastVal  # Subtract it from sum

        if len(currentIndexList) != 0:
            lastIndex = currentIndexList.pop()  # Remove the last element from current indexes
            startIndex = lastIndex  # Make it as the starting index for the next iteration

        if len(currentIndexList) == 0 and (startIndex == 0):  # If solution generating is finished, stop
            break

    solutionIndexList.reverse()  # Reverse the indexes list to ascending order

    return solutionIndexList  # Return indexes list of the best solution


def process(fileName):
    print("\n\n-----------------------")
    print(fileName)
    print("-----------------------")

    #  Open the file
    inputFile = open(inputDir + fileName + ".in", "rt")

    #  Read file
    firstLine = inputFile.readline()
    secondLine = inputFile.readline()
    inputFile.close()

    #  Print input data
    print("Input:")
    print(firstLine, secondLine)

    #  Assign parameters
    MAX, NUM = list(map(int, firstLine.split()))

    #  Create the pizza list by reading the file
    inputList = list(map(int, secondLine.split()))

    outputList = solve(MAX, inputList)  # Solve the problem and get output

    #  Print output data and create output file
    print("Output:")

    outputString = ""
    for i in outputList:
        outputString = outputString + str(i) + " "
    print(outputString)
    print("Length of Output: " + str(len(outputList)))

    outputFile = open(outputDir + fileName + ".out", "w")
    outputFile.write(str(len(outputList)) + "\n")
    outputFile.write(outputString)
    outputFile.close()


inputDir = "Input/"
outputDir = "Output/"

fileNames = ["a_example", "b_small", "c_medium", "d_quite_big", "e_also_big"]

for fileName in fileNames:  # Solve for each file
    process(fileName)
