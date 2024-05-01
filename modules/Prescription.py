# modules/Prescription.py

class Prescription:
    @staticmethod
    def generate_prescription(user_inputs, diagnostics_results):
        # Extract relevant user inputs and diagnostics results
        age = user_inputs['age']
        current_problem = user_inputs['current_problem']
        bmi_category = diagnostics_results['bmi']
        blood_pressure_category = diagnostics_results['blood_pressure']

        # Generate prescription based on diagnosis and user input
        if age > 60 or bmi_category == 'Obese' or blood_pressure_category == 'Stage 2 Hypertension':
            prescription = f"Based on your symptoms and diagnosis, please consult a healthcare professional for further evaluation."
        else:
            prescription = f"Recommendation: {current_problem} - Follow healthy diet, exercise regularly, and monitor blood pressure."

        return prescription
