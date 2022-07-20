a = [2,45,68,9,7,3,23,10]

def bubblesort(a):
    for i in range(len(a)):
        for j in range(len(a) - 1-i):
            if a[j]>a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
        print(a)




bubblesort(a)




