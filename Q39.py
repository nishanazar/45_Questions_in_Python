def average(lst: list[int]):
    avarage_cal = 0 
    for  i in lst:
        avarage_cal += i
    print(avarage_cal / len(lst))
    

average([10,30,40,50])
