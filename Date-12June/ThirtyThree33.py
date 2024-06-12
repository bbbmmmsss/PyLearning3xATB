# Loop

# Ther are 3 Types of loops in python
# 1. for loop
# 2. while loop
# 3. do while loop

# 1. For Loop
for i in range(3):
    print("Hello")

for i in  range(2,6):
    print(i)
#
# -------------------------------------------------
# Print odd number
for i in range(1, 10, 2):
    print(i)
# ---------------------------------------------
# 2. while loop
i = 0
while i < 3:
    print(i)
    # i += 1
    i=i+1

# ---------------------------------------
# 3. do while loop
i = 0
while True:
    print("xyz")
    i += 1
    if i == 3:
        break