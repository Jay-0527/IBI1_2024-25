X=1==1
Y=1>2# Set X and Y to make sure X is true and Y is false
W= X and Y
Z= X or Y#Use and ,or 
print(W)
print(Z)
# X | Y | X and Y | X or Y
# T | T | T       | T
# T | F | F       | T
# F | T | F       | T
# F | F | F       | F