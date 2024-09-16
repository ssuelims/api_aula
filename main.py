from fastapi import FastAPI,HTTPException

app = FastAPI()
@app.get("/")
def index():
    return{"mensagem":"ola mundo"}