import requests
from bs4 import BeautifulSoup

class ideone():
  def __init__(self, project_id):
    self.project_id = project_id
    self.response = requests.get('https://ideone.com/' + project_id)
    self.soup = BeautifulSoup(self.response.text, 'html.parser')
  def id(self):
    return self.project_id
  def language(self):
    for language in self.soup.find('strong'):
      return language
  def code(self):
    for code in self.soup.find_all("input", {"class": "code-to-copy"}):
      return code.get('value')