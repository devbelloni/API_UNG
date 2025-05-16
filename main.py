from fastapi import FastAPI 

app = FastAPI(title="API Simples")

@app.get("/v1")
async def get_geral():
    return {"msg":"Deu certo!"}