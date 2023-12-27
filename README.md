# Text2SQL_prompt
A Generative AI based project deployed through Streamlit Framework.

# Application:

![image](https://github.com/mr-nobody15/Text2SQL_prompt/assets/70313481/8d3e9e8f-9c02-4faa-a557-8a8f81676cc6)


# Installation:

Before proceeding to steps make sure you have: Anaconda Navigator, VS Code with C++ Redistributable as LLamaCPP utilised cpp compiler.
If you have anaconda environment and vscode: If an error arises "Error while installing python package: llama-cpp-python" then,
try to install c++ as an extension in vscode and try to run the code
OR
Reinstall VS Code with c++ build tools and other necessary tools, here's a reference:

![image](https://github.com/mr-nobody15/Text2SQL_prompt/assets/70313481/bfbb5143-2c41-4917-ab4a-ea429df170ec)

Just in case you don't have VS installer, you can find it with Download Build Tools from visualstudio.microsoft.com/visual-cpp-build-tools.

Then, use the following command:
!pip install llama-cpp-python 

# Setup:
Additionally, create a separate folder named model and download the llm model (Quantized) from huggingface - sqlcoder
Link - https://huggingface.co/TheBloke/sqlcoder2-GGUF/blob/main/sqlcoder2.Q4_K_M.gguf

Then change the path in "model_path" variable which is present inside the function.

## Environment:
Create a new environment after anaconda installation - conda create -n <your_env_name> and also activate the environment - conda activate <your_env_name> then,
Use the command:"pip install -r requirements" to install all necessary dependencies.

The commands are to be run in anaconda prompt after creating and activating the environment

# About:
This is an Generative AI based Application which is deployed through Streamlit Framework, based on the prompt we define answers are seen accordingly.
This is a "Prompt" based chatbot or Prompt Engineering based application utilised to convert a question in the form of query to a SQl (Structured Query Language) which is used to interact with the metabases and other databases. This is a local based application where we do not require any APIs or additional information to access or share our information thus putting a privacy of our personal information.

# Why this selected model?
![image](https://github.com/mr-nobody15/Text2SQL_prompt/assets/70313481/d1bacd5a-db55-4f7c-bdeb-c2fcf0c69649)

According to the above diagram, gpt-4 a closed Model requires API key and other details to access it whereas our selected model performance is about as good as the predecessor of GPT-4 and since it is open-sourced we can use it as a local model for any text generation related tasks.


