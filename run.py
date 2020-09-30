import praw
import configparser
from mal import AnimeSearch
import re


config = configparser.ConfigParser()
config.read('conf.ini')
reddit_user = config['REDDIT']['reddit_user']
reddit_pass = config['REDDIT']['reddit_pass']
reddit_client_id = config['REDDIT']['reddit_client_id']
reddit_client_secret = config['REDDIT']['reddit_client_secret']
reddit_target_subreddit = config['REDDIT']['reddit_target_subreddit']

reddit = praw.Reddit(
    username=reddit_user,
    password=reddit_pass,
    client_id=reddit_client_id,
    client_secret=reddit_client_secret,
    user_agent='A myanimelist reply bot (by u/impshum)'
)


def get_anime(query):
    search = AnimeSearch(query)
    result = search.results[0]
    if result:
        return f'**Title**: {result.title}  \n**Synopsis**: {result.synopsis}  \n**Score**: {result.score}  \n**Type**: {result.type}  \n**Episodes**: {result.episodes}  \n**Url**: {result.url}'


def main():
    for comment in reddit.subreddit(reddit_target_subreddit).stream.comments(skip_existing=True):
        titles = re.findall('\{(.*?)\}', comment.body)
        if titles:
            reply_text = ''
            for title in titles:
                result = get_anime(title)
                if result:
                    reply_text += f'{result}\n\n'

            comment.reply(reply_text.strip().replace('\n\n', '\n\n---\n\n'))
            print(' - '.join(titles))


if __name__ == '__main__':
    main()
