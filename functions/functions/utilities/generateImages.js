import createVertexAI from './createVertexAI.js';

async function generateImages(prompt) {
    // define variables
    var resp;
    var contentResponse;

    const vertexAI = createVertexAI();

    // Set up model
    const imageGenerationModel = vertexAI.preview.getGenerativeModel({
        // model: 'imagen-3.0-generate-001'
        // model: 'gemini-1.0-pro-vision'
        model: 'imagegeneration'
    });

    // try the prompt
    try {
        // Generate content using the initial prompt
        resp = await imageGenerationModel.generateContent(prompt);
        contentResponse = resp.response;

        return contentResponse;

    } catch (error) {
        console.error("Error generating content:", error);
        throw error;
    }
    
}

export default generateImages;