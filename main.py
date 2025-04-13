from http.client import HTTPException

from fastapi import FastAPI, Request, HTTPException
from starlette.responses import JSONResponse

app = FastAPI()

@app.post("/webhook", response_model=None)
async def webhook(request: Request):
    try:
        # Parse the JSON payload from Dialogflow
        payload = await request.json()

        # Log the received payload (for debugging purposes)
        print("Received payload:", payload)

        # Extract the intent name from the payload
        intent_name = payload.get('queryResult', {}).get('intent', {}).get('displayName', '')
        print(intent_name)
        # Prepare a simple response based on the intent
        if intent_name == "Route Intent":
            response_text = "Your expense will be this"
        else:
            response_text = "I'm not sure how to respond to that."

        # Return the response to Dialogflow
        return JSONResponse(content={
            "fulfillmentText": response_text
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Dummy root endpoint to test if the server is running
@app.get("/")
def read_root():
    return {"message": "FastAPI server is running!"}