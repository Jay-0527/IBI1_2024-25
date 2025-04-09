def Drug_dosage_cauculator(weight,strength_of_paracetamo): #function to calculate the dosage of paracetamol based on weight and strength of paracetamo
    if weight>100 or weight<10: #checking if weight is within the range of 10-100
        print("Invalid weight")
    if strength_of_paracetamo!=120 and strength_of_paracetamo!=250: #checking if strength of paracetamo is 120 or 250
        print("Invalid strength of paracetamo")
    else: #if weight and strength of paracetamo are valid
        dose=15*weight #calculating the dosage
        volume=dose/strength_of_paracetamo #calculating the volume needed
        return f"the volume needed: {volume}ml" #returning the volume needed
print(Drug_dosage_cauculator(50,120)) #calling the function with weight=50 and strength of paracetamo=120 as an example


    