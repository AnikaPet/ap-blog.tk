# ap-blog.tk

Simple blog application using Django. 
***
The homepage will redirect to about us page. Page /blog will list all blog posts, and there will be a dedicated detail page for each individual post.
Users can log in to the application or sign up. Once logged in, user can see all blog posts, but also Your profile page with their own blog posts. User can edit or delete their posts or add new one.
***
Installation
---
How to install an instance of this project:
1. Open terminal and make new directory for project 
```
mkdir project 
cd project
```
2. Clone git repository `git clone https://github.com/AnikaPet/ap-blog.tk.git`
3. Create and activate virtual enviroment
```
python3 -m venv .venv
source .venv/bin/activate
```
4. Install requirements
```
cd ap-blog.tk
pip install -r requirements.txt
```
5. Apply migrations `python3 manage.py migrate`
6. Run server `python3 manage.py runserver`
Your instance is running at http://127.0.0.1:8000/
---
Demo
***
![Alt text](/scr1.png?raw=true "Page that lists all blog posts.")
![Alt text](/scr2.png?raw=true "Your profile page.")
![Alt text](/scr3.png?raw=true "Add new blog post.")
