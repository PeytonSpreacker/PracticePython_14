import random

lst = list()
set = set()

list1 = random.sample(range(0,101), 10)
list2 = random.sample(range(0,101), 10)

def list_overlap():
    for i in list1:
        if i in list2:
            lst.append(i)
        else:
            continue
    if len(lst) > 0:
        print(lst)
    else:
        print('No overlaps.')

def set_generation():
    for i in list1:
        if i in list2:
            set.add(i)
        else: continue
    if len(set) > 0:
        print(set)
    else: print('No Overlaps')
    
def list_to_set():
    for i in list1:
        if i in list2:
            lst.append(i)
        else:
            continue
    for i in lst:
        set.add(i)
    if len(set) > 0:
        print(set)
    else: print('No Overlaps')

# list_overlap()
# set_generation()
list_to_set()