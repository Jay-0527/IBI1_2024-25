class Patient:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def bmi(self):
        bmi = self.weight / (self.height/100)**2
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi <= 25:
            return "Healthy"
        elif bmi>25:
            return "Overweight"
        
#Example usage
p1 = Patient("John", 25, 175, 70)
print(p1.bmi()) # Output: Healthy
    