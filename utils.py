import json

def append_json_element(file_name: str, append_dict: dict) -> bool:
    try:
        with open(file_name, "r+", encoding="utf-8") as f:
            results = json.load(f)
                    
            results.append(append_dict)

            f.seek(0)
            json.dump(results, f, default=str, indent=4)
            return True
    except:
        raise Exception(f"{file_name} couldn't be updated")