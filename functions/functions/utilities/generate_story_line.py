import json
from .initialize_vertexai import initialize_vertex_ai 
from vertexai.generative_models import GenerativeModel, FunctionDeclaration, Tool 

# Initialize Vertex AI
initialize_vertex_ai()

# function to generate story line
def generate_story_line():
    # load model
    model = GenerativeModel(
        "gemini-pro",
        system_instruction=[
            "create a childrenn's storybook story",
            "The story should have an introduction, eisght key moments, and a conclution",
            "the story should be in written in simple and engaging simple langauge for kids"
        ],
        tools=[get_story_tools()],
    )

    # generate response 
    response = model.generate_content(
        "Help me create a short story based on a duck who is kind and helpful.",
    )
    
    return restructure_response(response)

def get_story_tools():
    story_tools = Tool(
        function_declarations=[
            story_func()
        ],
    )
    
    return story_tools

def story_func():
    get_story_func = FunctionDeclaration(
        name="get_story",
        description="Generate a story",
        parameters={
            "type": "object",
            "properties": {
                "introduction": {
                    "type": "string",
                    "description": "Introduction to the story"
                },
                "introduction_image": {
                    "type": "string",
                    "description": "Image description for the introduction"
                },
                "slide_1": {
                    "type": "string",
                    "description": "Slide 1 of the story"
                },
                "slide_1_image": {
                    "type": "string",
                    "description": "Slide 1 image description"
                },
                "slide_2": {
                    "type": "string",
                    "description": "Slide 2 of the story"  
                },
                "slide_2_image": {
                    "type": "string",
                    "description": "Slide 2 image description"  
                },
                "slide_3": {
                    "type": "string",
                    "description": "Slide 3 of the story"  
                },
                "slide_3_image": {
                    "type": "string",
                    "description": "Slide 3 image description"  
                },
                "slide_4": {
                    "type": "string",
                    "description": "Slide 4 of the story"  
                },
                "slide_4_image": {
                    "type": "string",
                    "description": "Slide 4 image description"  
                },
                "slide_5": {
                    "type": "string",
                    "description": "Slide 5 of the story"  
                },
                "slide_5_image": {
                    "type": "string",
                    "description": "Slide 5 image description"  
                },
                "slide_6": {
                    "type": "string",
                    "description": "Slide 6 of the story"  
                },
                "slide_6_image": {
                    "type": "string",
                    "description": "Slide 6 image description"  
                },
                "slide_7": {
                    "type": "string",
                    "description": "Slide 7 of the story"  
                },
                "slide_7_image": {
                    "type": "string",
                    "description": "Slide 7 image description"  
                },
                "slide_8": {
                    "type": "string",
                    "description": "Slide 8 of the story"  
                },
                "slide_8_image": {
                    "type": "string",
                    "description": "Slide 8 image description"  
                },
                "conclusion": {
                    "type": "string",
                    "description": "summary of lesson learned and theme of the story"
                },
                "conclusion_image": {
                    "type": "string",
                    "description": "Image description for the conclusion"
                } 
            },
            "required": [
                "introduction",
                "introduction_image",
                "slide_1",
                "slide_1_image",
                "slide_2",
                "slide_2_image",
                "slide_3",
                "slide_3_image",
                "slide_4",
                "slide_4_image",
                "slide_5",
                "slide_5_image",
                "slide_6",
                "slide_6_image",
                "slide_7",
                "slide_7_image",
                "slide_8",
                "slide_8_image",
                "conclusion",
                "conclusion_image"
            ]
        }
    )
    return get_story_func

# a function to restructure response from Vertex AI
def restructure_response(response):
    dict_response = response.to_dict()
    args = dict_response["candidates"][0]["content"]["parts"][0]["function_call"]["args"]
    
    story = {
        "story": {
            "introduction": {
                "text": args["introduction"],
                "image": args["introduction_image"]
            },
            "slides": [
                {"number": 1, "text": args["slide_1"], "image": args["slide_1_image"]},
                {"number": 2, "text": args["slide_2"], "image": args["slide_2_image"]},
                {"number": 3, "text": args["slide_3"], "image": args["slide_3_image"]},
                {"number": 4, "text": args["slide_4"], "image": args["slide_4_image"]},
                {"number": 5, "text": args["slide_5"], "image": args["slide_5_image"]},
                {"number": 6, "text": args["slide_6"], "image": args["slide_6_image"]},
                {"number": 7, "text": args["slide_7"], "image": args["slide_7_image"]},
                {"number": 8, "text": args["slide_8"], "image": args["slide_8_image"]}
            ],
            "conclusion": {
                "text": args["conclusion"],
                "image": args["conclusion_image"]
            }
        }
    }
    
    # convert to JSON
    return json.dumps(story, indent=4)