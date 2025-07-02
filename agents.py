from crewai import Agent

from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from tools import tool

#call gemini model
llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))

# Creating a senior researcher agent with memory and verbose mode
print(llm.invoke("What is the capital of France?"))
news_reasearcher = Agent(
    role = "Senior Researcher",
    goal = "Unccover ground breaking technologies in {topic}",
    verbose  =True,
    memory = True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."

    ),
    tool = [tool],
    llm = llm,
    allow_delegation=True
)

## creating a write agent with custom tools responsible in writing news blog

news_writer = Agent(
    role = "Writer",
    goal = "Narrate compelling tech stories about {topic}",
    verbose  =True,
    memory = True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."

    ),
    tool = [tool],
    llm = llm,
    allow_delegation=False
)