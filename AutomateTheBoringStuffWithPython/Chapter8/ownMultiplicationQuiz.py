import random, time, datetime
numberOfQuestions = 10
correctAnswers = 0
for questionsNumber in range(numberOfQuestions):
    # Pick two random numbers:
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt = "#%s: %s x %s = " % (questionsNumber, num1,num2)
    print(prompt)
    userinput = input()
    #print(time.monotonic())
    startTime = time.process_time()

    numberOfTries = 0
    try:
        age = int(userinput)
    except:
        print("Please input an int number.")
    endTime = time.process_time()
    timespan = endTime-startTime
    print(timespan)
    if timespan>8.0:
        print("Out of time!")
    else:
        # This block runs if no exception were raised in the try block.
        print("Correct!")
        correctAnswers+=1

    time.sleep(1) #Brief pause to let user see the result.
print("Score: %s / %s" % (correctAnswers, numberOfQuestions))
