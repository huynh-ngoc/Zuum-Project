# Email Freight Quote Parser Prototype

---

## Introduction
This prototype code is designed to parse email content related to freight shipments and generate a freight quote based on the information extracted from the email. The code utilizes the spaCy library for Natural Language Processing (NLP) tasks. It's a basic implementation and does not incorporate more advanced NLP techniques using libraries such as NLTK or TensorFlow.

## Functionality
The code consists of several functions:

1. **process_email_body_advanced(body)**:
   - This function processes the email body using spaCy to extract relevant information such as pickup and drop-off dates, pickup and drop-off locations.
   - It also incorporates simple regex patterns to extract information if not found using spaCy.

2. **generate_freight_quote(extracted_info)**:
   - This function generates a freight quote based on the extracted information.
   - If any required information is missing, it prompts the user to provide the missing information.

3. **process_email_and_generate_quote(email_content)**:
   - This is the main function that processes the entire email content.
   - It calls the `process_email_body_advanced` function to extract information and then generates a freight quote using `generate_freight_quote`.

## Usage Instructions
To use this prototype, follow these steps:

1. **Install Dependencies**:
   - Ensure you have Python installed on your system.
   - Install the necessary dependencies by running:
     ```
     pip install spacy
     ```
   - Additionally, you need to download the English language model for spaCy. You can download it by running:
     ```
     python -m spacy download en_core_web_sm
     ```

2. **Run the Code**:
   - Copy the provided code into a Python script (e.g., `freight_quote_parser.py`).
   - Replace the `sample_email_content` variable with the actual email content you want to parse.
   - Run the script using:
     ```
     python freight_quote_parser.py
     ```

3. **Provide Missing Information**:
   - If any required information is missing from the email content, the script will prompt you to provide it.
   - You can manually input the missing information when prompted.

4. **Obtain Freight Quote**:
   - After providing all necessary information, the script will generate a freight quote based on the extracted details.

## Notes
- This prototype is a basic implementation and may not cover all possible email formats or scenarios.
- It primarily uses spaCy for NLP tasks and incorporates simple regex patterns for information extraction.
- For more advanced NLP techniques, consider integrating libraries like NLTK or TensorFlow.
- Further enhancements can be made to handle a wider variety of email formats and extract more detailed information.

---
This readme provides an overview of the prototype code for parsing email content and generating freight quotes. For any further inquiries or assistance, feel free to contact the developer.
