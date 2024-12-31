from utilities.generate_story_line import generate_story_line
from utilities.refine_image_descriptions import refine_image_descriptions

def generate_story_book(prompt):
    print("This is the Prompt ---> " + prompt)
    storyline = generate_story_line(prompt=prompt)
    storyline_refined = refine_image_descriptions(storyline)
    
    return update_image_descriptions(storyline, storyline_refined)

# function to update image descriptions
def update_image_descriptions(story_json, descriptions_json):
    # Extract descriptions from the second JSON
    descriptions = descriptions_json["candidates"][0]["content"]["parts"][0]["function_call"]["args"]

    # Update the introduction image description
    story_json["story"]["introduction"]["image"] = descriptions["introduction_image_description"]
    
    # update the conclusion image description
    story_json["story"]["conclusion"]["image"] = descriptions["conclusion_image"]

    # Update the slides image descriptions
    for slide in story_json["story"]["slides"]:
        key = f"slide_{slide['number']}_image"
        if key in descriptions:
            slide["image"] = descriptions[key]

    return story_json