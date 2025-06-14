inputList = [10, 20, 30, 40, 50]

totalIndex = 0
totalNilai = 0
for i in inputList:
    totalIndex += 1 # add index for each iteration
    totalNilai += i # add value for each iteration

print("Total Nilai: ", totalNilai) # print total value
print("Total rata-rata: ", totalNilai / totalIndex) # print average value
"""
basically:

iteration 1: 
totalIndex = 0 + 1 = 1
totalNilai = 0 + 10 = 10

iteration 2:
totalIndex = 1 + 1 = 2
totalNilai = 10 + 20 = 30
"""