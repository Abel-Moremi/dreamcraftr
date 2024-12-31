import logging
import json
from firebase_functions import https_fn
from firebase_admin import initialize_app
from generate_story import generate_story_book

initialize_app()


@https_fn.on_request()
def story_book(req: https_fn.Request) -> https_fn.Response:
    try:
        # Parse JSON body
        body = json.loads(req.get_data(as_text=True))
        prompt = body.get("prompt")
    except (ValueError, TypeError):
        return https_fn.Response("Invalid JSON body", status=400)
    
    if not prompt:
        return https_fn.Response("Please provide a prompt", status=400)
    
    # Generate the story and return it as JSON
    return https_fn.Response(generate_story_book(prompt), mimetype='application/json')