import os
os.system("cls" if os.name == "nt" else "clear") # clears the console by running a system command

Score = {"Student A": 100, "Student B": 85, "Student C": 95, "Student D": 88} # dictionary to store student scores

for k in Score: # iterate through the dictionary
    print(k, ":", Score[k]) # print each student and their score

totalScore = 0 # variable to store total score
totalIndex = 0 # variable to store total index

for i in Score:
    totalIndex += 1 # add index for each iteration
    totalScore += Score[i] # add value for each iteration

avgScore = totalScore / totalIndex # calculate average score
print("Across all four...")
print("Total Score: ", totalScore) # print total score
print("Average Score: ", format(avgScore, ",.2f")) # print average score

ScorePrint = ["A", "B", "C"] # list to store score categories
if avgScore >= 80:
    print("Score is ", ScorePrint[0]) # print score category A
elif avgScore >= 50 & avgScore < 80:
    print("Score is ", ScorePrint[1]) # print score category B
elif avgScore < 50:
    print("Score is ", ScorePrint[2]) # print score category C)

#don't do this btw, print it the last, use if for processing