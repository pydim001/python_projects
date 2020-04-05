import random
import time

av = []

def scramble():     #Creates a scramble for the Rubik's cube
    em = ""
    scramble = ["R2 ", "U2 ", "B2 ", "L2 ", "F2 ", "D2 ", "R ", "U ", "B ", "L ", "F ", "D ", "R' ", "U' ", "L' ", "F' ", "D' ", "B' "]
    ran = random.randint(0, len(scramble) - 1)
    for length in range(20):
        em = em + scramble[ran]
        ran = random.randint(0, len(scramble) - 1)
    return em

def average(array):     #function to print the average time
    sum = 0
    for tim in array:
        sum += tim
    return sum/(len(array))

while True:
    print(scramble(), "\n")     #prints scramble
    input("Press ENTER to start stopwatch")
    begin = time.time()     #begins time
    input("Press ENTER to stop stopwatch")
    end = time.time()    #stops time
    el = round(end - begin, 2)
    av.append(el)   #Makes a list of all times
    print(el)
    print("Average: ", round(average(av), 2), "\n")


