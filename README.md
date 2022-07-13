# Lap 4 Code Challenge

## Installation and Usage
To use deployed app:

Visit: https://ltl-url.herokuapp.com/

To use local version:
- clone and cd into repo folder
- `pipenv shell`
- `pipenv install`
- `pipenv run dev`
- Available on http://127.0.0.1:5000 

<hr>
<br>

## Design

<img width="515" alt="early designs" src="https://user-images.githubusercontent.com/91187363/178762834-4668aad6-b330-4e4f-9edf-d1bd24203abd.PNG">

<hr>
<br>

## Generating the strings:

###The Goal:

#### Make the url:
- easy to read
- easy to remember
- easy to say out loud and pass it on to others


#### How?

We used a combination of consonants + vowel + consonants + vowel 

we kept it all lower case as it's much easy for people to say, remember and type


### Option 1- Shorten and Add a random bit

- steps
  - take the first 3 characters after www. or // and then add them to the start of the end point
  - add a readable but completely random 4 letter word to the end, (c+v+c+v)

Eg.
https://www.bbc.com/news/live/world-asia-62144703

could be >

/bbc-tomi

/bbc-wila

/bbc-piko

### Option 2- Random 4 letter word

  - Generate a readable but completely random 4 letter word to the end, (c+v+c+v)

Eg.
https://www.bbc.com/news/live/world-asia-62144703

could be >

/lina

/zuta

/kema



### Option 3- Silly Sentence

  - Generate a readable string: number + adj + noun

Eg.

https://www.bbc.com/news/live/world-asia-62144703

could be >

/89sillypotatoes

/12agressiveholidays

/53thankfulstories



## Handling duplicates/ infinte possibilites:

- a string will try to be generated
- if it's a duplicate, already in the DB then it runs again
- it repeats this process 10x. 
- If it still can't find a unquie string after 10 attempts it will had a single int
- it will attempt this 3 times before adding another digit

EXAMPLE:

random gen url = you-bab 

x already exists, try again

random gen url = you-pol

x

random gen url = you-qat

x

(10 times for failing)

random gen url = you-qat2

x

random gen url = you-qat6

x

random gen url = you-qat1

x

still failing, add another digit:

random gen url = you-qat47

x

random gen url = you-qat76

x

random gen url = you-qat90

x

STILL FAILING?!

random gen url = you-qat651

x

random gen url = you-qat241

success!

my shortened url is  you-qat241


<hr>

# DATA:

### Silly_Sentence:

- 207 nouns stored in a tuple 
- 227 adjs stored in a tuple

### DB Structure:

with more time we'd move to postgres

```
[
  {"short_url":"you-gyc","url":"https://www.youtube.com/watch?v=pTFZFxd4hOI&t=582s&ab_channel=ProgrammingwithMosh"},
  {"short_url":"ltl-url","url":"https://ltl-url.herokuapp.com/"},
  {"short_url":"lahu","url":"https://ltl-url.herokuapp.com/"}
  
]
```

<hr>

## Endpoints:

/    = homepage

/url_list   = entire DB

/shorten    = displays the newly created url


## Test:

hmmmmm nada so far :/ 
