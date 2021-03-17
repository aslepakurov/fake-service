from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/health")
async def health():
    return "OK"


@app.post("/payload1")
async def payload(request: Request):
    print("Some additional funtionality")
    body_str = await request.body()
    return str(body_str.decode("UTF-8"))
