# Patient class representing individual patient details
class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Disease: {self.disease}"


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


# HospitalRecords class to manage the records of patients and calculate their risks
class HospitalRecords:
    def __init__(self):
        self.patients = []

    def add_patient(self, name, age, disease):
        patient = Patient(name, age, disease)
        self.patients.append(patient)

    def calculate_risk(self, patient):
        if patient.disease == "Diabetes":
            strategy = DiabetesRiskStrategy()
        elif patient.disease == "Hypertension":
            strategy = HypertensionRiskStrategy()
        elif patient.disease == "Asthma":
            strategy = AsthmaRiskStrategy()
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
    hospital_records.add_patient("Alice", 30, "Flu")
    hospital_records.add_patient("Bob", 45, "Diabetes")
    hospital_records.add_patient("Charlie", 35, "Hypertension")
    hospital_records.add_patient("David", 50, "Asthma")
    hospital_records.add_patient("Eva", 29, "Diabetes")

    # Displaying all patient records with risk assessments
    print("Patient Records and Risk Assessments:")
    hospital_records.show_records()
