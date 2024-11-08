import pyfiglet

from vector_db import build_listings_db, perform_semantic_search
from prompt_creator import start_conversation_and_get_query

MAX_TOKENS = 3500
NUM_LISTINGS = 15
LISTINGS_FILE_NAME = "file_loader_doc"
TEMPERATURE = 0.9


def art_message(message):
    ascii_art = pyfiglet.figlet_format(message)
    print(ascii_art)


def start_home_match():
    art_message("Welcome to HomeMatch!")

    query = start_conversation_and_get_query(user_input_enable=False)

    db = build_listings_db(NUM_LISTINGS, MAX_TOKENS, TEMPERATURE, LISTINGS_FILE_NAME)

    chain = perform_semantic_search(db, query, TEMPERATURE, MAX_TOKENS)

    art_message("Results!")

    print(chain)


# Main appli
start_home_match()
