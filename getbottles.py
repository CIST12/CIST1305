" The main function"
def main():
    totalBottles = getBottles()
    print(totalBottles * 10)

def getBottles():
    total = int(input("How many bottles? "))
    return total

main()
