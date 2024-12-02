# Check for null bytes and remove them from the file
file_path = 'D:/projectsoft/scrum-project/tests/test_accounts.py'

# Open the file in binary mode ('rb' for reading binary)
with open(file_path, 'rb') as file:
    content = file.read()  # Read all content of the file

# Remove null bytes (b'\x00' represents a null byte in binary form)
cleaned_content = content.replace(b'\x00', b'')  # Replaces all null bytes with nothing

# Save the cleaned content back to the file in binary mode ('wb' for writing binary)
with open(file_path, 'wb') as file:
    file.write(cleaned_content)  # Write the cleaned content back to the file

print("Null bytes removed and file saved.")
