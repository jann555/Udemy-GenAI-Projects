import openai
from pathlib import Path
import random

# Set up the OpenAI API key
openai.api_base = "https://openai.vocareum.com/v1"
openai.api_key = "YOUR API KEY"
model_name = "gpt-3.5-turbo-instruct"
LISTINGS_FILE_NAME = f"listings"


def generate_real_estate_listings(num, max_tokens, temperature, generate_new_listings=True) -> str:
    # Define the prompt for generating real estate listings
    print('Please wait while we prepare some awesome recommendations for you! Loading...')
    rand_seed = random.randint(1, 1000000) if generate_new_listings else ''
    path = f'./{LISTINGS_FILE_NAME}{rand_seed}.txt'
    file_exists = Path(path).is_file()

    # Check if this function has already been executed and generated an output file to avoid executing it again
    if file_exists:
        return path

    prompt = f"""
    Generate at least {num} real estate listings. Each listing should include:
    - Neighborhood
    - Price
    - Bedrooms
    - Bathrooms
    - House Size
    - Description
    - Neighborhood Description

    Example:
    Neighborhood: Roswell
    Price: $550,000
    Bedrooms: 4
    Bathrooms: 4
    House Size: 2,911 sqft
    
    Description: This homes sits on a private lot on a quiet cul-de-sac street, this traditional hard coat stucco 
    home is situated in an active swim and tennis community within the desirable Roswell High School district. 
    It offers a perfect blank canvas for your personal touches. Featuring two finished levels and an unfinished 
    basement, this home has ample space for your creativity. A welcoming large front porch opens into a two-story foyer,
    leading to a fireside living room, a separate dining room, and a gourmet kitchen equipped with double ovens and a 
    large work island. The kitchen seamlessly connects to the  fireside family room, complete with French doors that 
    open to a spacious deck. The second floor features a luxurious primary suite with a spa-like bath with vaulted 
    ceiling, and a generous walk-in closet, along with a versatile flex room. There are three additional bedrooms, 
    including one with a Jack and Jill bath and another en-suite. The full unfinished daylight basement is a blank 
    slate, stubbed for a full bath and ready for your finishing touches. Step outside to enjoy the large deck 
    overlooking the expansive private lot—perfect for entertaining or simply relaxing.  Two car side entry garage. 
    This is a great opportunity to create your dream home in a prime Roswell location where homes are selling for 
    significantly more.
    
    Neighborhood Description: Discover this exceptional opportunity in a highly sought-after area, just 1.5 miles from 
    the vibrant dining and shopping scene on Canton Street in Historic Roswell. Enjoy the convenience of nearby 
    Roswell Area Park, the Chattahoochee Nature Center, and top rated public and private schools. Plus, 
    East Cobb's Avenue offers even more options for shopping and dining. With easy access to GA 400 and major
     roads like Johnson Ferry and Roswell Road, commuting is a breeze. 
    
    Now, generate real estate listings following this template.
    """

    # Generate real estate listings using OpenAI's language model
    response = openai.Completion.create(
        engine=model_name,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature
    )

    listings = response.choices[0].text.strip()

    if path:
        with open(path, "a+") as file:
            # Write data to the file
            file.write(listings)

    return path
