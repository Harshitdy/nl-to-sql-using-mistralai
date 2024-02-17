from langchain_together import Together
from langchain.sql_database import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
import os
from dotenv import load_dotenv

load_dotenv()

together_api_key = os.environ['TOGETHER_API_KEY']

llm = Together(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    temperature=0.7,
    max_tokens=128,
    top_k=1,
    together_api_key= together_api_key
)


db_user = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']
db_host = os.environ['DB_HOST']
db_name = os.environ['DB_NAME']

db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}", sample_rows_in_table_info = 3)
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose = True)
qn1 = db_chain("If we have to sell all the Levi’s T-shirts today. How much revenue our store will generate without discount?")
print(qn1)