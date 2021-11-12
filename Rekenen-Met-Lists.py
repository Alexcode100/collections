list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [2,4,6,8,10,12,14,16,18,20]

def addAndDisplayLists (list1, list2):
    print('--------')

    for i in range(0,10):
        answer = list1[i] + list2[i]
        print(list1[i],' + ',list2[i],' =  ',answer)
    substractAndDisplayLists(list1,list2)

def substractAndDisplayLists (list1, list2):
    print('--------')
    for i in range(0,10):
        answer = list1[i] - list2[i]
        print(list1[i],' - ',list2[i],' =  ',answer)
    multiplyAndDisplayLists(list1,list2)

def multiplyAndDisplayLists (list1, list2):
    print('--------')

    for i in range(0,10):
        answer = list1[i] * list2[i]
        print(list1[i],' x ',list2[i],' =  ',answer)
    divideAndDisplayLists(list1,list2)
    
def divideAndDisplayLists (list1, list2):
    print('--------')
    for i in range(0,10):
        answer = list1[i] / list2[i]
        print(list1[i],' ÷ ',list2[i],' =  ',answer)

addAndDisplayLists(list1, list2)
