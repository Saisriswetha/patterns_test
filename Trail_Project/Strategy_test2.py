# Patient class representing individual patient details
class Patient:
    def __init__(self, name, age, disease,gender):
        self.name = name
        self.age = age
        self.disease = disease
        self.gender= gender

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Disease: {self.disease}, Gender:{self.gender}"


# Strategy interface for risk calculation
class RiskStrategy:
    def calculate_risk(self, patient):
        raise NotImplementedError("This method should be overridden by subclasses.")


# Concrete strategy for calculating risk for diabetes
class DiabetesRiskStrategy(RiskStrategy):
    def calculate_risk(self, patient):
        if patient.age > 40:
            return "High risk for complications."
        return "Moderate risk."
    
 #Added by Shivasai for calculating the risk for cancer

class Cancersymptoms:
    def __init__(self, fever, headaches, lumps, sleep_loss ):
        self.fever = fever
        self.headaches = headaches
        self.lumps = lumps
        self.sleep_loss= sleep_loss
    def count_symptoms(self):
        return sum([self.fever,self.headaches,self.lumps,self.sleep_loss])
  
class CancerRiskStartegy(RiskStrategy):
    def __init__(self, symptoms:Cancersymptoms):
        self.symptoms=symptoms

    def calculate_risk(self, patient):
        if self.symptoms.count_symptoms()>2 and patient.age > 18:
            if patient.gender=="Female":
                return "There is risk of Breast Cancer -- Please take precaution"
            elif patient.gender=="Male":
                return "There is risk of Cervical Cancer -- Please take precaution"
        return "Risk level uncertain - consider further screening."
 
# Concrete strategy for calculating risk for hypertension
class HypertensionRiskStrategy(RiskStrategy):
    def calculate_risk(self, patient):
        if patient.age > 50:
            return "High risk of heart disease."
        return "Low to moderate risk."


# Concrete strategy for calculating risk for asthma
class AsthmaRiskStrategy(RiskStrategy):
    def calculate_risk(self, patient):
        if patient.age < 30:
            return "Low risk."
        return "Moderate risk due to age."

#Added by Chetan Chhetri ___ the calculation for heart attack risk   
class HeartAttackRisk(RiskStrategy):
    def __init__(self,diabetes_cal):
        self.diabetes_cal=diabetes_cal
    def calculate_risk(self, patient):
        d_risk=self.diabetes_cal.calculate_risk(patient)
        if patient.age > 20  and d_risk=="High risk for complications.":
            return "Prone to heart attack"
        return super().calculate_risk(patient)


# HospitalRecords class to manage the records of patients and calculate their risks
class HospitalRecords:
    def __init__(self):
        self.patients = []

    def add_patient(self, name, age, disease,gender,symptoms=None):
        patient = Patient(name, age, disease,gender,symptoms)
        self.patients.append(patient)

    def calculate_risk(self, patient):
        if patient.disease == "Diabetes":
            strategy = DiabetesRiskStrategy()
        elif patient.disease == "Hypertension":
            strategy = HypertensionRiskStrategy()
        elif patient.disease == "Asthma":
            strategy = AsthmaRiskStrategy()
        elif patient.disease=="Heart Attack":
            strategy= HeartAttackRisk(DiabetesRiskStrategy())
        elif patient.disease=="Cancer" and patient.symptoms:
            strategy=CancerRiskStartegy(patient.symptoms)
        else:
            return "Risk calculation not available for this disease."

        return strategy.calculate_risk(patient)

    def show_records(self):
        for patient in self.patients:
            risk = self.calculate_risk(patient)
            print(f"{patient} | Risk Assessment: {risk}")


# Testing the Strategy pattern for hospital records
if __name__ == "__main__":
    hospital_records = HospitalRecords()

    # Adding records for 5 patients
    hospital_records.add_patient("Alice", 30, "Flu", "Female")
    hospital_records.add_patient("Bob", 45, "Diabetes", "Male")
    hospital_records.add_patient("Charlie", 35, "Hypertension", "Male")
    hospital_records.add_patient("David", 50, "Asthma", "Male")
    hospital_records.add_patient("Eva", 29, "Cancer", "Female", Cancersymptoms(fever=1, headaches=0, lumps=1, sleep_loss=1))
    hospital_records.add_patient("Helen", 65, "Heart Attack", "Female")
    hospital_records.add_patient("Mike", 55, "Cancer", "Male", Cancersymptoms(fever=0, headaches=1, lumps=1, sleep_loss=1))

    # Displaying all patient records with risk assessments
    print("Patient Records and Risk Assessments:")
    hospital_records.show_records()
