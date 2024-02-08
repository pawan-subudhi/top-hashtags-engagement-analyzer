from fastapi import FastAPI, HTTPException, Query
from backend.api.endpoints import hashtags_router
import uvicorn

app = FastAPI()

# OpenAPI Documentation
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
