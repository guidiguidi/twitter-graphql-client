"""
Example: Fetch all replies to a specific tweet ID using reverse GraphQL API.
"""
import os
import json
from dotenv import load_dotenv
from twitter_client import Twitter

load_dotenv()

auth_token = os.getenv("TWITTER_AUTH_TOKEN", "")
ct0 = os.getenv("TWITTER_CT0", "")
proxy = os.getenv("TWITTER_PROXY", None)

cookie_str = f"auth_token={auth_token}; ct0={ct0}"

client = Twitter(cookie=cookie_str, proxy=proxy)

# Replace with your target tweet ID (e.g. from tweet URL https://x.com/.../status/123456)
tweet_id = "1841860237225791488"

print(f"Fetching conversation thread for tweet {tweet_id}...")
try:
    resp = client.get_tweet_replies(tweet_id)
    print("Response received:")
    print(json.dumps(resp, indent=2)[:500] + "\n...[truncated]")
except Exception as e:
    print("Error:", e)
