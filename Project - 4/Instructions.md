  ## Project Instructions
In order to create the "HomeMatch" application, you can use these steps for guidance. Build the "HomeMatch" application in a Jupyter Notebook or Python file(s). A workspace is provided on the next page for you to use that has several dependencies already installed. It's good practice to create a GitHub repository to develop your application. You'll submit a zip file containing the application and supporting documentation files. Your project will be assessed against this rubric (opens in a new tab).

### Step 1: Setting Up the Python Application
- **Initialize a Python Project:** Create a new Python project, setting up a virtual environment and installing necessary packages like LangChain, a suitable LLM library (e.g., OpenAI's GPT), and a vector database package compatible with Python (e.g., ChromaDB or LanceDB). If you don't wish to create your files from scratch, starter files are available in the workspace on the next page as an application skeleton.

### Step 2: Generating Real Estate Listings
- **Generate real estate listings using a Large Language Model:** Generate at least 10 listings. This can involve creating prompts for the LLM to produce descriptions of various properties. An example of a listing might be:
  - **Neighborhood:** Green Oaks
  - **Price:** $800,000
  - **Bedrooms:** 3
  - **Bathrooms:** 2
  - **House Size:** 2,000 sqft
  - **Description:** Welcome to this eco-friendly oasis nestled in the heart of Green Oaks. This charming 3-bedroom, 2-bathroom home boasts energy-efficient features such as solar panels and a well-insulated structure. Natural light floods the living spaces, highlighting the beautiful hardwood floors and eco-conscious finishes. The open-concept kitchen and dining area lead to a spacious backyard with a vegetable garden, perfect for the eco-conscious family. Embrace sustainable living without compromising on style in this Green Oaks gem.
  - **Neighborhood Description:** Green Oaks is a close-knit, environmentally-conscious community with access to organic grocery stores, community gardens, and bike paths. Take a stroll through the nearby Green Oaks Park or grab a cup of coffee at the cozy Green Bean Cafe. With easy access to public transportation and bike lanes, commuting is a breeze.
- You'll use these listings to populate the database for testing and development of "HomeMatch".

### Step 3: Storing Listings in a Vector Database
- **Vector Database Setup:** Initialize and configure ChromaDB or a similar vector database to store real estate listings.
- **Generating and Storing Embeddings:** Convert the LLM-generated listings into suitable embeddings that capture the semantic content of each listing, and store these embeddings in the vector database.

### Step 4: Building the User Preference Interface
- **Collect buyer preferences:** Such as the number of bedrooms, bathrooms, location, and other specific requirements from a set of questions or by telling the buyer to enter their preferences in natural language. You can hard-code the buyer preferences in questions and answers or collect them interactively however you'd like. Example:
  - ```python
    questions = [
        "How big do you want your house to be?",
        "What are the 3 most important things for you in choosing this property?",
        "Which amenities would you like?",
        "Which transportation options are important to you?",
        "How urban do you want your neighborhood to be?",
    ]
    answers = [
        "A comfortable three-bedroom house with a spacious kitchen and a cozy living room.",
        "A quiet neighborhood, good local schools, and convenient shopping options.",
        "A backyard for gardening, a two-car garage, and a modern, energy-efficient heating system.",
        "Easy access to a reliable bus line, proximity to a major highway, and bike-friendly roads.",
        "A balance between suburban tranquility and access to urban amenities like restaurants and theaters."
    ]
    ```
- **Buyer Preference Parsing:** Implement logic to interpret and structure these preferences for querying the vector database.

### Step 5: Searching Based on Preferences
- **Semantic Search Implementation:** Use the structured buyer preferences to perform a semantic search on the vector database, retrieving listings that most closely match the user's requirements.
- **Listing Retrieval Logic:** Fine-tune the retrieval algorithm to ensure that the most relevant listings are selected based on the semantic closeness to the buyer’s preferences.

### Step 6: Personalizing Listing Descriptions
- **LLM Augmentation:** For each retrieved listing, use the LLM to augment the description, tailoring it to resonate with the buyer’s specific preferences. This involves subtly emphasizing aspects of the property that align with what the buyer is looking for.
- **Maintaining Factual Integrity:** Ensure that the augmentation process enhances the appeal of the listing without altering factual information.

### Step 7: Deliverables and Testing
- **Test your "HomeMatch" application:** Make sure it meets all of the requirements in the rubric (opens in a new tab). Your project code will be run when it's assessed. Enter different "buyer preferences" and ensure it works.
- **Jupyter Notebook/Python Program:** Compile the application code in a Jupyter notebook or a standalone Python program. Ensure the code is well-commented and logically structured.
- **Example Outputs:** Include example outputs showcasing how user preferences are processed and how the application generates personalized listing descriptions. You can include these in comments in your application or in a Jupyter notebook that's saved with outputs.

### Step 8: Project Submission
- **Generated Listings:** Include a file that contains your synthetically generated real estate listings. Name this file "listings".
- **Project Documentation:** Include a readme file or an accompanying document explaining the functionality, how to run the code, and any prerequisites or dependencies.
- **Code Submission:** Submit the Jupyter Notebook or Python program on the "Project Submission Page" that follows the workspace page.

### Stand-Out Suggestion
- Want to make your project stand out or stretch your skills? Add images and image search using CLIP to the real estate listings and implement multi-modal search in your "HomeMatch" application.