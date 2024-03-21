#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

// Define the URL for the Star Wars API (SWAPI) films endpoint with the film ID from the command line argument
const filmUrl = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`;

// Make a request to the SWAPI films endpoint
request(filmUrl, (error, response, body) => {
  // Check for errors in the HTTP request
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Parse the JSON response from the SWAPI films endpoint
  const film = JSON.parse(body);

  // Create an object to map character URLs to their names
  const urlToName = {};

  // Iterate through each character URL in the film's character list
  film.characters.forEach(characterUrl => {
    // Make a request to the individual character's endpoint
    request(characterUrl, (error, response, body) => {
      // Check for errors in the HTTP request
      if (error) {
        console.error('Error:', error);
        return;
      }

      // Parse the JSON response from the character's endpoint
      const character = JSON.parse(body);

      // Map the character's URL to their name in the object
      urlToName[character.url] = character.name;

      // Check if we have retrieved names for all characters
      if (Object.keys(urlToName).length === film.characters.length) {
        // Iterate through each character URL and print their names
        film.characters.forEach(characterUrl =>
          console.log(urlToName[characterUrl])
        );
      }
    });
  });
});
