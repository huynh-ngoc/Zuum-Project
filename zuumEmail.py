import spacy
import re

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Advanced NLP for parsing email body and extracting information
def process_email_body_advanced(body):
    # Parse the email body with spaCy
    doc = nlp(body)

    # Initialize variables to store extracted information
    extracted_info = {
        "Pick up date": "missing",
        "Drop off date": "missing",
        "logistic_shipment_pickup_location": "missing",
        "logistic_shipment_dropoff_location": "missing",
        "number_of_pickup_stops": "missing",
        "number_of_dropoff_stops": "missing",
        "truck_type": "missing",
        "hamazat": "missing",
        "weight_of_shipment": "missing",
        "number_of_pallets_or_boxes": "missing"
    }

    # Extract relevant information using spaCy and regex patterns
    for ent in doc.ents:
        if ent.label_ == "DATE":
            # Extract pickup and drop-off dates
            if "PU" in ent.text:
                extracted_info["Pick up date"] = ent.text.split("PU-")[1].strip()
            elif "DEL" in ent.text:
                extracted_info["Drop off date"] = ent.text.split("DEL-")[1].strip()
        elif ent.label_ == "GPE":
            # Extract pickup and drop-off locations
            if "from" in body.lower() and "to" in body.lower():
                locations = body.lower().split("from")[1].split("to")
                extracted_info["Pickup_location"] = locations[0].strip()
                extracted_info["Dropoff_location"] = locations[1].strip()

    # If pickup and drop-off dates are still missing, try to extract them using regex
    if extracted_info["Pick up date"] == "missing":
        pickup_date_match = re.search(r'PU-\s*([\d/]+)', body)
        if pickup_date_match:
            extracted_info["Pick up date"] = pickup_date_match.group(1)
    if extracted_info["Drop off date"] == "missing":
        dropoff_date_match = re.search(r'DEL-\s*([\d/]+)', body)
        if dropoff_date_match:
            extracted_info["Drop off date"] = dropoff_date_match.group(1)

    return extracted_info

# Function to generate freight quote based on extracted information
def generate_freight_quote(extracted_info):
    # Check if any information is missing
    missing_info = [key for key, value in extracted_info.items() if value == "missing"]
    if missing_info:
        print("The following information is missing from the email:")
        for key, value in extracted_info.items():
            if value != "missing":
                print(f"{key}: {value}")
            else:
                print(f"{key}: missing")
        print("Please provide the missing information.")
        # Here you can prompt the user to input the missing information manually
        # or you can automate it by querying a database or external service
        return None
    else:
        # If all information is available, generate the freight quote
        # Let's assume a fixed quote of $1000
        freight_quote = 1000
        return freight_quote


# Main function to process email content and generate freight quote
def process_email_and_generate_quote(email_content):
    extracted_info = process_email_body_advanced(email_content)
    freight_quote = generate_freight_quote(extracted_info)
    return freight_quote

# Sample email content (replace this with the actual email content)
sample_email_content = """
Hi- please let me know that you can take this load and your rate

Marion, OH to Bedford Park, IL – dry

PU- 11/8

DEL- 11/9

 

Thank you.

"""

# Call the function to process email content and generate freight quote
freight_quote = process_email_and_generate_quote(sample_email_content)
if freight_quote is not None:
    print("Freight Quote:", freight_quote)
