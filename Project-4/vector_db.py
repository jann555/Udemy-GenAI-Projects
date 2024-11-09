from langchain.chains.question_answering import load_qa_chain
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from listings_generator import generate_real_estate_listings as listing_gen

model_name = "gpt-3.5-turbo"
CHUNK_SIZE = 1000


def build_listings_db(num_listings, max_tokens, temperature, generate_new_listings):
    # We use listing_gen(num_listings, max_tokens, LISTINGS_FILE_NAME) to generate real listings and return them in the
    # form of a text file
    raw_listings = listing_gen(num_listings, max_tokens, temperature, generate_new_listings)
    # Load Text document from file_name path
    docs = TextLoader(raw_listings).load()
    # use a Text Splitter to split the documents into chunks
    splitter = CharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=0)

    splitter_docs = splitter.split_documents(docs)
    # initialize your embeddings model
    embeddings = OpenAIEmbeddings()

    # Return database instance with the chunks
    return Chroma.from_documents(splitter_docs, embeddings)


def perform_semantic_search(db, query, temperature, max_tokens):
    llm = OpenAI(model_name=model_name, temperature=temperature, max_tokens=max_tokens)
    similar_docs = db.similarity_search(query, k=2)
    prompt = PromptTemplate(
        template="{query}\nContext: {context}",
        input_variables=["query", "context"],
    )
    chain = load_qa_chain(llm, prompt=prompt, chain_type="stuff")
    return chain.run(input_documents=similar_docs, query=query)
