import os
import warnings
import pyfiglet
import argparse
from vector_db import build_listings_db, perform_semantic_search
from prompt_creator import start_conversation_and_get_query

# Set up argument parser
parser = argparse.ArgumentParser(description="HomeMatch Application")
parser.add_argument('--max_tokens', type=int, default=3500, help='Maximum number of tokens (default: 3500)')
parser.add_argument('--num_listings', type=int, default=15, help='Number of listings (default: 15)')
parser.add_argument('--generate_new_listings', type=bool, default=True, help='Generate new listings (default: True)')
parser.add_argument('--test_data_enabled', type=bool, default=True, help='Enable test data (default: True)')
parser.add_argument('--temperature', type=float, default=0.2, help='Temperature for model (default: 0.2)')

args = parser.parse_args()

MAX_TOKENS = args.max_tokens
NUM_LISTINGS = args.num_listings
GENERATE_NEW_LISTINGS = args.generate_new_listings
TEST_DATA_ENABLED = args.test_data_enabled
TEMPERATURE = args.temperature


def art_message(message):
    ascii_art = pyfiglet.figlet_format(message)
    print(ascii_art)


def start_home_match():
    art_message("Welcome to HomeMatch")
    # Start by asking the user some questions to better understand its preferences
    query = start_conversation_and_get_query(test_data_enabled=TEST_DATA_ENABLED)

    # We are going to generate the listings, create embeddings and load them to our ChromaDB
    db = build_listings_db(NUM_LISTINGS, MAX_TOKENS, TEMPERATURE, generate_new_listings=GENERATE_NEW_LISTINGS)

    # Perform semantic search and output the results
    chain = perform_semantic_search(db, query, TEMPERATURE, MAX_TOKENS)

    art_message("Results")

    print(chain)


# Main application
if __name__ == "__main__":
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        start_home_match()
