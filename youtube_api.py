
from googleapiclient.discovery import build

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'YOUTUBE API KEY'
youtube = build('youtube', 'v3', developerKey=api_key)

def youtube_search(query, max_results=10, order='relevance', video_duration='any'):
    search_response = youtube.search().list(
        q=query,
        part='id,snippet',
        maxResults=max_results,
        type='video',
        videoDuration=video_duration,
        order=order
    ).execute()

    videos = []

    # Extracting information and constructing video URL
    for search_result in search_response.get('items', []):
        video_id = search_result['id']['videoId']
        videos.append({
            'title': search_result['snippet']['title'],
            'videoId': video_id,
            'url': f"https://www.youtube.com/watch?v={video_id}"
        })

    return videos

# Example of a more specific search
videos = youtube_search('oven preheating tutorial', max_results=10, order='relevance')
for video in videos:
    print(f"Title: {video['title']}, Video ID: {video['videoId']}, URL: {video['url']}")