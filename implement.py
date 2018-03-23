from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

with open("tweet_with_url.txt", 'r') as data:
  text = [line.strip() for line in data]
 
 
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(text)
true_k = 3
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)
print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
file = open('words_per_cluster.txt', 'a') 
for i in range(true_k):
    print ("Cluster %d:" % i,)
    file.write("Cluster %d:" % i +'\n')
    file.write('\n'+ '\n')
    for ind in order_centroids[i, :10]:
        print (' %s' % terms[ind],)
        file.write(terms[ind]+'\n')
    file.write('\n')