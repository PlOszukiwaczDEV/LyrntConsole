import requests
import os
import utils.headers
import json
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Load cookies from environment variables
cookies = {
    '_TOKEN__DO_NOT_SHARE': os.getenv('TOKEN'),
    'temp-discord-token': os.getenv('temp-discord_token'),
    'cf_clearance': os.getenv('cf_clearance'),
}


def send_lynt(message: str, repostID: int = None):
    """
    Message - a message to send
    repostID - ID of the message to repost
    Images and reposting not supported for now
    """

    data = {
        'content': message
    }

    if repostID is not None:
        data['reposted'] = repostID

    # Send the POST request
    r = requests.post("https://lyntr.com/api/lynt", data=data, headers=utils.headers.lynt_headers, cookies=cookies)
    return r
def like_lynt(lyntID : int):
    """
    Like a lynt
    """

    data = json.dumps({
        "lyntId": lyntID
    })

    r = requests.post('https://lyntr.com/api/likelynt', cookies=cookies, headers=utils.headers.like_lynt_headers, data=data)
    return r
def delete_lynt(lyntID : int):
    """
    Delete a lynt
    """
    params = {
        'id': lyntID
    }

    r = requests.delete('https://lyntr.com/api/lynt', params=params, cookies=cookies, headers=utils.headers.delete_lynt_headers)
    return r
def comment_lynt(lyntID : int, commment : str):
    """
    Comment on a lynt
    """

    data = json.dumps({
        'id': lyntID,
        'content': commment
    })

    r = requests.post('https://lyntr.com/api/comment', cookies=cookies, headers=utils.headers.comment_lynt_headers, data=data)
    return r
def get_lynt(lyntID : int):
    r = requests.get(f"https://lyntr.com/api/lynt?id={lyntID}", cookies=cookies, headers=utils.headers.get_lynt_headers)
    return r
def get_comments_lynt(lyntID : int):
    r = requests.get(f"https://lyntr.com/api/comments?id={lyntID}", cookies=cookies, headers=utils.headers.get_lynt_headers)
    return r
