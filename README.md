# Experiment-Doc-Maker

A Python script that generates an experiment document based on the provided experiment number and aim. This tool automates the documentation process, making it easier for students to create structured experiment reports.

## Features
- Generate a detailed theory section using the Gemini API.
- Convert HTML content to a formatted Word document.
- Include user-specific details such as name, roll number, and batch.

## Prerequisites
Before running the script, ensure you have the following:

1. **Python 3.x** installed on your machine.
2. A valid API key for the Gemini API.

## Getting Started

### Step 1: Create an API Key
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Sign up for a free account if you don't have one.
3. Create a new API key and copy it.

### Step 2: Update the API Key in the Code
- Open the script in your preferred text editor.
- Locate the line with `genai.configure(api_key="")`.
- Replace the empty string with your actual API key, like so:
  ```python
  genai.configure(api_key="YOUR_API_KEY_HERE")
  ```

### Step 3: Install Necessary Packages
To ensure the script runs smoothly, you need to install the required Python packages. You can do this using pip:

```bash
pip install google-generativeai python-docx beautifulsoup4
```

### Step 4: Run the Script
After you have configured the API key and installed the necessary packages, run the script using Python:

```bash
python experiment_doc_maker.py
```

### Step 5: Provide Inputs
- When prompted, enter the following:
  - Experiment Number
  - Aim of the Experiment
  - Your Name
  - Your Roll Number
  - Your Batch

### Step 6: Check Your Document
After running the script, you will find a Word document named `experiment_<experiment_number>_aim_and_theory.docx` in the same directory. This document contains the generated content based on your inputs.

## Example Usage
```
Enter the Experiment Number: 1
Enter the Aim: To study the properties of semiconductors.
Enter your Name: John Doe
Enter your Roll Number: 123456
Enter your Batch: 2024
```

## License
This project is licensed under the MIT License.

## Acknowledgements
- [Google Generative AI](https://aistudio.google.com/) for providing the API to generate content.
- [Python-docx](https://python-docx.readthedocs.io/en/latest/) for handling Word document creation.

