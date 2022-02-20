# Chap04/facebook_top_posts.py
import json
from argparse import ArgumentParser


def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--page')
    return parser

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    fname = "data/Facebook_BBC_Posts.jsonl"

    all_posts = []
    with open(fname) as f:
        for line in f:
            post = json.loads(line)
            n_likes = post['likes_count']
            n_comments = post['comments_count']
            try:
                n_shares = post['shares_count']
            except KeyError:
                n_shares = 0
            post['all_interactions'] = n_likes + n_shares + n_comments
            all_posts.append(post)
    most_liked_all = sorted(all_posts,
                            key=lambda x: x['all_interactions'],
                            reverse=True)
    most_liked = most_liked_all[0]
    message = most_liked.get('message', '-empty-')
    created_at = most_liked['posted_at']
    n_likes = most_liked['likes_count']
    n_comments = most_liked['comments_count']
    print("Post with most interactions:")
    print("Message: {}".format(message))
    print("Creation time: {}".format(created_at))
    print("Likes: {}".format(n_likes))
    print("Comments: {}".format(n_comments))
    try:
        n_shares = most_liked['shares_count']
        print("Shares: {}".format(n_shares))
    except KeyError:
        pass
    print("Total: {}".format(most_liked['all_interactions']))
