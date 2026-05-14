def validate_emails(emails):
    import re
    
    # Simple pattern: 
    # - at least one character before @
    # - then @
    # - then at least one character, a dot, and at least two characters after the dot
    pattern = r'^.+@.+\..{2,}$'
    
    valid = []
    invalid = []

    for email in emails:
        if re.search(pattern, email):
            valid.append(email)
        else:
            invalid.append(email)            
    
    return {"valid": valid, "invalid": invalid}

# Test
emails = ["test@email.com", "invalid-email", "user@company.co.uk"]
print(validate_emails(emails))