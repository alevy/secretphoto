#!/usr/bin/env python3

import argparse
import importlib
import json
import ag.common.testing as testing
import ag.ag3.runner


parser = argparse.ArgumentParser(description="Description of your program")
parser.add_argument(
    "-j", "--json", help="Write JSON grade report to this file", required=False, type=str
)
args = vars(parser.parse_args())

print("================================================================")
results = testing.run_tests()
print("================================================================")

json_out = args["json"]
if json_out is not None:
    with open(json_out, 'w') as f:
        f.write(json.dumps(results, indent=2))

