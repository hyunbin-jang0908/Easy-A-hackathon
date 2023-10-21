import os

from io import StringIO

from dotenv import load_dotenv

import streamlit as st

import openai

from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.callbacks import get_openai_callback

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()

#defining the llm
llm = ChatOpenAI(temperature=0, model="gpt-4")

def main():
    
    st.set_page_config(page_title="Solidity to Clarity", page_icon=":computer:")

    with st.sidebar:
        st.title("Solidity to Clarity Converter")
        st.write("The converter is powered by OpenAI GPT-4")
    
        st.divider()
    
        st.caption("Made with :white_heart: by Caleb Kan, Cindy Yun, Ryan Fok, Lachlan Lai, Jeffrey Cheung, Hyunbin Jang")
        
    template = """Question: {question}
    Answer: Only output the final code in Clarity with Indentations & Comments"""

    prompt = PromptTemplate(template=template, input_variables=["question"])
    
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    
    uploaded_file = st.file_uploader("Upload `.sol` files here", type="sol")
    if uploaded_file is not None:
        
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        string_data = stringio.read()
        
        query = "Convert the Solidity Code into Clarity Code \n" + string_data
        
        with get_openai_callback() as cb:
            response = llm_chain.run(query)
            st.code(response, language='clarity')
            st.code("This message costed $" + str(round(cb.total_cost, 4)), language='python')
            st.download_button(label=":page_facing_up: Download code as `.clar`", data=response, file_name=(str(uploaded_file.name) + ".clar"))

if __name__ == "__main__":
    main()