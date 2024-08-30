# LangChain-Powered Chatbot with Web Search Capabilities

This project showcases a chatbot built using LangChain, equipped with web search functionality to provide precise answers to user queries. Powered by Groq's advanced NLP capabilities and integrated with Wikipedia, this chatbot offers an enhanced conversational experience.

![Screenshot of the Chatbot Interface](Screenshot%202024-08-29%20185809.png)

## Project Structure

```
project-directory/ 
│ ├── app.py 
├── requirements.txt 
├── .env 
├── README.md 
├── LICENSE 
├── .gitignore 
└── Screenshot_2024-08-29_185809.png
```


## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.8 or higher
- Pip (Python package installer)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/langchain-chatbot-web-search.git
cd langchain-chatbot-web-search
```

2. Install the required Python packages:

```bash 
pip install -r requirements.txt
```

3. Set up your environment variables in the `.env` file:

```bash
GROQ_API_KEY=your_groq_api_key
```

1. Replace the placeholder with your actual Groq API key.

2. Running the Application
3. Ensure your `.env` file is properly configured with your Groq API key.

4. Run the Streamlit application:

```bash
streamlit run app.py
```
- Open your web browser and go to http://localhost:8501 to interact with the chatbot.

## Example Usage
- Enter a query such as "What is machine learning?".
- The chatbot will search Wikipedia and return a concise answer based on the retrieved information.
- The interaction history is displayed, showing the query and the response.

## Integration Details

- `LangChain`: Manages the conversation flow and integrates with external APIs like Wikipedia.
- `Groq API`: Provides high-performance NLP capabilities for processing user queries.
- `Streamlit`: Powers the interactive front-end for the chatbot, providing a seamless user experience.

## Files

- `app.py`: The main Python script that sets up the Streamlit interface, handles user input, and integrates with LangChain and Groq.
- `requirements.txt`: Lists all the Python dependencies needed to run the application.
- `.env`: Contains the API key for Groq. This file should not be included in version control.
- `README.md`: This file, providing an overview of the project.
- `LICENSE`: The project's license, specifying how others may use the code.
- `.gitignore`: Specifies files and directories that should be ignored by Git, such as the .env file and any other sensitive information.
- `Screenshot_2024-08-29_185809.png`: A screenshot of the chatbot interface, included for reference.

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.

## .gitignore
The following files are ignored in version control:

```bash
.env
__pycache__/
*.pyc
*.pyo
*.pyd

```

## Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgments
- Thanks to LangChain for providing the tools to build conversational AI.
- Thanks to Groq for powering the chatbot with advanced NLP capabilities.
- Thanks to Streamlit for offering an easy-to-use platform for building interactive web applications.
