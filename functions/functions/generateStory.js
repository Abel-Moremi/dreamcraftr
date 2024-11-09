import generateText from './utilities/generateText.js';

/**
 * Generates a children's story with scene descriptions for illustrations.
 * @param {string} prompt - The text prompt to generate content.
 */
async function generateStory(prompt) {
  return await generateText(prompt);
}

// Export function
export default generateStory;