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





