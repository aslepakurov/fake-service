from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/health")
async def health():
    return "OK"


@app.post("/payload")
async def payload(request: Request):
    return request.body()
