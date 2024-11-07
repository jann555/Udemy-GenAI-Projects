from langchain import OpenAI, PromptTemplate, LLMChain
import os

from langchain_core.prompts import FewShotPromptTemplate

# Set up the OpenAI API key
os.environ["OPENAI_API_KEY"] = "voc-927679694126677349941366e0f8c9298d01.66643071"
os.environ["OPENAI_API_BASE"] = "https://openai.vocareum.com/v1"

# Define the few-shot examples
examples = [
    {
        "question": "Find a large property under $1,000,000 in Green Oaks with at least 3 bedrooms with beautiful "
                    "surroundings",
        "answer": """
        "Neighborhood": "Green Oaks",
        "Price": "$800,000",
        "Bedrooms": "3",
        "Bathrooms": "2",
        "House Size": "2,000 sqft",
        "Description": "Welcome to this eco-friendly oasis nestled in the heart of Green Oaks. 
        This charming 3-bedroom, 2-bathroom home boasts energy-efficient features such as solar panels and a 
        well-insulated structure. Natural light floods the living spaces, highlighting the beautiful hardwood 
        floors and eco-conscious finishes. The open-concept kitchen and dining area lead to a spacious backyard with a 
        vegetable garden, perfect for the eco-conscious family. Embrace sustainable living without compromising on style 
        in this Green Oaks gem.",
        "Neighborhood Description": "Green Oaks is a close-knit, environmentally-conscious community with access to 
        organic grocery stores, community gardens, and bike paths. Take a stroll through the nearby Green Oaks Park or 
        grab a cup of coffee at the cozy Green Bean Cafe. With easy access to public transportation and bike lanes, 
        commuting is a breeze."
        """

    },
    {
        "question": "Find a reasonably prices home with enough bedrooms for a growing family with plenty of space and "
                    "sunlight in a good school district with good location for young adults",
        "answer": """
        "Neighborhood": "Sunnydale",
        "Price": "$750,000",
        "Bedrooms": "4",
        "Bathrooms": "3",
        "House Size": "2,500 sqft",
        "Description": "Experience luxury living in Sunnydale. This stunning 4-bedroom, 3-bathroom home features a 
        spacious open floor plan, high ceilings, and large windows that fill the space with natural light. 
        The gourmet kitchen is a chef's dream with top-of-the-line appliances and a large island. The master suite 
        boasts a spa-like bathroom and a walk-in closet. The backyard is perfect for entertaining with a beautiful 
        patio and landscaped garden.",
        "Neighborhood Description": "Sunnydale is known for its upscale living, excellent schools, and vibrant 
        community. Residents enjoy close proximity to shopping centers, fine dining, and recreational parks. 
        Sunnydale's serene atmosphere and convenient location make it a highly sought-after neighborhood."
        """

    }
]

# Create the prompt template
prompt_template = """
Generate a real estate listing based on the following details:

Neighborhood: {Neighborhood}
Price: {Price}
Bedrooms: {Bedrooms}
Bathrooms: {Bathrooms}
House Size: {House Size}

Description: {Description}

Neighborhood Description: {Neighborhood Description}

"""

example_prompt = PromptTemplate(input_variables=["question", "answer"], template="{question}\n{answer}")

# cot_prompt = FewShotPromptTemplate(
#     examples=examples,
#     example_prompt=example_prompt,
#     suffix="Use these questions and answers to give correct response to the problem below: {input}",
#     input_variables=["input"]
# )

# Initialize the LLM chain with few-shot examples
llm_chain = LLMChain(
    llm=OpenAI(model_name="gpt-3.5-turbo", temperature=0, max_tokens=2000),
    prompt_template=example_prompt
)

# Generate listings
for i in range(10):
    # Generate details for a new listing
    new_listing = {
        "Neighborhood": f"Neighborhood {i+1}",
        "Price": f"${(i+1) * 100000 + 600000}",
        "Bedrooms": str((i % 4) + 2),
        "Bathrooms": str((i % 3) + 1),
        "House Size": f"{(i+1) * 500 + 1500} sqft",
        "Description": "",  # Leave blank for the model to fill in
        "Neighborhood Description": ""  # Leave blank for the model to fill in
    }

    # Generate the listing
    generated_listing = llm_chain.run(new_listing)
    print(generated_listing)
