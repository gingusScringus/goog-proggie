mahasiswa = {}

mahasiswa['Budi'] = 85
mahasiswa['Siti'] = 90
mahasiswa['Andi'] = 78

print(mahasiswa)

avgScore = 0
totalScore = 0
totalIndex = 0
for i in mahasiswa:
    totalIndex += 1 # add index for each iteration
    totalScore += mahasiswa[i] # add value for each iteration

avgScore = totalScore / totalIndex # calculate average score
print("Across all three...")
print("Total Score: ", totalScore) # print total score
print("Average Score: ", format(avgScore, ",.2f")) # print average score
