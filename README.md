# Twitter-Analysis
A python repository for analysing Twitter Tweets. My motivation for this repository are the following online tutorials/blogs.
  * http://adilmoujahid.com/posts/2014/07/twitter-analytics/
  * http://pythoncentral.io/introduction-to-tweepy-twitter-for-python/
  * http://pythoncentral.io/introduction-to-tweepy-twitter-for-python/

Following tasks are being implemented on Twitter Tweets.
### Predicting the most favourite football player in English Premier League. 
I aim to predict the most favourite football player according to collected tweets. Initially, I will be making a simple model for getting some results. I will be cleaning the data and then extract some good features. I will be then applying NER model in tweets to extract players' names.
## Getting Started
### Prerequisites
Python requirements:
  * Tweepy
  * Matplotlib
  * Pandas
  * Nltk

### Running on your system
If you wish, you can try downloading the latest tweets using following command.
  ```
  python twitter_stream.py > ./data/twitter_API_data.txt
  
  ```
Make sure that you put up proper user credentials in the code in order to use Twitter API. If you want, you can even work directly on my data. 
To get results, run *python twitter_analysis.py* on your terminal. 
  
## License
### MIT License
Copyright (c) 2016 Divesh Pandey

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
