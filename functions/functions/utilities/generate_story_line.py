import json
from .initialize_vertexai import initialize_vertex_ai 
from vertexai.generative_models import GenerativeModel, FunctionDeclaration, Tool 

# Initialize Vertex AI
initialize_vertex_ai()

# function to generate story line
def generate_story_line(prompt):
    # load model
    model = GenerativeModel(
        "gemini-pro",
        system_instruction = [
            "write a children's storybook story.",
            "structure the story with an introduction, eight key momemnets, and a conclusion.",
            "use simple, engaging language that is suitable for childrent",
            "Provide vivid, imaginative scene descriptions and ensure character descriptions are detailed, consistent throughout the story, and reused whenever characters reappear.",
        ],

        tools=[get_story_tools()],
    )

    # generate response 
    response = model.generate_content(
        prompt,
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
                    "description": "Provide detailed and vivid descriptions for each slide 1 to aid image generation."
                },
                "slide_2": {
                    "type": "string",
                    "description": "Slide 2 of the story"  
                },
                "slide_2_image": {
                    "type": "string",
                    "description": "Provide detailed and vivid descriptions for each slide 2 to aid image generation."  
                },
                "slide_3": {
                    "type": "string",
                    "description": "Slide 3 of the story"  
                },
                "slide_3_image": {
                    "type": "string",
                    "description": "Provide detailed and vivid descriptions for each slide 3 to aid image generation."  
                },
                "slide_4": {
                    "type": "string",
                    "description": "Slide 4 of the story"  
                },
                "slide_4_image": {
                    "type": "string",
                    "description": "Provide detailed and vivid descriptions for each slide 4 to aid image generation."  
                },
                "slide_5": {
                    "type": "string",
                    "description": "Slide 5 of the story"  
                },
                "slide_5_image": {
                    "type": "string",
                    "description": "Provide detailed and vivid descriptions for each slide 5 to aid image generation."  
                },
                "slide_6": {
                    "type": "string",
                    "description": "Slide 6 of the story"  
                },
                "slide_6_image": {
                    "type": "string",
                    "description": "Provide detailed and vivid descriptions for each slide 6 to aid image generation."  
                },
                "slide_7": {
                    "type": "string",
                    "description": "Slide 7 of the story"  
                },
                "slide_7_image": {
                    "type": "string",
                    "description": "Provide detailed and vivid descriptions for each slide 7 to aid image generation."  
                },
                "slide_8": {
                    "type": "string",
                    "description": "Slide 8 of the story"  
                },
                "slide_8_image": {
                    "type": "string",
                    "description": "Provide detailed and vivid descriptions for each slide 8 to aid image generation."  
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
    # Convert the response to a dictionary
    dict_response = response.to_dict()

    # Extract the function call arguments
    args = dict_response["candidates"][0]["content"]["parts"][0]["function_call"]["args"]

    # Structure the story
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

    # Convert to JSON string with indentation
    return json.dumps(story, indent=4)
