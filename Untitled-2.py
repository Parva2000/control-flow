def same_name(your_name, my_name):
    return your_name == my_name

def same_name(DARA, parva):
    return DARA == parva
print(same_name("DARA", "parva"))

def same_name(dara,parva):
    if dara == parva:
        return True
    else:
        return False
print(same_name("dara","parva"))

def movie_review(rating):
    if rating <= 5:
        return "Avoid at all costs!"
    elif rating < 9:
        return "this one was fun."
    else:
        return "outstanding"
print(movie_review(7))

def max_num(num1, num2,num3):
    if num1 > num2 and num1 > num3:
        return num1 
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3 
    else:
        return "It's a tie!"
print(max_num(3, 5, 7))