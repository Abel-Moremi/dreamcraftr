import os
import vertexai
from dotenv import load_dotenv

load_dotenv()

def initialize_vertex_ai():
    project = os.getenv('PROJECT_ID')
    region = os.getenv('LOCATION')
    vertexai.init(
        project=project,
        location=region,
    )