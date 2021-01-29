# Think Python 3.14 Exercises
# Exercise 3.3

def draw_grid():
    """
    draws a grid with two rows and two columns
    """
    for i in range(0,2):
        print('+',('- '*4)[:-1],'+', ('- '*4)[:-1], '+')
        for i in range(0,5):
            print('|', ' '*7, '|', ' '*7, '|')
        #end for
    #end for
    print('+',('- '*4)[:-1],'+', ('- '*4)[:-1], '+')

    
    return None
