from fastapi import FastAPI

app = FastAPI()


@app.post("/event_git")
async def event_git():
    return {"message": "Hello World"}
