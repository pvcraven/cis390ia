"""
Example code demonstrating how to read information from environment
variables.

For better security, your password would be encrypted and you'd
need to decrypt it before use. That's a separate lesson.
"""
import os

# Get environment variables
api_user = os.getenv('API_USER')
api_password = os.environ.get('API_PASSWORD')

# Print results
print(f"{api_user=}")
print(f"{api_password=}")
