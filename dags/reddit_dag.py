import praw
from datetime import datetime
import json
import os

def init_reddit_client():
    return praw.Reddit(
        client_id=os.getenv('REDDIT_CLIENT_ID'),
        client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
        user_agent=os.getenv('REDDIT_USER_AGENT')
    )

def fetch_subreddit_data(subreddit_name):
    """
    Fetch data from a specific subreddit and save it to a JSON file.
    
    Args:
        subreddit_name (str): Name of the subreddit to fetch data from
        
    Returns:
        str: Path to the saved JSON file
    """
    # Initialize Reddit client
    reddit = init_reddit_client()
    
    # Fetch posts from subreddit
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    
    for post in subreddit.hot(limit=100):
        posts.append({
            'title': post.title,
            'score': post.score,
            'id': post.id,
            'url': post.url,
            'num_comments': post.num_comments,
            'created_utc': datetime.fromtimestamp(post.created_utc).isoformat(),
            'author': str(post.author),
            'upvote_ratio': post.upvote_ratio
        })
    
    # Save to JSON file with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = '/opt/airflow/data'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_file = f'{output_dir}/{subreddit_name}_{timestamp}.json'
    with open(output_file, 'w') as f:
        json.dump(posts, f)
    
    return output_file