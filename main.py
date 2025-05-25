from googleapiclient.discovery import build
import sys
sys.stdout.reconfigure(encoding='utf-8')

# YouTube API Key
API_KEY = "AIvaSyBFCpsFM7Lv2wAy4V0GjYVMfHYBQ2OBjSc"

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
            maxResults=min(50, total_results - len(channels)),  # API allows max 50 per request
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
                break  # Stop on reaching the requested count

        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break  # No more results available

    return channels


# Fetch 20 channels in the "Technology" category
category = "Technology"  # Change to your desired category
channels = search_channels_by_keyword(category, total_results=20)

# Print results
print("\n🔹 YouTube Channels Found:\n")
for idx, channel in enumerate(channels, start=1):
    print(f"{idx}. Channel Name: {channel['Channel Name']}")
    print(f"   Channel ID: {channel['Channel ID']}")
    print(f"   Description: {channel['Description']}")
    print(f"   URL: {channel['Channel URL']}")
    print("-" * 60)
