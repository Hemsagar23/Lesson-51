with open('Codingal.txt', 'w') as file:
    file.write("Hi! I am Penguin and I am 1 yr old. \n Hello everyone. \nWelcome to Codingal")

with open('Codingal.txt', 'r') as file:
    data = file.readlines()
    print(data)
    print("Words in this file are....")
    for line in data:
        word = line.split()
        print(word)