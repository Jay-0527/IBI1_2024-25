class Patients: # class for patients
    def __init__(self, name, age, admission_date, medical_history): # define init function to initialize the attributes of the class
        self.name = name
        self.age = age
        self.admission_date = admission_date
        self.medical_history = medical_history #
    def print_details(self): # define print_details function to print the details of the patient
        print(f"Patient: {self.name}, Age: {self.age}, Last Admission: {self.admission_date}, History: {self.medical_history}") # print the details of the patient
patients = [Patients("John Smith", 45, "15/03/2025", "Hypertension, Type 2 Diabetes"),
        Patients("Sarah Johnson", 32, "22/03/2024", "Asthma, Seasonal allergies"),
        Patients("Michael Brown", 28, "10/04/2024", "None")] # create a list of patients as an example
for patient in patients:
    patient.print_details() # call the print_details function for each patient in the list
