list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

flat_list = []
for sublist in list:
    for item in sublist:
        flat_list.append(item)
