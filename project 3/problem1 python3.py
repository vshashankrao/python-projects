'''Shashank Rao
RUID: 185005733
'''

def replace_element(L, oldel, newel):
    #replaces selected element in list and returns every instance of said element
    if len(L) == 1:
        if L[0] == oldel:
            L[0] = newel
        return L
    else:
        L = replace_element(L[:len(L)-1], oldel, newel) + replace_element(L[len(L)-1:], oldel, newel)
        return L
    

def num_double_letters(astr):
    #counts the number of times there are double letters
    if len(astr) < 2:
        return 0
    else:
        if astr[0] == astr[1]:
            return num_double_letters(astr[1:]) + 1
        else:
            return num_double_letters(astr[1:])
def has_repeats(L):
    #counts the number of times the list repeats
    if len(L) < 2:
        return False
    else:
        if L[0] == L[1]:
            return True
        else:
            if len(L) != 2:
                temp_L = L[0:1] + L[2:]
                if(has_repeats(temp_L)):
                    return True
                else:
                    temp_L = L[1:]
                    if(has_repeats(temp_L)):
                        return True
                    else:
                        return False
            else:
                return False
            
