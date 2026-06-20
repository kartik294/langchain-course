<<<<<<< HEAD
import os

from dotenv import load_dotenv
=======
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
>>>>>>> 4aa0742 (hello world chain)

load_dotenv()


def main():
<<<<<<< HEAD
    print("Hello from langchain-course!")


if __name__ == "__main__":
    main()
=======

    information = """
    Elon Musk is a billionaire entrepreneur and business magnate. He is the CEO of Tesla and SpaceX,
    founder of xAI, and co-founder of PayPal. He is known for his work in electric vehicles,
    space exploration, artificial intelligence, and other technology ventures.
    """

    summary_template = """
    You are a helpful assistant.

    Based ONLY on the information below:

    {information}

    Provide:
    1. A short summary
    2. Two interesting facts

    Answer directly.
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    llm = ChatOllama(
        model="gemma3:270m",
        temperature=0
    )

    chain = summary_prompt_template | llm

    # Debug: See what is being sent to the model
    formatted_prompt = summary_prompt_template.format(
        information=information
    )

    print("========= PROMPT =========")
    print(formatted_prompt)
    print("==========================\n")

    response = chain.invoke(
        {"information": information}
    )

    print("========= RESPONSE =========")
    print(response.content)
    print("============================")


if __name__ == "__main__":
    main()
>>>>>>> 4aa0742 (hello world chain)
