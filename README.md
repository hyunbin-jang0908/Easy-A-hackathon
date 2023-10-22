# Introducing Clarevolvers
This project was specifically crafted to bridge the gap between two prominent smart contract languages: Solidity and Clarity. By harnessing the capabilities of Large Language Models and leveraging advanced Natural Language Processing techniques, the initiative offers a seamless transformation of smart contracts written in Solidity into their Clarity equivalents. Such a conversion not only broadens the application spectrum for developers but also underscores the potential of integrating machine learning with blockchain technologies.
## Table of Contents  
- [Introducing Clarevolvers](#introducing-clarevolvers)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Installation](#installation)
    - [Technical Initialization](#technical-initialization)
    - [Functionality](#functionality)
  - [Contributors](#contributors)

## Getting Started  
### Installation 
To explore the capability of instantly converting your smart contracts from Solidity Code to Clarity Code, it's remarkably simple. Just [click on this link](https://sol2clar.streamlit.app/) and you'll be on your way to a smooth transition between the two coding languages.

### Technical Initialization
- Libaries to install: `os`, `io`, `streamlit`, `streamlit-js-eval`, `python-dotenv`, `openai-schema-pydantic`, `openai`, `langchainplus-sdk`, `langchain`
- Defining the Large Language Model
	```python
	llm  =  ChatOpenAI(temperature=0, model="gpt-4")
	```

### Functionality
   - **Description**: We are establishing a precise query template for the Large Language Model (LLM) to ensure that its output is singularly focused on the conversion from Solidity to Clarity Code. By refining the input parameters and eliminating ambiguities, this template aims to mitigate randomness in the model's responses, driving more consistent and targeted results tailored to the specific needs of Solidity to Clarity Code conversion.
   - **Technical**: 
		- `Promt Template Implementation`
			 ```python
			template = """Question: {question}
			Answer: Only output the final code in Clarity with Indentations & Comments"""
			prompt = PromptTemplate(template=template, input_variables=["question"])
			llm_chain = LLMChain(prompt=prompt, llm=llm)
			```
   - **Description**: This configuration defines the front-end button functionality of the website. When a user uploads a file with the `.sol` extension, the system triggers an extraction process to gather all data within the file. This data is then channeled through the Large Language Model, which undertakes the task of converting the Solidity code into Clarity Code. Upon successful conversion, the system generates a new file with the `.clar` extension, which is then made available to the user for download.
   - **Technical**: 
		- `Main Function Implementation`
			 ```python
			uploaded_file = st.file_uploader("Upload `.sol` file here", type="sol")
			if  uploaded_file  is  not  None:
			
				stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
				string_data = stringio.read()
				
				query = "Convert the Solidity Code into Clarity Code \n"  +  string_data

				with get_openai_callback() as cb:
					response = llm_chain.run(query)
					st.code(response, language='clarity')
					st.code("This message costed $" + str(round(cb.total_cost, 4)), language='python')
					st.download_button(label=":page_facing_up: Download code as `.clar`", data=response, file_name=(str(uploaded_file.name) + ".clar"))
			```

    
## Contributors
The project was skillfully designed by a talented team consisting of `Cindy Yun`, `Ryan Fok`, `Caleb Kan`, `Hyunbin Jang`, `Jeffrey Cheung`, and `Lachlan Lai`. Created as an entry for the EasyA x Stacks Hackathon, it was tailored for the AI track of the event. The innovative and novel ideas presented by the team led to the project's recognition as the winning product, a testament to their combined expertise and commitment.