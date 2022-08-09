

def matrix_product(*args):
    for i in args:
        yield [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
