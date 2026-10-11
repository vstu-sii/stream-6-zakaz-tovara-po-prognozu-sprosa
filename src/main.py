from fastapi import FastAPI

app = FastAPI(title="AI Store Order", version="0.1.0")


@app.get("/")
def hello():
    return {"status": "ok", "message": "AI Store Order — hello world"}


@app.get("/health")
def health():
    return {"status": "healthy"}
