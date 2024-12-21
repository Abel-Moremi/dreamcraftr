from firebase_functions import https_fn
from firebase_admin import initialize_app
from generate_story import generate_story_book

initialize_app()


@https_fn.on_request()
def story_book(req: https_fn.Request) -> https_fn.Response:
     return https_fn.Response(generate_story_book(), mimetype='application/json')