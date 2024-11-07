# A starter file for the HomeMatch application if you want to build your solution in a Python program instead of a
# notebook.

import os
from listings_generator import generate_real_estate_listings as listing_gen

from langchain.llms import OpenAI
from langchain.vectorstores import Chroma

"""
PART I - Understanding Buyer Preferences:
Buyers will input their requirements and preferences, such as:
 -location, property type, budget, amenities, and lifestyle choices.
 
 The application uses LLMs to interpret these inputs in natural language, 
 understanding nuanced requests beyond basic filters.
"""

## 1- TODO Generate at least 10 listings using prompting examples. Use these examples to populate DB
real_state_listings = listing_gen()
print(real_state_listings)
"""
PART II - Integrating with a Vector Database:

Connect "HomeMatch" with a vector database, where all available property listings are stored.
Utilize vector embeddings to match properties with buyer preferences, focusing on aspects like
neighborhood vibes, architectural styles, and proximity to specific amenities.
"""

"""

PART III - Personalized Listing Description Generation:

For each matched listing, use an LLM to rewrite the description in a way that highlights aspects 
most relevant to the buyer’s preferences.
Ensure personalization emphasizes characteristics appealing to the buyer without altering 
factual information about the property.
"""

"""
PART IV - Listing Presentation:
Output the personalized listing(s) as a text description of the listing.
"""
