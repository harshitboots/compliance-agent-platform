import streamlit as st
from openai import AzureOpenAI
from databricks import sql
import os

# ---------- Azure OpenAI Client ----------

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),,
    api_version=os.getenv("AZURE_OPENAI_API_VERSION")
)

# ---------- Databricks Connection ----------

def get_transactions():

    connection = sql.connect(
        server_hostname=os.getenv("DATABRICKS_HOST"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN")
    )

    cursor = connection.cursor()

    cursor.execute("""
        SELECT transaction_id,
               customer_id,
               amount,
               location,
               merchant
        FROM fraud.transactions
        LIMIT 10
    """)

    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results


# ---------- Streamlit UI ----------

st.title("🕵️ Fraud Investigation AI Assistant")

st.write("Ask questions about fraud alerts and transactions.")

# Show latest transactions
if st.button("Load Recent Transactions"):
    data = get_transactions()
    st.write(data)

# Chat input
user_input = st.chat_input("Ask about fraud alerts...")

if user_input:

    transactions = get_transactions()

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a fraud investigation analyst helping investigate suspicious banking transactions."
            },
            {
                "role": "user",
                "content": f"""
User question:
{user_input}

Here are recent transactions:
{transactions}

Analyze them and respond clearly.
"""
            }
        ]
    )

    answer = response.choices[0].message.content

    st.write(answer)