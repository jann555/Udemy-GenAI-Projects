# Personalized Real Estate Agent

## Synthetic Data Generation

### Generating Real Estate Listings with an LLM
- **RUBRIC ITEM PASSED DESCRIPTION**: The submission must demonstrate using a Large Language Model (LLM) to generate at least 10 diverse and realistic real estate listings containing facts about the real estate.
- **RUBRIC ITEM REVIEWER TIPS**: Check if the LLM is effectively utilized to create detailed and varied listings. Listings should not be generic and must reflect creativity and realistic aspects of real estate properties.

## Semantic Search

### Creating a Vector Database and Storing Listings
- **RUBRIC ITEM PASSED DESCRIPTION**: The project must demonstrate the creation of a vector database and successfully storing real estate listing embeddings within it. The database should effectively store and organize the embeddings generated from the LLM-created listings.
- **RUBRIC ITEM REVIEWER TIPS**: Verify the implementation of the vector database and assess how the embeddings are generated from the listings. Ensure that the database is appropriately configured for storing and retrieving the embeddings. Check if the embeddings are representative of the listing's semantic content, allowing for effective retrieval based on semantic searches. The reviewer should also look for efficient handling and querying of the database within the application.

### Semantic Search of Listings Based on Buyer Preferences
- **RUBRIC ITEM PASSED DESCRIPTION**: The application must include a functionality where listings are semantically searched based on given buyer preferences. The search should return listings that closely match the input preferences.
- **RUBRIC ITEM REVIEWER TIPS**: Evaluate the search mechanism's effectiveness in matching listings to specific preferences. Check if the search results are relevant and accurately reflect the preferences inputted.

## Augmented Response Generation

### Logic for Searching and Augmenting Listing Descriptions
- **RUBRIC ITEM PASSED DESCRIPTION**: The project must demonstrate a logical flow where buyer preferences are used to search and then augment the description of real estate listings. The augmentation should personalize the listing without changing factual information.
- **RUBRIC ITEM REVIEWER TIPS**: Focus on the logic connecting the search results to the augmentation process. The augmented descriptions should be personalized in a way that aligns with the buyer's preferences while maintaining the integrity of the original listing.

### Use of LLM for Generating Personalized Descriptions
- **RUBRIC ITEM PASSED DESCRIPTION**: The submission must utilize an LLM to generate personalized descriptions for the real estate listings based on buyer preferences. The descriptions should be unique, appealing, and tailored to the preferences provided.
- **RUBRIC ITEM REVIEWER TIPS**: Assess the effectiveness and creativity of the LLM in generating personalized descriptions. Check for the relevance and uniqueness of these descriptions in relation to the buyer’s preferences.


---

# Suggestions to Make Your Project Stand Out

For a project that truly stands out, consider integrating CLIP to enable multimodal search capabilities. This advanced feature would allow the application to search real estate listings through textual descriptions and images associated with each property. By doing so, the application can align visual elements of a property (like style, layout, and surroundings) with the textual buyer preferences.

## Implementation Overview

### Image Embeddings
Generate embeddings for real estate images using CLIP, which can then be stored in the vector database alongside text embeddings.

### Multimodal Search Logic
Develop a search algorithm that considers both text and image embeddings to find listings that best match the buyer's preferences, including visual aspects.

---