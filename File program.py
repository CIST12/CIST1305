counter = 0
f = open("myfile.txt", "a")
while counter < 5:
    number = (input(" input a number "))
    f.write(number)
    counter += 1
    
f = open("myfile.txt")
print(f.read())
