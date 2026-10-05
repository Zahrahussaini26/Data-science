values= [12, -5, 0, 7, -3, 0, 18, -1]
positive_values=[]
Negative_values=[]
zero_values=[]
for value in values:
    if value>0:
        positive_values.append(value)
    elif value<0:
        Negative_values.append(value)
    else:
        Negative_values.append(value)
print("Postive values: ", positive_values)
print("Negative values: ", Negative_values)
print("zero values: ", zero_values)



