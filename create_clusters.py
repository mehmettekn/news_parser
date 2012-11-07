# Following is an implementation of AGGLOMERATIVE ALGORITHM for cluster-
# ing. I was inspired by the post:
# http://www.daniweb.com/software-development/python/code/216641/statistical-learning-with-python-clustering

import sys
import math
import random

from collections import namedtuple
from datetime import datetime,timedelta

from google.appengine.ext import db

from models.post import *

class Point:
    def __init__(self, coords, post_key, reference=None):
        self.coords = coords
        self.post_key = post_key        
        self.n = len(coords)
        self.reference = reference
    
    def __repr__(self):
        return str(self.coords)

class Cluster:
    def __init__(self, points):
        if len(points) == 0:
            raise Exception("ILLEGAL: EMPTY CLUSTER")
        self.points = points
        self.n = points[0].n
         
    def __repr__(self):
        return str(self.points)

    def update(self, points):
        old_centroid = self.centroid
        self.points = points
        self.centroid = self.calculate_centroid()
        return get_distance(old_centroid, self.centroid)

    def calculate_centroid(self):
        centroid_coords = []
        for i in range(self.n):
            centroid_coords.append(0.0)
            for p in self.points:
                centroid_coords[i] = centroid_coords[i]+p.coords[i]
            centroid_coords[i] = centroid_coords[i]/len(self.points)
        return Point(centroid_coords)

    def get_single_distance(self, cluster):
        ret = get_distance(self.points[0], cluster.points[0])
        for p in self.points:
            for q in cluster.points:
                distance = get_distance(p, q)
                if distance < ret: ret = distance
        return ret

    def get_complete_distance(self, cluster):
        ret = get_distance(self.points[0], cluster.points[0])
        for p in self.points:
            for q in cluster.points:
                distance = get_distance(p, q)
                if distance > ret: ret = distance
        return ret

    def get_centroid_distance(self, cluster):
        return get_distance(self.centroid, cluster.centroid)

    def fuse(self, cluster):
        points = self.points
        points.extend(cluster.points)
        return Cluster(points)

def make_distance_matrix(clusters, linkage):
    ret = dict()
    for i in range(len(clusters)):
        for j in range(len(clusters)):            
            if j == i:            
                break
            if linkage == 's':
                ret[(i,j)] = clusters[i].get_single_distance(clusters[j])
            elif linkage == 'c':
                ret[(i,j)] = clusters[i].get_complete_distance(clusters[j])
            elif linkage == 't':
                ret[(i,j)] = clusters[i].get_centroid_distance(clusters[j])
            else:
                raise Exception("INVALID LINKAGE")
    return ret

def agglo(points, linkage, cutoff):
    if not linkage in [ 's', 'c', 't' ]:
        raise Exception("INVALID LINKAGE")
    if not points:
        raise Exception("No Points Acquired")    
    clusters = []
    for p in points:
        clusters.append(Cluster([p]))
    min_distance = 0
    while (True):     
        distances = make_distance_matrix(clusters, linkage)       
        if len(clusters) == 1:
            break        
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

def make_post_points(post):
    coords, post_key = create_token_dict(post)
    return Point(coords, post_key)
        
def plot(clusters):
    root = Tk()
    cp = ClusterPlot(root)
    root.mainLoop()   

def fetch_posts(newstype, limit):
    posts = Post.all().filter('newstype =', newstype).fetch(limit = limit)
    return posts

def scalar(vector_dict): 
    total = 0 
    for count in vector_dict.values(): 
        total += count * count 
    return math.sqrt(total) 

def cosine_similarity(A, B):  
    total = 0 
    for token in A:
        if token in B: 
            total += A[token] * B[token] 
    return float(total) / (scalar(A) * scalar(B))

def get_distance(a, b):
    similarity = cosine_similarity(a.coords, b.coords)
    if similarity == 0:
        return 100000 # a big random number.   
    return 1 / similarity

def fetch_posts(newstype, hours=6, limit):
    posts = (Post.all().filter('newstype =', newstype)
             .filter('pubDate >', datetime.now() - timedelta(hours = hours))
             .fetch(limit = limit))    
    print len(posts)    
    return posts

def create_token_dict(post):
    post_dict = dict()
    for token in post.tokens_list:
        if token not in post_dict:
            post_dict[token] = 1
        else:
            post_dict[token] += 1
    return post_dict, post.key()

def main(): 
    newstype = 'economy_urls'    
    linkage, agglo_cutoff = 's', 4.0
    posts = fetch_posts(newstype, 100)
    points = []
    for post in posts:
        p = make_post_points(post)
        points.append(p)    
    clusters = agglo(points, linkage, agglo_cutoff)
    for cluster in clusters:
        News_Cluster(parent = cluster_key(), newstype = newstype) 
















