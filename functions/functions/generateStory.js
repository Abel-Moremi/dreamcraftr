import dotenv from 'dotenv';
import { VertexAI } from '@google-cloud/vertexai';

/**
 * Generates a children's story with scene descriptions for illustrations.
 * @param {string} prompt - The text prompt to generate content.
 */
async function generateStory(prompt) {

  // Load environment variables from .env file
  dotenv.config();

  // initial prompt
  const initialPrompt = `Help create a children's storybook using the following structure: 
                        An intro: Introduce the main character, setting and theme 
                        10 slides: Each slide should have a short, engaging line or two that is suitable for children ages 3-6 
                        10 Descriptions of pictures per slide: Provide a detailed image description for each slide to guide illustration, focus on vivid colors, cute expressions, and magical or cozy elements 
                        
                        Output this in JSON format with each slide containing: 
                        slide_number: the slide's sequence from 1 to 10 
                        text: A short description of the story on this slide 
                        image_description: A description of what should appear in the illustration 
                        
                        Use this as inspiration: --> ${prompt}`;

  // Get projectId and location from environment variables
  const projectId = process.env.PROJECT_ID;
  const location =  process.env.LOCATION;

  console.log("Project ID:", projectId);
  console.log("Location:", location);

  // Initialize Vertex AI client with specified project and location
  const vertexAI = new VertexAI({
    project: 'dreamcraftr',
    location: 'us-central1',
  });

  // Set up model
  const generativeModel = vertexAI.getGenerativeModel({
    model: 'gemini-1.5-pro-002', // Specified Gemini model
  });

  // try the prompt
  try {
    const resp = await generativeModel.generateContent(initialPrompt);
    const contentResponse = resp.response;
  
    console.log("I am the goat");
    // console.log("Content Response:", contentResponse);
  
    // Parse content response to JSON if necessary
    // const jsonResponse = typeof contentResponse === 'string' ? JSON.parse(contentResponse) : contentResponse;
    // console.log("Response JSON:", jsonResponse);
  
    // Access text content
    // const text = jsonResponse.story.candidates[0].content.parts[0].text;
    // console.log("Extracted Text:", text);
  
    // Clean up any escaped quotes if necessary, and parse to final JSON format
    // const textJson = JSON.stringify(JSON.parse(text.replace(/\\"/g, '"')), null, 2);
  
    console.log("Generated Story and Image Descriptions:", JSON.stringify(contentResponse));
    return contentResponse;
  
  } catch (error) {
    console.error("Error generating content:", error);
    throw error;
  }
}

// Export function
export default generateStory;