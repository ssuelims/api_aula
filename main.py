from fastapi import FastAPI,HTTPException,Depends,status

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()
outh2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
def index():
    return{"mensagem":"ola mundo"}

@app.post("/token")
async def logar(data: OAuth2PasswordRequestForm=Depends()):
    if data.username =="kaua"and data.password == "senai123":
        return{"acces_": "supersecreto","token_type":"bearer"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="credenciais invalida")