import os
import google.generativeai as genai
from docx import Document

# Configure Gemini API
genai.configure(api_key="YOUR_GOOGLE_API_KEY")

def generate_theory(aim):
    # Use Gemini-1.5-Flash to generate content for the Theory section
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Input prompt for the theory section
    prompt = f"Generate a detailed theory section for the experiment with the aim: {aim}"

    # Generate content
    response = model.generate_content(prompt)

    # Return generated theory text
    return response.text if response and response.text else "Error generating theory."

def create_experiment_doc(experiment_number, aim, theory):
    # Create a new Document
    doc = Document()

    # Add Experiment Title (centered and bold)
    doc.add_heading(f'Experiment - {experiment_number}', 0)

    # Add Aim section
    doc.add_heading('Aim', level=1)
    doc.add_paragraph(aim)

    # Add Theory section
    doc.add_heading('Theory', level=1)
    doc.add_paragraph(theory)

    # Save the document as 'experiment_aim_and_theory.docx'
    doc_name = f'experiment_{experiment_number}_aim_and_theory.docx'
    doc.save(doc_name)
    print(f"Document '{doc_name}' has been created successfully!")

if __name__ == "__main__":
    # Take Experiment Number and Aim as input from the command line
    experiment_number = input("Enter the Experiment Number: ")
    aim = input("Enter the Aim: ")

    # Generate Theory based on the Aim (using Gemini API)
    theory = generate_theory(aim)

    # Create the experiment document with Experiment Number, Aim, and Theory
    create_experiment_doc(experiment_number, aim, theory)
