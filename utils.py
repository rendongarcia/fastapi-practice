# Python
import json
from typing import List

# FastAPI
from fastapi import HTTPException, status, logger

def append_json_element(file_name: str, append_dict: dict) -> bool:
    try:
        with open(file_name, "r+", encoding="utf-8") as f:
            results = json.load(f)
                    
            results.append(append_dict)

            f.seek(0)
            json.dump(results, f, default=str, indent=4)
            return True
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"{file_name} couldn't be updated")


def search_json_element(file_name: str, column_search: str, id_search: str) -> dict:
    try:
        with open(file_name, "r+", encoding="utf-8") as f:
            results = json.load(f)
            
            for data in results:
                if data[column_search] == id_search:
                    return data            
            return None
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error while searching id: {id_search}")


def search_and_update_json_element(file_name: str, column_search: str, id_search: str, replace_dict: dict) -> dict:
    try:
        with open(file_name, "r+", encoding="utf-8") as f:
            results = json.load(f)
            
            for data in results:
                if data[column_search] == id_search:
                    replace_dict[column_search] = id_search
                    results[results.index(data)] = replace_dict
                    with open(file_name, "w", encoding="utf-8") as f2:
                        f2.seek(0)
                        json.dump(results, f2, default=str, indent=4)
                        
                        return replace_dict
            return None
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error while searching id: {id_search}")
    

def search_and_delete_json_element(file_name: str, column_search: str, id_search: str) -> dict:
    try:
        with open(file_name, "r+", encoding="utf-8") as f:
            results = json.load(f)
            for data in results:
                if data[column_search] == id_search:                    
                    del results[results.index(data)]
                    with open(file_name, "w", encoding="utf-8") as f2:
                        f2.seek(0)
                        json.dump(results, f2, default=str, indent=4)
                        return data
            return None
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error while searching id: {id_search}")
    