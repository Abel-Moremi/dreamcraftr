import json
from .initialize_vertexai import initialize_vertex_ai 
from vertexai.generative_models import GenerativeModel 

# Initialize Vertex AI
initialize_vertex_ai()

# function to generate story line
def generate_story_line():
    # load model
    model = GenerativeModel("gemini-1.5-flash-002")

    # generate response 
    response = model.generate_content(
        "tell me about Botswana",
    )
    
    return json.dumps(response.text)
