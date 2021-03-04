# Using readlines()
bKeyFile = open('csvFiles/bKey.csv', 'r')
lines = bKeyFile.readlines()
 
# counter
count = 0

# Strips the newline character
for line in lines:
    count += 1
    loLine = line.split("=")
    
    if len(loLine) != 2:
        print("Uh oh")
    
print(len(lines))