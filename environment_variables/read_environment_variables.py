import os

# Get environment variables
api_user = os.getenv('API_USER')
api_password = os.environ.get('API_PASSWORD')

# Print results
print(f"{api_user=}")
print(f"{api_password=}")
