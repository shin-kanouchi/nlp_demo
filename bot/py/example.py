#!/usr/bin/python
# coding:utf-8

from api import API
import w2v_dialog
import MeCab

with API() as api:
    # ツイートする
    # api.tweet('tweet test2')

    # リプを取得
    for mention in api.get_mentions():
        text = mention['text']
        tweet_id = mention['id_str']
        screen_name = mention['user']['screen_name']
        # ユーザ情報(プロフィール)
        name = mention['user']['name']
        zone = mention['user']['time_zone']
        location = mention['user']['location']
        description = mention['user']['description']
        #print mention
        #print text, tweet_id, screen_name, name, zone, location, description

        tagger = MeCab.Tagger('-Owakati')
        #result = tagger.parse(' '.join(text.split()[1:]).decode('utf-8'))
        result = tagger.parse(' '.join(text.split()[1:]).encode('utf-8'))
        
        #words = result.strip().split(' ')
        print result
        SV = w2v_dialog.sentence_vectorizer('../model/matrix50.model')
        w2v_list = SV.use_database('../model/NTCIR.wakati.u20', result)
        # リプを返す
        print ''.join(w2v_list[0].split())
        print ''.join(w2v_list[1].split())
        print ''.join(w2v_list[2].split())
        content = ''.join(w2v_list[0].split())

        api.reply(content, tweet_id, screen_name)
