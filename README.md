# Twitter / X Reverse GraphQL API Client (Python)

A lightweight, session-based Python client for interacting with Twitter/X's private GraphQL and REST endpoints without requiring expensive official API subscriptions.

## 🚀 Key Features

- **No Official API Keys Required:** Operates directly via session cookies (`auth_token` and `ct0`).
- **Cursor-Based Pagination:** Efficiently traverses deeply nested reply threads, user timelines, and conversations.
- **GraphQL Query & Mutation Engine:** Native support for operations like `TweetDetail`, `UserByScreenName`, `CreateTweet`, and `CreateRetweet`.
- **Proxy Support:** Seamlessly route requests through HTTP/HTTPS and SOCKS5 residential proxy pools.
- **CSRF Token Extraction:** Automatically parses and synchronizes `x-csrf-token` headers from session states.

## 📦 Installation

```bash
pip install -r requirements.txt
cp .env.example .env
```

## 🛠️ Usage Example

```python
from twitter_client import Twitter

# Initialize with session cookie string
cookie = "auth_token=your_auth_token; ct0=your_ct0;"
client = Twitter(cookie=cookie, proxy="http://user:pass@host:port")

# Fetch replies to a tweet
thread = client.get_tweet_replies(tweet_id="1841860237225791488")
print(thread)

# Post a reply
client.create_reply(tweet_id="1841860237225791488", text="Hello from Python!")
```

## 📂 Examples

Check the `examples/` directory:
- `examples/fetch_replies.py`: How to scrape reply trees and conversation metadata.
- `examples/post_reply.py`: How to dispatch replies programmatically.
