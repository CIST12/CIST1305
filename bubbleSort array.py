def bubbleSort(swati):
    n = len(swati)
    swapped = False
    for i in range(n - 1):
        for j in range(0,n-i-1):
            if swati[j] > swati[j + 1]:
                swapped = True
                swati[j], swati[j + 1] = swati[j + 1], swati[j]

            if not swapped:
                return    


swati = [24,64,23,91,40,29]

bubbleSort(swati)


print("sorted array is :")
for i in range(len(swati)):
    print("% d" % swati[i],end=" ")