outputFile = open('UpdatedFile.txt', "w")

inputFile = open('Repeated.txt', "r")

lines_seen_so_far = set()
print("Eliminating duplicate items......")
for line in inputFile:

    if line not in lines_seen_so_far:

        print(line)
        outputFile.write(line)
        
        lines_seen_so_far.add(line)

inputFile.close()
outputFile.close()