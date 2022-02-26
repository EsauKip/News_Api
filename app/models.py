class Article:
    """class that instanciates news articles from the news api
    """
def __init__(self,author,description,time,url,image,title):
    self.author = author
    self.description = description
    self.time = time
    self.url = url
    self.image = image
    self.title = title 
class source:
    """class that instanciates the source object
    """
def __init__(self,name,description,id,url):   
    self.name = name
    self.description = description
    self.id = id
    self.url = url
class Headlines:
    """class that instanciates the headlines of the categories and sources object
    """   
def __init__(self,author,description,time,url,image,title):
    self.author = author
    self.description = description
    self.time = time
    self.url = url
    self.image = image
    self.title = title    
class Category:
    """class that instanciates object news  categories object from the sources class
    """
def __init__(self,author,description,time,url,image,title):
    self.author = author
    self.description = description
    self.time = time
    self.url = url
    self.image = image
    self.title = title
