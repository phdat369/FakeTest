from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def check_sever():
    return {
        "message": "API is running"
    }
