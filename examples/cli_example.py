#!/usr/bin/env python

# Very Simple CLI example to get indicator details from Alienvault OTX

from OTXv2 import OTXv2
import IndicatorTypes
import argparse
import os
import json

# Store OTX API key in environment variable OTX_API_KEY
API_KEY = os.getenv("OTX_API_KEY")

otx = OTXv2(API_KEY)

parser = argparse.ArgumentParser(description='OTX CLI Example')
parser.add_argument('-i', '--ip', help='IP eg; 4.4.4.4', required=False)
parser.add_argument('-d', '--domain', help='Domain eg; alienvault.com', required=False)
parser.add_argument('-ho', '--hostname', help='Hostname eg; www.alienvault.com', required=False)
parser.add_argument('-u', '--url', help='URL eg; http://www.alienvault.com', required=False)
parser.add_argument('-m', '--md5', help='MD5 Hash of a file eg; 7b42b35832855ab4ff37ae9b8fa9e571', required=False)
parser.add_argument('-p', '--pulse', help='Search pulses for a string eg; Dridex', required=False)
parser.add_argument('-s', '--subscribed', help='Get pulses you are subscribed to', required=False, action='store_true')

args = vars(parser.parse_args())

output_data = {}

if args["ip"]:
    output_data["ip_details"] = otx.get_indicator_details_full(IndicatorTypes.IPv4, args["ip"])

if args["domain"]:
    output_data["domain_details"] = otx.get_indicator_details_full(IndicatorTypes.DOMAIN, args["domain"])

if args["hostname"]:
    output_data["hostname_details"] = otx.get_indicator_details_full(IndicatorTypes.HOSTNAME, args["hostname"])

if args["url"]:
    output_data["url_details"] = otx.get_indicator_details_full(IndicatorTypes.URL, args["url"])

if args["md5"]:
    output_data["md5_details"] = otx.get_indicator_details_full(IndicatorTypes.FILE_HASH_MD5, args["md5"])

if args["pulse"]:
    result = otx.search_pulses(args["pulse"])
    output_data["pulse_search_results"] = result.get('results')

if args["subscribed"]:
    output_data["subscribed_pulses"] = otx.getall(max_items=3, limit=5)

# Save output data to a JSON file
with open('otx_output.json', 'w') as json_file:
    json.dump(output_data, json_file, indent=4)

print("Data has been saved to otx_output.json")
