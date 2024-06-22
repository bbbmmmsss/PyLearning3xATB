# we can change the list name by using index(0 ,1, 3, 4) index value

name=['Bhagyashree','Vishakha','Rani','Rohit']
def change(name):
    name[1]='Deepali'
    name[0]='Mahesh'
    return name

change(name)
print(change(name))