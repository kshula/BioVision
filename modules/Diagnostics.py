# modules/Diagnostics.py

class HealthDiagnosticsTool:
    def __init__(self):
        self.patient_data = {}
        self.results = {}

    def add_patient_data(self, **kwargs):
        self.patient_data.update(kwargs)

    def run_diagnostics(self):
        # Extract patient data
        age = self.patient_data.get('age', None)
        height = self.patient_data.get('height', None)
        weight = self.patient_data.get('weight', None)
        bmi = self.calculate_bmi(height, weight)

        fasting_glucose = self.patient_data.get('fasting_glucose', None)
        lipid_profile = {
            'total_cholesterol': self.patient_data.get('total_cholesterol', None),
            'hdl_cholesterol': self.patient_data.get('hdl_cholesterol', None),
            'ldl_cholesterol': self.patient_data.get('ldl_cholesterol', None),
            'triglycerides': self.patient_data.get('triglycerides', None)
        }
        blood_cell_counts = {
            'hemoglobin': self.patient_data.get('hemoglobin', None),
            'red_blood_cells': self.patient_data.get('red_blood_cells', None),
            'white_blood_cells': self.patient_data.get('white_blood_cells', None),
            'platelets': self.patient_data.get('platelets', None)
        }
        nutritional_status = {
            'vitamin_d': self.patient_data.get('vitamin_d', None),
            'vitamin_b12': self.patient_data.get('vitamin_b12', None),
            'folate': self.patient_data.get('folate', None)
        }

        blood_pressure = {
            'blood_pressure_systolic': self.patient_data.get('blood_pressure_systolic', None),
            'blood_pressure_diastolic': self.patient_data.get('blood_pressure_diastolic', None),
        }

        # Perform diagnostics
        self.results['bmi'] = self.categorize_bmi(bmi)
        self.results['blood_glucose'] = self.categorize_blood_glucose(fasting_glucose)
        self.results['lipid_profile'] = self.analyze_lipid_profile(**lipid_profile)
        self.results['blood_cell_counts'] = self.analyze_blood_cell_counts(**blood_cell_counts)
        self.results['nutritional_status'] = self.analyze_nutritional_status(**nutritional_status)
        self.results['blood_pressure'] = self.categorize_blood_pressure(**blood_pressure)

    def calculate_bmi(self, height, weight):
        if height is not None and weight is not None:
            return weight / (height ** 2)
        return None

    def categorize_bmi(self, bmi):
        if bmi is not None:
            if bmi < 18.5:
                return "Underweight"
            elif 18.5 <= bmi < 25:
                return "Normal weight"
            elif 25 <= bmi < 30:
                return "Overweight"
            else:
                return "Obese"
        return "Unknown"

    def categorize_blood_glucose(self, fasting_glucose):
        if fasting_glucose is not None:
            if 70 <= fasting_glucose <= 100:
                return "Normal Fasting Blood Glucose"
            elif 100 <= fasting_glucose <= 125:
                return "Prediabetes (Impaired Fasting Glucose)"
            elif fasting_glucose >= 126:
                return "Diabetes (Fasting Hyperglycemia)"
        return "Unknown"

    def analyze_lipid_profile(self, total_cholesterol, hdl_cholesterol, ldl_cholesterol, triglycerides):
        if all(val is not None for val in [total_cholesterol, hdl_cholesterol, ldl_cholesterol, triglycerides]):
            if total_cholesterol < 200 and hdl_cholesterol >= 40 and triglycerides < 150:
                return "Normal lipid profile"
            elif total_cholesterol >= 240 or ldl_cholesterol >= 160:
                return "High cholesterol levels, increased cardiovascular risk"
            else:
                return "Borderline lipid profile, further evaluation recommended"
        return "Unknown"

    def analyze_blood_cell_counts(self, hemoglobin, red_blood_cells, white_blood_cells, platelets):
        if all(val is not None for val in [hemoglobin, red_blood_cells, white_blood_cells, platelets]):
            if hemoglobin >= 13.5 and red_blood_cells >= 4.5 and white_blood_cells >= 4.0 and platelets >= 150:
                return "Normal blood cell counts"
            elif hemoglobin < 12 or red_blood_cells < 4.0 or platelets < 150:
                return "Low blood cell counts, potential anemia or thrombocytopenia"
            else:
                return "Abnormal blood cell counts, further evaluation recommended"
        return "Unknown"

    def analyze_nutritional_status(self, vitamin_d, vitamin_b12, folate):
        if all(val is not None for val in [vitamin_d, vitamin_b12, folate]):
            status = []
            if vitamin_d >= 30:
                status.append("Adequate vitamin D")
            else:
                status.append("Low vitamin D, supplementation recommended")

            if vitamin_b12 >= 200:
                status.append("Adequate vitamin B12")
            else:
                status.append("Low vitamin B12, further evaluation recommended")

            if folate >= 3.0:
                status.append("Adequate folate")
            else:
                status.append("Low folate levels, supplementation recommended")

            return ", ".join(status)
        return "Unknown"
    
    def categorize_blood_pressure(self, blood_pressure_systolic, blood_pressure_diastolic):
    
        if blood_pressure_systolic < 120 and blood_pressure_diastolic < 80:
            return "Normal Blood Pressure"
        elif 120 <= blood_pressure_systolic < 130 and blood_pressure_diastolic < 80:
            return "Elevated Blood Pressure"
        elif 130 <= blood_pressure_systolic < 140 or 80 <= blood_pressure_diastolic < 90:
            return "Hypertension Stage 1"
        elif blood_pressure_systolic >= 140 or blood_pressure_diastolic >= 90:
            return "Hypertension Stage 2"
        else:
            return "Hypertensive Crisis"
