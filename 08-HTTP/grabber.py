import requests


class RedditGrabber:
    HOME = "https://www.reddit.com/login"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                      " AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/73.0.3683.103 Safari/537.36 OPR/60.0.3255.170"
                      " (Edition Yx 03)",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.reddit.com/login/",
        "Content-Type": "application/x-www-form-urlencoded",
        "Connection": "keep-alive"
    }

    def __init__(self, username, password):
        self.session = requests.Session()
        self.session.headers = self.HEADERS
        self.auth(username, password)

    def getPage(self, url):
        self.session.headers = self.HEADERS
        return self.session.get(url).text

    def auth(self, username, password):
        get = self.session.get(self.HOME)
        print(get.text)
        abc = input("x: ")
        data = {
            'csrf_token': abc,
            'otp': '',
            'password': password,
            'dest': 'https//www.reddit.com',
            'username': username
        }
        print(self.session.post(url='https://www.reddit.com/login',
                                data=data).text)

    def get_more_posts(self, post_id=None, dist=None, access_token=None):
        if not post_id:
            post_id = input('x: ')
        if not dist:
            dist = input('dist: ')
        url = f'https://gateway.reddit.com/desktopapi/v1/frontpage?rtj=only' \
            f'&redditWebClient=web2x&app=web2x-client-production' \
            f'&after={post_id}&dist={dist}&sort=best&layout=card' \
            f'&useMockData=false&allow_over18=&include='
        if not access_token:
            access_token = input('access_token: ')
        self.session.headers['Referer'] = "https://www.reddit.com/"
        self.session.headers['Authorization'] = 'Bearer ' + access_token
        self.session.headers['reddit-user_id'] = 'desktop2x'
        return self.session.get(url=url).text

