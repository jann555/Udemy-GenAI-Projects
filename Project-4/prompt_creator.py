import os
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = "YOUR API KEY"
os.environ["OPENAI_API_BASE"] = "https://openai.vocareum.com/v1"
# Defined a constant to define when to implement user interaction

model = "gpt-3.5-turbo"
temperature = 0.5
llm = ChatOpenAI(model=model, temperature=temperature, max_tokens=2000)

# Define hardcode questions for testing purposes

QUESTIONS = [
    "How big do you want your house to be?\n",
    "What are 3 most important things for you in choosing this property?\n",
    "Which amenities would you like?\n",
    "Which transportation options are important to you?\n",
    "How urban do you want your neighborhood to be?\n",
]
ANSWERS = [
    "A comfortable three-bedroom house with a spacious kitchen and a cozy living room.\n",
    "A quiet neighborhood, good local schools, and convenient shopping options.\n",
    "A backyard for gardening, a two-car garage, and a modern, energy-efficient heating system.\n",
    "Easy access to a reliable bus line, proximity to a major highway, and bike-friendly roads.\n",
    "A balance between suburban tranquility and access to urban amenities like restaurants and theaters.\n"
]

Q_AND_A = {
    "personal_questions": QUESTIONS,
    "personal_answers": ANSWERS
}


def print_hardcoded_q_n_a():
    for i in range(len(QUESTIONS)):
        print(Q_AND_A["personal_questions"][i], "\n")
        print(Q_AND_A["personal_answers"][i], "\n")

    return Q_AND_A


def get_conversation_query(personal_questions: [], personal_answers: []):
    questions_count = len(personal_questions)
    query = """"""
    query += f"""You are the AI model that will find real state listings that match the criteria to the user answers 
    to personal questions. Ask the user {questions_count + 1} questions\n"""

    for i in range(questions_count):
        query += f'Question {i}: {personal_questions[i]}\n'
        query += f'Answer {i}: {personal_answers[i]}\n'

    query += """\n\n Now recommend listings with personalized descriptions based on buyer preferences. The 
    descriptions should be unique, appealing, and tailored to the preferences provided. This involves subtly 
    emphasizing aspects of the property that align with what the buyer is looking for. Ensure that the augmentation 
    process enhances the appeal of the listing without altering factual information. Output the real state listing(s) 
    with the personalized augmented text description while keeping the basic listing information.\n"""
    return query


def ask_user_questions():
    questions_and_answers = {
        "personal_questions": QUESTIONS,
    }

    answers = []
    print("Answer the following questions so we can help you find your dream home\n")
    for question in QUESTIONS:
        answer = input(question)
        answers.append(answer)
    questions_and_answers["personal_answers"] = answers
    print("Thank you for helping us better understand what you are looking for in a home\n")

    return questions_and_answers


def start_conversation_and_get_query(test_data_enabled=False):
    print('Let\'s start by getting you know your preferences by answering some basic questions to help you find your '
          'dream home\n')
    questions_and_answers = ask_user_questions() if not test_data_enabled else print_hardcoded_q_n_a()
    questions = questions_and_answers["personal_questions"]
    answers = questions_and_answers["personal_answers"]
    query = get_conversation_query(questions, answers)
    return query
