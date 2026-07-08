import os
import sys
from dotenv import load_dotenv
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__))))

from extractor.extractor import Extractor

load_dotenv()

document = """
Stockly is an inventory intelligence platform.

It helps retailers reduce inventory costs by 22%.

Features

AI Forecasting

Inventory Optimization

Target Customers

Retail Chains

Primary Buyer

Supply Chain Manager
"""

extractor = Extractor()
result = extractor.extract(document)

print(result.model_dump_json(indent=2))