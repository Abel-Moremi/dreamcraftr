import json
from .initialize_vertexai import initialize_vertex_ai
from vertexai.generative_models import GenerativeModel, FunctionDeclaration, Tool

# Initialize Vertex AI
initialize_vertex_ai()

# function to refine image descriptions
def refine_image_descriptions(response_json):
    # load model
    model = GenerativeModel(
        "gemini-pro",
        system_instruction = [
            'understand the story and the characters in the story',
            'replace charector names with pyhsical descriptions of the character',
            'enhance the image description with more details and optimize for image generation',
            'elaborate on the appearance, actions, and emotions of the characters in the story',
            'keep the charactor descriptions consistent throughout the story',
        ],
        tools=[get_image_tools()],
    )
    
    # generate response
    response = model.generate_content(
        json.dumps(response_json),
    )
    
    return json.dumps(response.to_dict(), indent=4)

# set up tools
def get_image_tools():
    image_tools = Tool(
        function_declarations=[
            image_func()
        ],
    )
    
    return image_tools

# define the image function
def image_func():
    image_function = FunctionDeclaration(
        name="refine_image_descriptions",
        description="Refine image descriptions",
        parameters={
            "type": "object",
            "properties": {
                "introduction_image": {
                    "type": "string",
                    "description": "Understand the story and its characters, focus on detailed image descriptions optimized for generation, elaborating on their appearance, actions, and emotions while ensuring consistency throughout.Replace charater names with description of the character."
                },
                "slide_1_image": {
                    "type": "string",
                    "description": "Understand the story and its characters, focus on detailed image descriptions optimized for generation, elaborating on their appearance, actions, and emotions while ensuring consistency throughout. Replace charater names with description of the character."
                },
                "slide_2_image": {
                    "type": "string",
                    "description": "Understand the story and its characters, focus on detailed image descriptions optimized for generation, elaborating on their appearance, actions, and emotions while ensuring consistency throughout. Replace charater names with description of the character."
                },
                "slide_3_image": {
                    "type": "string",
                    "description": "Understand the story and its characters, focus on detailed image descriptions optimized for generation, elaborating on their appearance, actions, and emotions while ensuring consistency throughout. Replace charater names with description of the character."
                },
                "slide_4_image": {
                    "type": "string",
                    "description": "Understand the story and its characters, focus on detailed image descriptions optimized for generation, elaborating on their appearance, actions, and emotions while ensuring consistency throughout. Replace charater names with description of the character."
                },
                "slide_5_image": {
                    "type": "string",
                    "description": "Understand the story and its characters, focus on detailed image descriptions optimized for generation, elaborating on their appearance, actions, and emotions while ensuring consistency throughout. Replace charater names with description of the character."
                },
                "slide_6_image": {
                    "type": "string",
                    "description": "Understand the story and its characters, focus on detailed image descriptions optimized for generation, elaborating on their appearance, actions, and emotions while ensuring consistency throughout. Replace charater names with description of the character."
                },
                "slide_7_image": {
                    "type": "string",
                    "description": "Understand the story and its characters, focus on detailed image descriptions optimized for generation, elaborating on their appearance, actions, and emotions while ensuring consistency throughout. Replace charater names with description of the character."
                },
                "slide_8_image": {
                    "type": "string",
                    "description": "Understand the story and its characters, focus on detailed image descriptions optimized for generation, elaborating on their appearance, actions, and emotions while ensuring consistency throughout. Replace charater names with description of the character."
                },
                "conclusion_image": {
                    "type": "string",
                    "description": "Understand the story and its characters, focus on detailed image descriptions optimized for generation, elaborating on their appearance, actions, and emotions while ensuring consistency throughout. Replace charater names with description of the character."
                },
            },
            "required": [
                "introduction_image",
                "slide_1_image",
                "slide_2_image",
                "slide_3_image",
                "slide_4_image",
                "slide_5_image",
                "slide_6_image",
                "slide_7_image",
                "slide_8_image",
                "conclusion_image",
            ],
        },
    )
    
    return image_function 
        
