import streamlit as st
from langchain.llms import LlamaCpp
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.callbacks.manager import CallbackManager
from langchain import PromptTemplate, LLMChain
import os

def generate_queries(questions):
    model_path = "E:/text_sql/model/sqlcoder2.Q4_K_M.gguf"

    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model 'sqlcoder2.Q4_K_M.gguf' not found in the 'models' folder.")

    llm = LlamaCpp(
        model_path=model_path,
        temperature=0.75,
        max_tokens=512,
        top_p=1,
        callback_manager=callback_manager,
        verbose=True,
    )

    prompt_template = """
    Generate a SQL query to retrieve specific information from the database.

    The database schema includes two tables:
    - `products`: Contains product details (product_id, name, price, quantity)
    - `sales`: Contains sales records (sale_id, product_id, customer_id, salesperson_id, sale_date, quantity)

    Your SQL query should answer the following question:
    "{question}"

    Please write an SQL query that retrieves the required information based on the provided schema:
    """

    prompt = PromptTemplate(template=prompt_template, input_variables=['question'])
    llm_chain = LLMChain(prompt=prompt, llm=llm)

    queries = []

    for question in questions:
        response = llm_chain.run(question)
        # Extract the query from the LLAMACPP response
        start_marker = 'llama_print_timings:'
        end_marker = response.find(start_marker)
        query = response[:end_marker].strip() if end_marker != -1 else response.strip()
        queries.append(query)

    return queries


# Define the Streamlit app
st.set_page_config(page_title="Text->SQL Chatbot", page_icon=":robot_face:")

def main():
    st.title("Text To SQL Query Generator :pencil::robot_face:")

    question_input = st.text_area("Enter your question:	:grey_question:")

    if st.button("Generate Query"):
        if not question_input:
            st.warning("Please enter a question.")
        else:
            queries = generate_queries([question_input])
            st.subheader("Generated SQL Query:")
            st.code(queries[0])

if __name__ == "__main__":
    main()
