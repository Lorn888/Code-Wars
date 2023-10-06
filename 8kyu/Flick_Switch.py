# Create a function that always returns True for every item in a given list. However, if an element is the word 'flick', switch to always returning the opposite boolean value.

lst = ['codewars', 'flick', 'code', 'wars']

def flick_switch(lst):
    new=[]
    switch = 0
    for item in lst:
        if item == "flick" and switch == 0:
            switch = 1
        elif item == "flick" and switch == 1:
            switch = 0

        if switch == 0:
            new.append(True)
        elif switch == 1:
            new.append(False)
    return new