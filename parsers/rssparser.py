from main import *
from models.urls import *
from models.post import *


class RssParser(BaseHandler):
    def get_data(self, name, src):
        try:        
            _data = src.findAll(name)[0]  
        except(IndexError):
            _data = BeautifulSoup("No Data Received") 
        data = _data.get_text()
        return data    
            
    def _parse_rss(self, urltype):
        result = namedtuple('Result', ['title', 'description', 'link',
                                       'content', 'image', 'pubDate',
                                       'src', 'newstype'])
        results = []
        for url in urllist[urltype]:            
            try:                
                _page = urlfetch.fetch(url)  
            except urlfetch.DeadlineExceededError:
                 continue                
            page = _page.content                
            xml = BeautifulSoup(page)
            posts = xml.findAll("item")
            source = self.get_data("title", xml)            
            for post in posts:
                newstype = urltype                
                title = self.get_data("title", post)
                _desc = BeautifulSoup(self.get_data("description", post))
                desc = _desc.get_text()
                link = self.get_data("link", post)
                _image = _desc.find('img')
                _pubDate = self.get_data('pubDate', post)
                try:
                    pubDate = parser.parse(_pubDate) + timedelta(hours=1)           
                except (ValueError):
                    pubDate = datetime.utcnow()  
                if _image: image = _image['src']
                else: image = no_image_url
                content = "no content yet" #add parsing for content later"
                src = source      
                results.append(result(title, desc, link, content, image, pubDate, src, newstype))
        return results
        
    def parse_rss(self, urltype):
        results = self._parse_rss(urltype)
        update_flag = False
        for r in results:
            val1 = memcache.get(r.link)                  
            val2 = memcache.get(r.image)            
            if val1 == None and val2 == None:
                update_flag = True                
                logging.error("New Post Entity Being Created")                
                tokens = self.create_tokens(r)                
                p = Post(parent = post_key(), title = r.title,
                         description = r.description,
                         link = r.link, content = r.content,
                         image = r.image, pubDate = r.pubDate,
                         src = r.src, tokens_list = tokens, newstype = r.newstype)                
                p.put()
                memcache.set(r.link, True)
                memcache.set(r.image, True)
            else: logging.error("Duplicate post avoided")
        get_posts(update = update_flag)

    def tokenize_string(self, string, limit = 5):    
        tokens = string.split()
        tokens = list(token[:limit].lower() for token in tokens)        
        return tokens
            

    def create_tokens(self, post, token_limit = 20):
        string = post.title + post.description
        tokens = self.tokenize_string(string)[:token_limit]
        return tokens
