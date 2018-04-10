class Source:
  """
  News_source class that defines source Objects
  """
  def __init__(self, id, name,description, url, category):
    self.id = id
    self.name = name
    self.description = description
    self.url = url
    self.category = category


class Articles:
  """
  Article class that defines the article Object
  """
  def __init__(self, author, title, description,url, picture, publishedAt):
    self.author = author
    self.title = title
    self.description = description
    self.url = url
    self.picture = picture
    self.publishedAt = publishedAt
