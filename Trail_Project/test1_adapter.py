# Patient class representing individual patient details
class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Disease: {self.disease}"


# Legacy system that manages patient records in an old way
class LegacySystem:
    def __init__(self):
        self.patients = []

    def add_patient_record(self, name, age, disease):
        self.patients.append({"name": name, "age": age, "disease": disease})

    def get_patients(self):
        return self.patients


# Adapter class to convert legacy system data to a format usable by the hospital records
class Adapter:
    def __init__(self, legacy_system):
        self.legacy_system = legacy_system

    def add_patient(self, patient):
        self.legacy_system.add_patient_record(patient.name, patient.age, patient.disease)

    def get_all_patients(self):
        records = self.legacy_system.get_patients()
        return [Patient(record["name"], record["age"], record["disease"]) for record in records]


# HospitalRecords class to manage the records of patients
class HospitalRecords:
    def __init__(self):
        self.legacy_system = LegacySystem()
        self.adapter = Adapter(self.legacy_system)

    def add_patient(self, name, age, disease):
        patient = Patient(name, age, disease)
        self.adapter.add_patient(patient)

    def show_records(self):
        patients = self.adapter.get_all_patients()
        for patient in patients:
            print(patient)


# Testing the Adapter pattern for hospital records
if __name__ == "__main__":
    hospital_records = HospitalRecords()

    # Adding records for 5 patients
    hospital_records.add_patient("Alice", 30, "Flu")
    hospital_records.add_patient("Bob", 45, "Diabetes")
    hospital_records.add_patient("Charlie", 35, "Hypertension")
    hospital_records.add_patient("David", 50, "Asthma")
    hospital_records.add_patient("Eva", 29, "Migraine")

    # Displaying all patient records
    print("Patient Records:")
    hospital_records.show_records()
