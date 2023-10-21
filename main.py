import os

from io import StringIO

from dotenv import load_dotenv

import streamlit as st

import openai

from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()

#defining the llm
llm = ChatOpenAI(temperature=0, model="gpt-4")

def main():
    
    st.set_page_config(page_title="Solidity to Clarity", page_icon=":robot_face:")

    with st.sidebar:
        st.title(":robot_face: Solidity to Clarity Converter")
        st.write("The converter is powered by OpenAI gpt-3.5-turbo-16k LLM")
    
        st.divider()
    
        st.caption("Made with :white_heart: by Caleb Kan, Cindy Yun, Ryan Fok, Lachlan Lai, Jeffrey Cheung, Hyunbin Jang")
        
    template = """Question: {question}
    Answer: Only output the final code in Clarity with Indentations & Comments"""

    prompt = PromptTemplate(template=template, input_variables=["question"])
    
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        string_data = stringio.read()
        query = "Convert the Solidity Code into Clarity Code" + string_data
        st.write(llm_chain.run(query))

if __name__ == "__main__":
    main()