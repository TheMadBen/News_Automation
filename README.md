# Setup
Must pip install flask and request  
Set up flask environment: In my case, I used VSCode - https://code.visualstudio.com/docs/python/tutorial-flask  
Once that is done, make sure all the files and folders are within the virtual environment (.venv) 
py -m flask run then follow the link on local host port 5000 to work the web application

# News Automation
This is a web applicaiton that implements HTML/CSS, Flask, Python, and Newsdata API  
It returns that latest news from user input search query and returns the title, description, link, and date on the webpage  
Note: The API searches news articles for specific keywords or phrases present in the news title, content, URL, meta keywords and meta description. In order for articles to be found, the keywords or phrase has to appear somewhere in the article.  
Note: Another thing to note is that not every news article publisher is accepted or used by the Newsdata API, so whichever this API accepts will be returned. Results may differ from Google News.  
Example: Joe Biden (might not return anything since many news articles refer to him as Biden or President Biden, so these two should be the search words)  
