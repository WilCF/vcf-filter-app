import vobject

def filter_vcf_with_phone_numbers(input_file, output_file):
    with open(input_file, 'r') as file:
        vcf_data = file.read()  # Read entire content at once

    vcf_contacts = vobject.readComponents(vcf_data)  # Process all contacts from the string data

    with open(output_file, 'w') as outfile:
        for contact in vcf_contacts:
            # Clean contact to remove photos and retain only phone numbers and formatted names
            clean_contact(contact)
            # Check if contact has phone number to include it
            if 'tel' in contact.contents:
                outfile.write(contact.serialize())

def clean_contact(contact):
    # Remove photo if present
    if 'photo' in contact.contents:
        del contact.contents['photo']

    # Retain only the phone number and formatted name fields
    for key in list(contact.contents):
        if key != 'tel' and key != 'fn':
            del contact.contents[key]

# Example usage
input_vcf = 'input.vcf'  # Replace with your input file path
output_vcf = 'filtered_output.vcf'  # Replace with your desired output file path

filter_vcf_with_phone_numbers(input_vcf, output_vcf)
