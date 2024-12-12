from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_ollama import OllamaLLM
from pathlib import Path
import logging
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()         # Muestra logs en la consola
    ]
)

### Turn everything into classes, functions and methods ###

class DataBase():

    def __init__(self, path : str):
        self.path = path
    
    def db_check_handler(self) -> bool:
        """
        Takes a string path, turns it into Path object for better control and checks existence and correct suffix.

        Args:
            self : the Database object
                self.path (str): The path attribute.
        
        Returns:
            bool True: The file is fine.
            bool False: There's an error with the file
        """
        path = Path(self.path)
        if path.exists() == True and path.suffix == ".db":
            logging.info(f"File '{path}' exists and is a database...")
            return True
        else:
            logging.info(f"File '{path}' doesn't exist or is not a database...")
            return False

    def load_sqlite(self) -> SQLDatabase:
        """
        Loads a SQLlite database from a given arg (uri).
        
        Args:
            self.uri (str): The URI to find the SQL database.
        
        Returns:
            SQLDatabase Obj: Langchain SQLite object.
        """
        if self.db_check_handler() == True:
            logging.info(f"File '{self.path}' loaded into a SQLite...")
            return SQLDatabase.from_uri("sqlite:///" + self.path)
        else:
            logging.info(f"Error with file '{self.path}'")
            raise ValueError(f"Cannot load to SQLite Database. There is a mistake with the database file at '{self.path}'")

    ### More methods to add ###


def get_sql_response(db: SQLDatabase, examples: list, input: str) -> dict:
    """
    Loads the
    """
    example_prompt = PromptTemplate.from_template("User input: {input}\nSQL query: {query}")
    prompt = FewShotPromptTemplate(
        examples=examples[:5],
        example_prompt=example_prompt,
        prefix="You are a SQLite expert. Given an input question, create a syntactically correct SQLite query to run. Unless otherwise specificed, do not return more than {top_k} rows.\n\nHere is the relevant table info: {table_info}\n\nBelow are a number of examples of questions and their corresponding SQL queries, return only the SQL Query",
        suffix="User input: {input}\nSQL query: ",
        input_variables=["input", "top_k", "table_info"],
    )

    #print(prompt.format(input="How many artists are there?", top_k=3, table_info="foo"))

    llm_db = OllamaLLM(model="llama3.1", temperature=0)
    chain = create_sql_query_chain(llm_db, db, prompt)
    response = chain.invoke({"question": input})
    query = db.run(response)
    sql_dict = {
        "SQL Query": response,
        "Results": query
    }
    logging.info(f"The created SQL syntax is: {sql_dict}")
    return sql_dict

