from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import logging
from SQL_Tools import DataBase, get_sql_response
import json

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()         # Muestra logs en la consola
    ]
)

class Assistant:

    def __init__(self, input: str, sql_dict: dict, model: str = "llama3.1"):
        self.model = model
        self.sql_dict = sql_dict
        self.input = input
        self.prompt = self.get_prompt()
        self.llm = OllamaLLM(model=self.model, temperature=0.5)

    def get_response(self) -> str:
        model = self.llm
        return model.invoke(self.prompt)

    def get_prompt(self) -> str:
        template = """You're a Book Finder assistant.
        You will be given a user question and a dictionary with a SQL query and response.
        Your task is to generate a response to answer the question based in all given information.
        Use friendly language and answer briefly to the question.

        Question: {input}
        SQL Dictionary: {sql_dict}

        Your Answer:
        """
        prompt_template = PromptTemplate.from_template(template)
        return prompt_template.format(input=self.input, sql_dict=self.sql_dict)

with open('./data/examples.json', 'r') as file:
    examples = json.load(file)

db_path = "./database/bookstore.db"
db = DataBase(db_path)
sqlite_db = db.load_sqlite()

input = "Do you have Ryan Holiday books?"
sql_response= get_sql_response(db=sqlite_db, examples=examples, input=input)

llm = Assistant(input=input, sql_dict=sql_response)

#print(llm.prompt)
print(llm.get_response())


