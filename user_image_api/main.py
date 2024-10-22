import uvicorn

from user_image_api import run_api

api = run_api()

if __name__ == "__main__":
    uvicorn.run("main:api", host="0.0.0.0", log_level="debug", port=8000)
