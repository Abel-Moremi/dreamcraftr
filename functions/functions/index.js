import dotenv from 'dotenv';
import { https } from 'firebase-functions';
import generateStory from './generateStory.js';

// Load environment variables from .env file
dotenv.config();

export const generateStoryFunction = https.onRequest(async (req, res) => {
  // Validate request method
  if (req.method !== 'POST') {
    return res.status(405).send({ error: 'Method not allowed. Please use POST.' });
  }

  // Get the prompt from the request body
  const { prompt } = req.body;

  // Check if prompt is provided
  if (!prompt) {
    return res.status(400).send({ error: 'Prompt is required.' });
  }

  try {
    // Call the generateStory function with the provided prompt
    const story = await generateStory(prompt);
    // Send the generated story back in the response
    res.status(200).send(await generateStory(prompt));
  } catch (error) {
    console.error("Error in story generation:", error);
    res.status(500).send({ error: 'Error generating story.' });
  }
});