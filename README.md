# TextMining
Text-Mining : interpretting twitter tweets on the topic : #padmavati and then clustering the data sets and do analysis using K-Means and K-Batch Means algo

### Running the scraping script for tweets
```sh
python3 magboard.py
```
This will create a tweets.txt file
Then run `python3 extract.py ` to remove the image urls from tweets.txt file and it will also print the positive/negative/neutral tweets after the sentiment analysis.

### Running DbScan with analysis using k-means and k-batch means
```sh 
python3 dbscan.py
```
### Result
![alt text](https://github.com/aryanshar/TextMining/blob/master/Figure_1.png?raw=true)
![alt text](https://github.com/aryanshar/TextMining/blob/master/kmeansVSMiniBatchKmeans.png?raw=true)
