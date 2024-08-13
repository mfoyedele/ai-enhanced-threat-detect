from OTXv2 import OTXv2, IndicatorTypes
from pandas.io.json import json_normalize
from datetime import datetime, timedelta

otx = OTXv2("OTX_API_KEY")

pulses = otx.getall()

# len(pulses)

json_normalize(pulses)[0:5]