# biovision_main.py

from modules.Language import Language
from modules.Diagnostics import HealthDiagnosticsTool
from modules.Prescription import Prescription

class BioVision:
    def __init__(self):
        pass

    def start(self):
        # Use Language module
        text = "Hello, how are you?"
        language_meaning = Language.get_meaning(text)
        print(f"Language Meaning: {language_meaning}")

        # Use Diagnostics module
        diagnostics_tool = HealthDiagnosticsTool()
        diagnostics_tool.add_patient_data('total_cholesterol', 200)
        diagnostics_tool.add_patient_data('hdl_cholesterol', 50)
        diagnostics_tool.run_diagnostics()
        diagnostics_results = diagnostics_tool.results
        print("Diagnostics Results:")
        for analysis_type, result in diagnostics_results.items():
            print(f"- {analysis_type.capitalize()}: {result}")

        # Use Prescription module
        prescription = Prescription.generate_prescription(diagnostics_results)
        print(f"Prescription: {prescription}")

if __name__ == "__main__":
    biovision = BioVision()
    biovision.start()
