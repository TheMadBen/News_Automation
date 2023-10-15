# Setup
Set up flask environment: In my case, I used VSCode - [Link to setup Flask in VSCode](https://code.visualstudio.com/docs/python/tutorial-flask)<br>
Must pip install flask and request (py -m pip install flask, py -m pip install request)<br>
Once that is done, make sure all the files (app.py, newsGrabber.py) and folders (static/styles, templates) are within the virtual environment (.venv). Don't mind the pycache, output.json, and news_automation_ss.png<br>
'py -m flask run' then follow the link on local host port 5000 to work the web application

# News Automation
This is a web applicaiton that implements HTML/CSS, Flask, Python, and Newsdata API<br>
It returns that latest news from user input search query and returns the title, description, link, and date on the webpage<br><br>
Note: The API searches news articles for specific keywords or phrases present in the news title, content, URL, meta keywords and meta description. In order for articles to be found, the keywords or phrase has to appear somewhere in the article.<br><br>
Note: Another thing to note is that not every news article publisher is accepted or used by the Newsdata API, so whichever this API accepts will be returned. Results may differ from Google News.<br><br>
Example: Joe Biden (might not return anything since many news articles refer to him as Biden or President Biden, so these two should be the search words)<br><br>
![alt text](https://github.com/TheMadBen/news_automation/blob/main/news_automation_ss.png)
