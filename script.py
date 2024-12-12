from SQL_Tools import DataBase, get_sql_response
import json

#####

with open('./data/examples.json', 'r') as file:
    examples = json.load(file)

db_path = "./database/bookstore.db"

#db_pt = Path(db_path)
#print(db_pt.exists())
#print(db_pt.suffix)

db = DataBase(db_path)
sqlite_db = db.load_sqlite()
input = "Which Adam Grant books do you have?"
sql_response= get_sql_response(db=sqlite_db, examples=examples, input=input)
print(type(sql_response))
print(sql_response)



