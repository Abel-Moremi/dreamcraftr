function cleanJson(data) {
    // Check if the data starts with ```json and ends with ```
    if (typeof data === 'string' && data.startsWith('```json') && data.endsWith('```')) {
      // Remove the markers
      data = data.slice(7, -3).trim();
    }
  
    // Parse the JSON string if it's still a string after marker removal
    if (typeof data === 'string') {
      data = JSON.parse(data);
    }
  
    // Recursive cleaning function
    function clean(data) {
      if (Array.isArray(data)) {
        return data.map(clean);
      } else if (typeof data === 'object' && data !== null) {
        const cleanedObject = {};
        for (const key in data) {
          cleanedObject[key] = clean(data[key]);
        }
        return cleanedObject;
      } else if (typeof data === 'string') {
        return data.replace(/\s+/g, ' ').trim();
      }
      return data;
    }
  
    return clean(data);
  }
  
// export function
export default cleanJson;