import os
from OTXv2 import OTXv2, IndicatorTypes
from datetime import datetime, timedelta

# Initialize OTXv2 with your API key
API_KEY = os.getenv("a5f8715786fe25a9fad928d50c1aaad9480afdba4666d0")

otx = OTXv2(API_KEY)

# Fetch all pulses
pulses = otx.getall()

# Print the number of pulses retrieved
print(f"Number of pulses retrieved: {len(pulses)}")

# Print the pulses data
print(pulses)
