import { VertexAI } from '@google-cloud/vertexai';

function createVertexAI() {
    // Initialize Vertex AI client with specified project and location
    const createVertexAI = new VertexAI({
        project: '',
        location: '',
    });
    
    return createVertexAI;
}

export default createVertexAI;