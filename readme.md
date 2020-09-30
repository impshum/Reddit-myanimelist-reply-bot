## Reddit myanimelist reply bot

Streams comments and replies with myanimelist info if a title if found between curly brackets.


User comment

    I like {paranoia agent} and {lain}.


Bot reply

    Title: Mousou Dairinin
    Synopsis: The infamous Shounen Bat (Lil' Slugger) is terrorizing the residents of Musashino City. Flying around on his rollerblades and beating people down with a golden baseball bat, the assailant seems imposs...
    Score: 7.69
    Type: TV
    Episodes: 13
    Url: https://myanimelist.net/anime/323/Mousou_Dairinin

    ---

    Title: Serial Experiments Lain
    Synopsis: Lain Iwakura, an awkward and introverted fourteen-year-old, is one of the many girls from her school to receive a disturbing email from her classmate Chisa Yomoda—the very same Chisa who recently comm...
    Score: 8.02
    Type: TV
    Episodes: 13
    Url: https://myanimelist.net/anime/339/Serial_Experiments_Lain


### Instructions

-   Install requirements `pip install -r requirements.txt`
-   Create Reddit (script) app at <https://www.reddit.com/prefs/apps/> and get keys
-   Edit conf.ini with your details
-   Run it `python3 run.py`

### Settings Info

`reddit_user` - Reddit username  
`reddit_pass` - Reddit password  
`reddit_client_id` - Reddit Client ID  
`reddit_client_secret` - Reddit Client Secret  
`reddit_target_subreddit` - Subreddit to stream and reply to
