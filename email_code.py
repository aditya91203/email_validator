import re

def validate_email(email):
    # Define the regex pattern for a valid email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use re.match to check if the email matches the pattern
    if re.match(pattern, email):
        return "The email address is valid."
    else:
        return "The email address is invalid."

# Example usage
email_to_test = "example@example.com"  # Replace with the email you want to validate
result = validate_email(email_to_test)
print(result)
