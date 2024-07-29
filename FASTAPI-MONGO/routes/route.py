from fastapi import APIRouter,HTTPException
from models.todos import Todo
from config.database import collection_name
from schema.schemas import list_serial,individual_serial
from bson import ObjectId

router = APIRouter(tags=["CRUD-Operation"])

@router.get("/todos/")
async def get_todos():
    todos_cursor = collection_name.find()
    todos = await list_serial(todos_cursor)  
    return todos

@router.post("/create/")
async def post_todo(todo:Todo):
    result = await collection_name.insert_one(todo.dict(exclude_unset=True))
    return {"id": str(result.inserted_id)}
    
    # todo_id = collection_name.insert_one(todo.dict(exclude_unset=True)).inserted_id
    
@router.put("/update/{ID}")
async def put_todo(ID:str,todo:Todo):
    result= await collection_name.find_one_and_update(
        {"_id":ObjectId(ID)},
        {"$set":todo.dict(exclude_unset=True)},
        return_document=True)
    
    if result is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return individual_serial(result)
    
    
@router.delete("/delete/{ID}")
async def delete_todo(ID:str):
    result = await collection_name.delete_one({"_id": ObjectId(ID)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"detail": "Todo deleted"}