start = 5
endno = 10000

def lucas_lehmer(start):
    my_list=[4]
    value=2**start-1
    lucas=4
    for val in range(1, start - 1):
        lucas = ((lucas*lucas)-2) % value
        my_list.append(lucas)
    if lucas == 0:
        print("prime", value)
        print("")


while start <= endno:
    lucas_lehmer(start)
    start+=1