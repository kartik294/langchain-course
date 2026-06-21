from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch






llm = ChatOpenAI(model="gpt-4o-mini")

tools = [TavilySearch]

agent = create_agent(
    model=llm,
    tools=tools
)


def main():
    print("Hello from langchain-course!")

    result = agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content="Search the real time job postings for an AI engineer using langchain in the banglore on linkedin and list thier details"
                )
            ]
        }
    )

    print(result)


if __name__ == "__main__":
    main()