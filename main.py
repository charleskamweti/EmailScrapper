import sys
import csv
import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Configure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")

def search_channels_by_keyword(keyword, total_results=100):
    """Fetch YouTube channels based on a keyword (category) with pagination."""
    youtube = build("youtube", "v3", developerKey=API_KEY)
    
    channels = []
    next_page_token = None

    while len(channels) < total_results:
        request = youtube.search().list(
            q=keyword,  
            type="channel",
            part="snippet",
            maxResults=min(50, total_results - len(channels)),
            pageToken=next_page_token
        )
        response = request.execute()

        for item in response.get("items", []):
            channel_name = item["snippet"]["channelTitle"]
            channel_id = item["id"]["channelId"]
            description = item["snippet"]["description"]
            channel_url = f"https://www.youtube.com/channel/{channel_id}"

            channels.append({
                "Channel Name": channel_name,
                "Channel ID": channel_id,
                "Description": description,
                "Channel URL": channel_url
            })

            if len(channels) >= total_results:
                break

        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break

    return channels

def export_to_csv(channels, filename="youtube_channels.csv"):
    """Export channel list to a CSV file."""
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["Channel Name", "Channel ID", "Description", "Channel URL"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for channel in channels:
            writer.writerow(channel)

# --- Run the tool ---
category = "Technology"
channels = search_channels_by_keyword(category, total_results=20)

print("\n🔹 YouTube Channels Found:\n")
for idx, channel in enumerate(channels, start=1):
    print(f"{idx}. Channel Name: {channel['Channel Name']}")
    print(f"   Channel ID: {channel['Channel ID']}")
    print(f"   Description: {channel['Description']}")
    print(f"   URL: {channel['Channel URL']}")
    print("-" * 60)

# Export to CSV
export_to_csv(channels)
print("\n Channels exported to 'youtube_channels.csv'")
