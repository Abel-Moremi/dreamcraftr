import generateText from './utilities/generateText.js';
import generateImages from './utilities/generateImages.js';

/**
 * Generates a children's story with scene descriptions for illustrations.
 * @param {string} prompt - The text prompt to generate content.
 */
async function generateStory(prompt) {

  // return await generateText(prompt);
  return await generateImages(prompt);
}

// Export function
export default generateStory;