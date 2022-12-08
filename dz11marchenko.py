# from sort_best import bubblesort,SortInsert,SortMerge,SortQuick,SortShell,li,metrics

# bubblesort(li)
# with open("Sort_Results.txt", mode="w", encoding="utf8") as f:
#     f.write(f"Пузырём(лучший)\nКол-во проходов {metrics[0]}\nКол-во перестановок {metrics[1]}\n")
#     metrics = [0,0]
# SortInsert(li)
# with open("Sort_Results.txt", mode="a+", encoding="utf8") as f:
#     f.write(f"\nВставками(лучший)\nКол-во проходов {metrics[0]}\nКол-во перестановок {metrics[1]}\n")
#     metrics = [0,0]
# SortShell(li)
# with open("Sort_Results.txt", mode="a+", encoding="utf8") as f:
#     f.write(f"\nШелла(лучший)\nКол-во проходов {metrics[0]}\nКол-во перестановок {metrics[1]}\n")
#     metrics = [0,0]
# SortMerge(li)
# with open("Sort_Results.txt", mode="a+", encoding="utf8") as f:
#     f.write(f"\nСлиянием(лучший)\nКол-во проходов {metrics[0]}\nКол-во перестановок {metrics[1]}\n")
#     metrics = [0,0]
# SortQuick(li)
# with open("Sort_Results.txt", mode="a+", encoding="utf8") as f:
#     f.write(f"\nБыстрая(лучший)\nКол-во проходов {metrics[0]}\nКол-во перестановок {metrics[1]}\n")
#     metrics = [0,0]

with open("Sort_Results.txt", mode="a+", encoding="utf8") as f:
    f.write("елси список не большой , и мало времени, можно использовать метод пузыря. метод вставками лучше применять для лучшего варианта, а Шелла для среднего и худшего. Быстрая сортировка является наиболее эффективным из всех вышеперечисленных решений.")