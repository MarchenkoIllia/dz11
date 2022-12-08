# Выводы записать в файл средствами Python

li = [6,5,4,3,2,1]

metrics = [0,0]


def bubblesort(sorted_list: list):
    for i in range(len(sorted_list)):
        for j in range(len(sorted_list)-1-i):
            metrics[0] += 1
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
                metrics[1] += 1

def SortInsert(sorting_list, start = 1):
    for i in range(start,len(sorting_list)):
        for j in range(i,0,-1):
            metrics[0] += 1
            if sorting_list[j] < sorting_list[j-1]:
                sorting_list[j], sorting_list[j-1] = sorting_list[j-1], sorting_list[j]
                metrics[1] += 1
            else:
                break

def SortShell(sorting_list):
    step = len(sorting_list) // 2
    while step > 0:
        for i in range(0,step):
            metrics[0] +=1 
            for j in range(i+step,len(sorting_list),step):
                for metrics[1] in range(j,0,-step):
                    if sorting_list[j] < sorting_list[j-step]:
                        sorting_list[j], sorting_list[j-step] = sorting_list[j-step], sorting_list[j]
                        metrics[1] +=1
                    else:
                        break
        step //= 2  
    SortInsert(li)     

def SortMerge(sorting_list):
    metrics[0] +=1
    if len(sorting_list) > 1:
        n = len(sorting_list) // 2
        leftPart = sorting_list[:n]
        rightPart = sorting_list[n:]
        SortMerge(leftPart)
        SortMerge(rightPart)
        i = j = k = 0
        while i < len(leftPart) and j < len(rightPart):
            
            if leftPart[i] < rightPart[j]:
                sorting_list[k] = leftPart[i]
                i+=1
                
            else:
                sorting_list[k] = rightPart[j]
                j+=1
                
            k+=1
        
        while i < len(leftPart):
            sorting_list[k] = leftPart[i]
            i+=1
            k+=1
            metrics[1]+=1
        while j < len(rightPart):
            sorting_list[k] = rightPart[j]
            j+=1
            k+=1
            metrics[1]+=1

def SortQuick(sorting_list, leftInd=0, rightInd=0):
    if rightInd == 0:
        rightInd = len(sorting_list)-1
    i = leftInd
    j = rightInd
    pivot = sorting_list[leftInd + (rightInd - leftInd) // 2]
    metrics[0]+=1
    while i <= j:
        while sorting_list[i] < pivot:
            i+=1
        while sorting_list[j] > pivot:
            j-=1
        if i <= j:
            sorting_list[i], sorting_list[j] = sorting_list[j], sorting_list[i]
            i+=1
            j-=1
    if leftInd < j:
        SortQuick(sorting_list, leftInd, j)
        metrics[1]+=1
    if i < rightInd:
        SortQuick(sorting_list, i, rightInd)
        metrics[1]+=1


bubblesort(li)
with open("Sort_Results.txt", mode="a+", encoding="utf8") as f:
    f.write(f"\nПузырём(худший)\nКол-во проходов {metrics[0]}\nКол-во перестановок {metrics[1]}\n")
    metrics = [0,0]
    li = [6,5,4,3,2,1]
SortInsert(li)
with open("Sort_Results.txt", mode="a+", encoding="utf8") as f:
    f.write(f"\nВставками(худший)\nКол-во проходов {metrics[0]}\nКол-во перестановок {metrics[1]}\n")
    metrics = [0,0]
    li = [6,5,4,3,2,1]
SortShell(li)
with open("Sort_Results.txt", mode="a+", encoding="utf8") as f:
    f.write(f"\nШелла(худший)\nКол-во проходов {metrics[0]}\nКол-во перестановок {metrics[1]}\n")
    metrics = [0,0]
    li = [6,5,4,3,2,1]
SortMerge(li)
with open("Sort_Results.txt", mode="a+", encoding="utf8") as f:
    f.write(f"\nСлиянием(худший)\nКол-во проходов {metrics[0]}\nКол-во перестановок {metrics[1]}\n")
    metrics = [0,0]
    li = [6,5,4,3,2,1]
SortQuick(li)
with open("Sort_Results.txt", mode="a+", encoding="utf8") as f:
    f.write(f"\nБыстрая(худший)\nКол-во проходов {metrics[0]}\nКол-во перестановок {metrics[1]}\n")
    metrics = [0,0]
    li = [6,5,4,3,2,1]