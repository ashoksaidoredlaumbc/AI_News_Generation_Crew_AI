# Crew AI Gemini LLM

This project leverages [CrewAI](https://github.com/joaomdmoura/crewAI) to orchestrate autonomous AI agents for researching and writing about cutting-edge technology topics. It uses Google's Gemini LLM (via `langchain_google_genai`) and integrates internet search capabilities with SerperDev.

## Features
- **Autonomous Researcher Agent:** Uncovers groundbreaking technologies in a given topic.
- **Writer Agent:** Crafts compelling, easy-to-understand articles based on research.
- **Sequential Task Execution:** Research and writing tasks are performed in order.
- **Internet Search Integration:** Uses SerperDev for up-to-date information.
- **Customizable Topic:** Easily specify the technology topic of interest.

## Requirements
- Python 3.8+
- Google Gemini API access
- SerperDev API access

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/ashoksaidoredlaumbc/AI_News_Generation_Crew_AI.git
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Environment Variables
Create a `.env` file in the project root with the following variables:

```
GOOGLE_API_KEY=your_google_gemini_api_key
SERPER_API_KEY=your_serperdev_api_key
```

- `GOOGLE_API_KEY`: Your Google Gemini API key (for `langchain_google_genai`).
- `SERPER_API_KEY`: Your SerperDev API key (for internet search).

## Usage
Run the main crew script to generate a research report and a markdown article on your chosen topic:

```bash
python crew.py
```

By default, the topic is set to `Agentic Retrieval Augmented Generation (RAG)`. To change the topic, modify the `inputs` argument in `crew.py`:

```python
result = crew.kickoff(inputs={'topic': 'Your Desired Topic'})
```

## Output
- The script prints the research and article results to the console.
- The final article is saved as `new-blog-post.md` in the project directory.

## File Structure
- `agents.py`: Defines the researcher and writer agents.
- `tasks.py`: Sets up the research and writing tasks.
- `tools.py`: Configures the SerperDev tool for internet search.
- `crew.py`: Main entry point to run the crew and tasks.
- `requirements.txt`: Python dependencies.

## License
MIT (or specify your license)

## Acknowledgements
- [CrewAI](https://github.com/joaomdmoura/crewAI)
- [LangChain Google Gemini](https://python.langchain.com/docs/integrations/llms/google_gemini)
- [SerperDev](https://serper.dev/) 
