import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper,WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun,DuckDuckGoSearchRun
from langchain.agents import initialize_agent,AgentType
from langchain.callbacks import StreamlitCallbackHandler
import os

from dotenv import load_dotenv
load_dotenv()
groq_api_key=os.getenv('GROQ_API_KEY')

#Arxiv wrapper:

arxiv_wrapper=ArxivAPIWrapper(top_k_results=1,doc_content_chars_max=200)
arxiv=ArxivQueryRun(api_wrapper=arxiv_wrapper)

#wikipedia wrapper:
api_wrapper=WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=200)
wiki=WikipediaQueryRun(api_wrapper=api_wrapper)

search=DuckDuckGoSearchRun(name='Search')
st.title('langchain -Chat with search')


#sidebar for settings:
st.sidebar.title('settings')
api_key=st.sidebar.text_input('Enter your Groq API key:',type='password')

if "messages" not in st.session_state:
    st.session_state['messages']=[
        {'role':'assistant','content':'hi,Iam a chat bot who can search the web.how can i help you?'}

    ]
for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])

if prompt:=st.chat_input(placeholder='what is machine learning'):
    st.session_state.messages.append({'role':'user','content':prompt})
    st.chat_message('user').write(prompt)

    llm=ChatGroq(groq_api_key=groq_api_key,name='Llama3-8b-8192',streaming=True)
    tools=[search,arxiv,wiki]

    search_agents=initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,handle=True)
    with st.chat_message('assistant'):
        st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
        response=search_agents.run(st.session_state.messages,callbacks=[st_cb])
        st.session_state.messages.append({'role':'assistant','content':response})
        st.write(response)



