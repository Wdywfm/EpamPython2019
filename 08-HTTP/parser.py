import grabber
import config
import time
import json
from bs4 import BeautifulSoup


def get_sub(link):
    link_list = link.split('/')
    return link_list[4]


def count_subs(sub_dict, sub):
    if sub in sub_dict:
        sub_dict[sub] += 1
    else:
        sub_dict[sub] = 1
    return sub_dict


grab = grabber.RedditGrabber(config.username, config.password)
html_doc = grab.getPage(url="https://www.reddit.com")
time.sleep(2)
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
data = soup.find('script', {'id': 'data'}).text
data = data.split('"')
dist = ''
posts_dict = {}
access_token = None
for i, val in enumerate(data):
    if val == 'dist':
        for c in data[i+1]:
            if c.isdigit():
                dist += c
    if val == 'accessToken':
        access_token = data[i+2]
        break
for i, val in enumerate(data):
    if val == 'models':
        if data[i+2][0:3] == 't3_':
            data = data[i:]
            break
for i, val in enumerate(data):
    if val == 'recent':
        data = data[:i]
        break
data = '"'.join(data)[8:]
data = data[:len(data)-1]
data = json.loads(data)
new_token = list(data.keys())[0]
for key in data:
    if '.com/r/' in data[key]['permalink']:
        posts_dict[key] = data[key]
data = grab.get_more_posts(new_token, int(dist), access_token)
time.sleep(2)
data = json.loads(data)
print(len(posts_dict))
while len(posts_dict) < 100:
    for post in data['posts']:
        if '.com/r/' in data['posts'][post]['permalink']:
            posts_dict[post] = data['posts'][post]
        if len(posts_dict) == 100:
            break
    data = grab.get_more_posts(data['token'], data['dist'], access_token)
    data = json.loads(data)
    time.sleep(2)
    print(len(posts_dict))
file = open('posts.txt', 'w')
sub_reddit_dict = {}
for key in posts_dict:
    print(key)
    print(posts_dict[key])
    sub_reddit = get_sub(posts_dict[key]['permalink'])
    sub_reddit_dict.update(count_subs(sub_reddit_dict, sub_reddit))
    file.write(f'Id: {key}\n')
    a = posts_dict[key]['author']
    file.write(f'Author: {a}\n')
    a = posts_dict[key]['title']
    file.write('Title: '+ascii(a)+'\n')
    a = posts_dict[key]['permalink']
    file.write(f'Link: {a}\n')
    if posts_dict[key]['media']:
        if 'content' in posts_dict[key]['media'].keys():
            a = posts_dict[key]['media']['content']
            file.write(f'Media: {a}\n')
        elif 'hlsUrl' in posts_dict[key]['media'].keys():
            a = posts_dict[key]['media']['hlsUrl']
            file.write(f'Media: {a}\n')
        else:
            full_text = ''
            for text in posts_dict[key]['media']['richtextContent']['document']:
                for t in text['c']:
                    if 'u' in t.keys():
                        full_text += (t['u'] + '\n')
                    if 't' in t.keys():
                        full_text += (t['t'] + '\n')
            file.write(f'Text: {full_text}\n')
    elif posts_dict[key]['source']:
        a = posts_dict[key]['source']['url']
        file.write(f'Media: {a}\n')
    a = posts_dict[key]['numComments']
    file.write(f'Number of comments: {a}\n')
    a = posts_dict[key]['score']
    file.write(f'Score: {a}\n')
    file.write(80*'-'+'\n')
file.close()
file = open('top5subs.txt', 'w')
i = 0
for sub in sorted(sub_reddit_dict, key=sub_reddit_dict.get, reverse=True):
    file.write(sub+'\n')
    i += 1
    if i == 5:
        break
file.close()
