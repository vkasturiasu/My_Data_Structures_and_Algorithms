#Start from the beginning and proceed inorder to create a sorted array
a = [101,5,2,6,7,8,5,100]
def insertion_sort(a):
    for i in range(len(a)):
        temp = a.pop(i)
        j = i-1
        while j>=0 and a[j] > temp:
           j = j-1
        a.insert(j+1,temp)
        print(a)

insertion_sort(a)

