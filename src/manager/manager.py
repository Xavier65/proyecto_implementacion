from pydantic import BaseModel

class Manager:
    @classmethod
    def insert(self,table_name:str, record:BaseModel):
        try:
            record_dict = record.model_dump()
            keys = [k for k in record_dict.keys()]
            values = [v for v in record_dict.values()]
            print(f"INSERT INTO {table_name}{tuple(keys)} VALUES {tuple(values)}")
        except Exception as e:
            print(f"Error {e}")
