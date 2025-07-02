from crewai import Crew, Process
from tasks import research_task, write_task
from agents import news_reasearcher, news_writer


crew  =Crew(
    agents = [news_reasearcher, news_writer],
    tasks = [research_task, write_task],
    process = Process.sequential,
)

# Starting the task execution process with enhanced feedback

result=crew.kickoff(inputs={'topic':'Agentic Retrieval Augmented Generation (RAG)'})
print(result)