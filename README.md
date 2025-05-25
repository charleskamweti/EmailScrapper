# YouTube Channel Finder

This Python script allows you to search YouTube channels based on a keyword (e.g., Technology, Education, Fitness) using the YouTube Data API v3. It prints the results to the console and exports them to a CSV file. The API key is securely loaded from a `.env` file.

## Features

- Search for YouTube channels by keyword
- Fetch up to 100 channels with pagination
- Export results to a `youtube_channels.csv` file
- Loads the YouTube API key securely from a `.env` file
- UTF-8 safe output handling

## Requirements

Make sure you have Python 3.7+ and install dependencies:

```
pip install google-api-python-client python-dotenv
```

## Setup

Clone the repository or download the script.

Create a .env file in the project root and add your API key:
YOUTUBE_API_KEY=your_actual_api_key_here

Run the script:
python main.py

## Output

Console: Displays each found YouTube channel's name, description, and URL.

CSV File: Saves channel details to youtube_channels.csv.

Example Output (Console)

1. Channel Name: TechWorld
   Channel ID: UC123456...
   Description: Reviews and tutorials
   URL: https://www.youtube.com/channel/UC123456...
------------------------------------------------------------

## Security Note

Do not commit your .env file or API key to public repositories.

### License

This project is licensed under the MIT License.

### Contributions

Feel free to fork the repository and submit pull requests or open issues!