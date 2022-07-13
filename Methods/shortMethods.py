# from itertools import count
import random
mock_db=['pod-cus','duv-has','you-dos']
# to run, call shorten_url(oringalurl)
import random
from site import addpackage #not sure
import Methods.words as words

rc = random.choice

def sillystring():
    return str(random.randint(2,99))+rc(words.adjs)+rc(words.nouns)


def shorten_url(url):
    c=0
    numofattempts=10
    while c<numofattempts:
        short_url = www_checker(url)
        # short_url = 'pod-cus' #Try add double
        print(mock_db)
        if short_url in mock_db:
            print('doubled', short_url, 'is the same as ',  mock_db)
            c +=1
        else:
            results_print(url, short_url)
            add_numbers(short_url)
            print(short_url)
            break
        # results_print(url, short_url)
    return short_url

def www_checker(url):
    if 'www.' in url:
        print('there is www.')
        url_startpos = url.find('www.')+4
        short_url = url[url_startpos:url_startpos+3:]+'-'+gen_rand_word()
    else:
        # short_url = gen_rand_word(0)
        url_startpos = url.find('//')+2
        short_url = url[url_startpos:url_startpos+3:]+'-'+gen_rand_word()
    return short_url

def gen_rand_word():
    rc=random.choice
    vowel=['a','e','i','o','u']
    cons=['q','w','r','t','y','p','s','d','f','g','h','j','k','l','z','c','v','b','n','m'] #x is missing
    random_word = rc(cons)+rc(vowel)+rc(cons)+rc(vowel)
    return random_word
   

def add_numbers(short_url):
    highest_num=9
    counter = 0
    while counter < 3:
        randomnum=random.randint(0,highest_num)
        short_url = short_url + str(randomnum)
        if short_url in mock_db:
            counter += 1
        else:
            return short_url
    highest_num = int(str(highest_num)+'9')

def results_print(url, short_url):
    print('Original url:', url)
    print('Shorten url: /'+ short_url)
    print('')
# test_urls=['https://www.amazon.es/s/?ie=UTF8&keywords=pas5&index=aps&tag=hydes-21&ref=pd_sl_4du4dlq3kf_b&adgrpid=114262704862&hvpone=&hvptwo=&hvadid=494081627943&hvpos=&hvnetw=g&hvrand=12173096921777144966&hvqmt=b&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1005411&hvtargid=kwd-298074010463&hydadcr=14615_1815589&gclid=CjwKCAjwt7SWBhAnEiwAx8ZLavT4YYtn0DMq9Dmt6MSmXT6b3lEUboZ0Vpga_4d1MMhEM9z4KBia_BoC7l4QAvD_BwE','https://github.com/xargon666/slay_the_spire_api_server','https://datascienceparichay.com/article/python-keep-only-letters-from-a-string/','www.youtube.com','https://app.rebrandly.com/public/links/share?href=rb.gy/aung43','https://www.amazon.es/','https://www.facebook.com/']
# # for testing many at once from the list above
# def run():
#     for i in test_urls:
#         shorten_url (i)
# if __name__ == '__main__':
#     shorten_url (var)
