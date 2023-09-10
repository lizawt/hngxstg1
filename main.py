from fastapi import FastAPI, HTTPException
from datetime import datetime
import pytz

app = FastAPI()

@app.get("/api")
async def get_endpoint(slack_name: str, track: str):
    # Current UTC time with a +/-2 minute window
    utc_time = datetime.now(pytz.utc)

    #JSON format response
    response = {
        "slack_name": slack_name,
        "day_of_week": utc_time.strftime("%A"), 
        "current_utc_time": utc_time.strftime("%Y-%m-%dT%H:%M:%S"),
        "track": track,
        "github_file_url": "https://github.com/lizawt/hngxstg1/blob/main/main.py",
        "github_repo_url": "https://github.com/lizawt/hngxstg1",
        "status_code": 200
    }

    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
