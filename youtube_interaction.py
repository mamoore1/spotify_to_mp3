from googleapiclient.discovery import build

# API key
API_KEY = "AIzaSyA7w4Yj_PjfhKrU0TpfWwq7sHkgIIDpKFk"

# API service name and version
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"

# Base video watch url
BASE_URL = "https://www.youtube.com/watch?v="

def video_search(search_term):
    """
    A function which takes in a string search term, looks up that search term through the Youtube API and returns a
    link to the first video in the list of searched videos

    :param search_term: a string containing terms to be searched on youtube
    :return: a string holding the url of a video
    """
    # Building youtube request
    youtube = build(API_SERVICE_NAME, API_VERSION, developerKey=API_KEY)
    request = youtube.search().list(
        part="snippet",
        maxResults=5,
        q=search_term,
    )
    response = request.execute()['items']

    # Assign an empty string to hold the video id
    video_id = ''

    # Checking that the current search result is a video, rather than a channel
    # While there are responses in the list
    while response:
        # Check whether the list entry is a video
        if response[0]['id']['kind'] == 'youtube#video':
            # If so, set video_id equal to the id of the video
            video_id = response[0]['id']['videoId']
            # Break out of the loop
            break;
        # Otherwise remove the entry from the list
        else:
            response.pop(0)
    # If a video has been found
    if video_id:
        # Combine the watch url and the video id
        video_url = BASE_URL + video_id
        # Return the video id
        return video_url
    # Otherwise print that the video was not found
    print("Video not found")
    # Return from the function
    return