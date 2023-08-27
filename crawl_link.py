import re
from bs4 import BeautifulSoup

def get_hrefs(html_string):
  hrefs = []
  soup = BeautifulSoup(html_string, 'html.parser')
  a_tags = soup.findAll('a', class_='tbody-5 p-t-4 YLycza2 u9KHmsf')
  for item in a_tags:
    hrefs.append("https://www.fiverr.com/" + item['href'])
  # for match in re.finditer(r'<a\s+href=".*?"\s+target="_blank"\s+class="tbody-5 p-t-4 YLycza2 u9KHmsf"\s+title=""\s+rel="">(.*?)</a>', html_string):
  #   hrefs.append(match.group(1))
  return hrefs

with open('./fiverr_html.txt', 'r') as f:
    data = f.read()

hrefs = get_hrefs(data)
# for i in hrefs:
#   print(i)
#   break
print(len(hrefs))
print(hrefs)