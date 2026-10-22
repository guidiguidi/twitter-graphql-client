"""
Example: Send a reply to a tweet using reverse GraphQL API mutations.
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

tweet_id = "1841860237225791488"
text = "Great point!"

print(f"Posting reply to tweet {tweet_id}...")
try:
    resp = client.create_reply(tweet_id=tweet_id, text=text)
    print("Reply result:", json.dumps(resp, indent=2))
except Exception as e:
    print("Error:", e)
