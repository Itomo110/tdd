def add(x,y):
    if type(x) == int:
        if type(y) == int:
            return x + y
        elif type(y) == str:
            raise(ValueError)
    elif type(x) == str:
        if type(y) == int:
            raise(ValueError)
        else:
            list1 = [x,y]
            answer = " ".join(list1)
            return answer



def sub(x,y):
    return x - y


def mul(x,y):
    if type(x) == int:
        if type(y) == int:
            return x*y
    
    elif type(x) == str:
        if type(y) == int:
            return x*y
        elif type(y) == float:
            return ""

    else:
        return ""