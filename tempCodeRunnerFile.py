from bs4 import BeautifulSoup

with open('home.html','r') as f:
   content = f.read()
   

soup = BeautifulSoup(content,'lxml')
courses_html_tags = soup.find_all('h5')
print(courses_html_tags)
for course in courses_html_tags:
   print(course.text)
  
