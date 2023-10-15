from flask import Flask, request, render_template, url_for
import newsGrabber

# setting up flask
# https://code.visualstudio.com/docs/python/tutorial-flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('newsPage.html')

@app.route('/get_query/', methods=['GET', 'POST'])
def get_query():
    if request.method == 'POST':
        query = request.form.get('query')
        url_Encoded = query.replace(" ", "%20") # api call requires url encoding
        json_response = newsGrabber.grab(url_Encoded)  # get response so that other functions can use
        title_list = newsGrabber.get_title(json_response)
        description_list = newsGrabber.get_description(json_response)
        url_list = newsGrabber.get_url(json_response)
        date_list = newsGrabber.get_date(json_response)
        
        zipped = zip(title_list, description_list, url_list, date_list)

    return render_template('newsPage.html', query=query, zipped=zipped)

if __name__=="__main__":
    app.run(debug=True)