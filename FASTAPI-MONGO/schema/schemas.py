from typing import List
from bson import ObjectId

async def list_serial(cursor) -> List[dict]:
    todos = []
    async for todo in cursor:  
        todos.append(individual_serial(todo)) 
    return todos

def individual_serial(todo) -> dict:
    
    return {
        "id": str(todo["_id"]),  
        "name": todo["name"],
        "description": todo["description"],
        "complete": todo["complete"]
    }



'''def individual_serial(todo)-> dict:
    return{
        "id":str(todo["_id"]),
        "name":todo["name"],
        "description":todo["description"],
        "complete":todo["complete"]
        
    }
    
def list_serial(todos) -> list:
    return  [individual_serial(todo) for todo in todos]'''
    
    

# def task_serial(task)-> dict:
#     return{
#         "id": str(task["_id"]),
#         "title": task["title"],
#         "description": task["description"],
#         "due_date": str(task["due_date"]),
#         "status": task["status"],
#         "priority": task["priority"],
#         "assigned_to": individual_serial(task["assigned_to"]) if task["assigned_to"] else None,
#         "subtasks": [individual_serial(subtask) for subtask in task["subtasks"]] if task["subtasks"] else None
#     }
