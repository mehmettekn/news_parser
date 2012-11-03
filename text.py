from collections import namedtuple

def fetch_posts(newstype, limit):
    posts = Post.all().filter('newstype =', newstype).fetch(limit = limit)
    return posts
    
def create_token_dict(post1, post2):
    post1_vectors = dict()
    post2_vectors = dict()
    for token in post1.tokens_list:
        if token not in post1_vectors:
            post1_vectors[token] = 1
        else:
            post1_vectors[token] += 1
        if token in post2.tokens_list:
            if token not in post2_vectors:
                post2_vectors[token] = 1
            else:
                post2_vectors[token] += 1
        else:
            post2_vectors[token] = 0
    return post1_vectors, post2_vectors

def scalar(vector_dict): 
    total = 0 
    for count in vector_dict.values(): 
        total += count * count 
    return sqrt(total) 

def cosine_similarity(A, B):  
    total = 0 
    for token in A:
        if token in B: 
            total += A[token] * B[token] 
    return float(total) / (scalar(A) * scalar(B))

def make_distance_matrix(clusters):
    ret = dict()
    for i in range(len(clusters)):
        for j in range(len(clusters)):
            if j == i:
                break
            else:            
                ret[(i,j)] = clusters[i].getSingleDistance(clusters[j])
            
    return ret
    


def agglo(posts):
    clusters = []
    min_distance = 0
    while True:
        distances = make_distance_matrix(clusters)
        min_key = distances.keys()[0]
        min_distance = distances[min_key]
        for key in distances.keys():
            if distances[key] < min_distance:
                min_key = key
                min_distance = distances[key]
        if min_distance > cutoff or len(clusters) == 1:
            break
        else:
            c1, c2 = clusters[min_key[0]], clusters[min_key[1]]
            clusters.remove(c1)
            clusters.remove(c2)
            clusters.append(c1.fuse(c2))
    return clusters

def get_distance(a, b):
    return 1 / cosine_similarity(a, b)

    

class Clusters:
    def get_single_distance(self, cluster):
        ret = get_distance(self.points[0], cluster.points[0])
        for p in self.points:
            for q in cluster.points:
                distance = get_distance(p, q)
                if distance < ret:
                    ret = distance
        return ret
    
    
