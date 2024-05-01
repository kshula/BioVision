from modules.Language import Language
from modules.Diagnostics import HealthDiagnosticsTool
from modules.Prescription import Prescription
from modules.helpers import about, disclaimer
import time
import random

class BioVision:
    def __init__(self):
        pass

    def get_user_inputs(self):
        # Loading
        print("Welcome to BioVision")
        print(about)
        print("Information Request")
        print("To proceed with the health assessment:")
        
        # Prompt user for basic demographic info
        age = int(input("Enter your age: "))
        height = random.uniform(1.5, 2.0)  # Randomize height between 1.5m to 2.0m
        weight = random.uniform(50, 100)   # Randomize weight between 50kg to 100kg
        gender = input("Enter your gender (Male/Female): ").lower()
        cardio = random.choice(["Yes", "No"])  # Randomize cardio condition (Yes/No)
        current_problem = input("Enter your current health problem or symptom: ")

        # Calculate BMI
        bmi = weight / (height ** 2)

        # Prepare user inputs as a dictionary
        user_inputs = {
            'age': age,
            'height': height,
            'weight': weight,
            'gender': gender,
            'cardio': cardio,
            'current_problem': current_problem,
            'bmi': bmi
        }

        return user_inputs

    def start(self):
        print("Initializing BioVision Health Diagnostics Tool...")
        time.sleep(2)  # Simulate initialization delay
        print("Booting up... Please wait.")
        time.sleep(2)  # Simulate booting process
        print("Accessing patient database...")
        time.sleep(2)  # Simulate database access
        print("Connecting to diagnostic servers...")
        time.sleep(2)  # Simulate server connection
        print("\nBioVision is ready to assist you!\n")   

        # Get user inputs
        user_inputs = self.get_user_inputs()

        # Use Diagnostics module
        diagnostics_tool = HealthDiagnosticsTool()

        # Simulate random blood test results (for demonstration purposes)
        blood_tests = {
            'total_cholesterol': random.randint(150, 250),
            'hdl_cholesterol': random.randint(30, 70),
            'ldl_cholesterol': random.randint(80, 150),
            'triglycerides': random.randint(50, 200),
            'hemoglobin': random.uniform(12, 16),
            'red_blood_cells': random.uniform(4, 6),
            'white_blood_cells': random.uniform(4, 10),
            'platelets': random.uniform(150, 400),
            'vitamin_d': random.uniform(20, 40),
            'vitamin_b12': random.uniform(150, 600),
            'folate': random.uniform(2, 20),
            'blood_pressure_systolic': random.randint(100, 160),
            'blood_pressure_diastolic': random.randint(60, 100)
        }

        # Combine user inputs and blood test results into a single dictionary
        patient_data = {**user_inputs, **blood_tests}

        # Add combined data to diagnostics tool
        diagnostics_tool.add_patient_data(**patient_data)

        # Run diagnostics
        print(disclaimer)
        diagnostics_tool.run_diagnostics()
        diagnostics_results = diagnostics_tool.results

        # Generate prescription based on diagnostics results and user input
        prescription = Prescription.generate_prescription(user_inputs, diagnostics_results)

        # Return diagnosis results and prescription
        return diagnostics_results, prescription

if __name__ == "__main__":
    biovision = BioVision()
    diagnosis_results, prescription = biovision.start()

    # Display diagnosis results
    print("\nDiagnostics Results:")
    for analysis_type, result in diagnosis_results.items():
        print(f"- {analysis_type.capitalize()}: {result}")

    # Display prescription
    print(f"\nPrescription: {prescription}")
