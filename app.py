import base64
import json

# Load Base64 string from JSON file
with open("pdf_base64.json", "r") as json_file:
    data = json.load(json_file)
    base64_string = data["base64string"]

# Decode Base64 and save as a PDF file
pdf_data = base64.b64decode(base64_string)
with open("output.pdf", "wb") as pdf_file:
    pdf_file.write(pdf_data)

print("PDF file saved as output.pdf")
