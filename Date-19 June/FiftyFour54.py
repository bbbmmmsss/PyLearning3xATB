# Calling Inner_finction & outer_function
def outer_function():
    glpbal_a=10
    def inner_function():
        b=20
        print(b)
    inner_function()
    print(glpbal_a)


outer_function()