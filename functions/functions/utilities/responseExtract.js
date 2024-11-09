function responseExtract(jsonData) {
    // Access the candidates array within the story object
    const candidates = jsonData.candidates;
    
    // Iterate through each candidate's content
    for (const candidate of candidates) {
        // Get the parts array where the text content is located
        const parts = candidate.content.parts;
        
        // Iterate through each part and check if it contains "text"
        for (const part of parts) {
            if (part.text) {
                // Extract and return the text
                return part.text;
            }
        }
    }
    
    // Return null if no text was found
    return null;
}

// export function
export default responseExtract;