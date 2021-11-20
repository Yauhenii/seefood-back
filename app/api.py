from fastapi import FastAPI

app = FastAPI()

@app.get("/getAllFood/")
async def get_all_food():
    return{'food':'all_food_stub'}