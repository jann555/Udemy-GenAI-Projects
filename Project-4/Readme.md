# HomeMatch

This application leverages large language models (LLMs) and vector databases to transform standard real estate listings into personalized narratives that resonate with potential buyers' unique preferences and needs.

### Runbook
The first step to run this application is to install all the python packages includes in `requirements.txt`

**Run:**
```
pip install -r requirements.txt
```

To execute the code from the terminal run:

```
python HomeMatch.py
```

***Configure your API key***

```
Replace the text "YOUR API KEY" at the top of the following files:
-listings_generator.py
-prompt_creator.py
```

**Accepted Flags**
These flags offer control of the constants implemented on this application to give the user better control.

```
--max_tokens:'Maximum number of tokens for model (default: 3500)'
--num_listings:'Estimated Minimum Number of listings to be generated(default: 15)'
--generate_new_listings:'Generate new listings every time we execute the application (default: True)'
--test_data_enabled:'Enable test data will use hardcoded questions and answers; thus bypassing user input (default: True)'
--temperature:'Temperature for model. Higher temperature will increase creativity (default: 0.2)'

Example: python ./HomeMatch.py --max_tokens 2000 --num_listings 20 --temperature 0.5

```

### Application Flow

HomeMatch with will start the application by welcoming you to the application and informing you that it needs to ask you a few questions to help you find the best available listings according to your needs.

- The application builds a query from the questions and answers

- In the back-end the application is going to synthetically generate listings using a predefined template and save the output to a text file. We used the model "gpt-3.5-turbo-instruct" to generate these listings

- We load, split into chunks and generate embeddings.

- We load the split chunks and embeddings into our ChromaDB.

- The program performs semactic search using the query and the context from our DB.  We used the model "gpt-3.5-turbo" for our llm.

- Output the recommendations based on the user preferences.


