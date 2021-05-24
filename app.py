from flask import Flask, render_template, request
from spacy_summarization import text_summarizer
import os
import spacy
from flask import session
from database import uloginact, ureg, storedata, aaddmeeting, getvoices, meetingnames, storecombinedchats, getcombinedchats
from datetime import datetime
nlp = spacy.load('en_core_web_sm')
app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/alogin')
def alogin():
    return render_template('login.html', utype="admin")


@app.route('/ulogin')
def ulogin():
    return render_template('login.html', utype="user")


@app.route('/registration')
def registration():
    return render_template('registration.html')


@app.route('/home')
def home():
    result = meetingnames()
    return render_template('userhome.html', data=result)


@app.route('/ahome')
def ahome():
    return render_template('adminhome.html')


@app.route('/addmeeting')
def addmeeting():
    return render_template('addmeeting.html')


@app.route('/voices')
def voices():
    data = meetingnames()
    return render_template('voicechats.html', data=data)


@app.route('/summarized')
def summarized():
    result = meetingnames()
    return render_template('summarized.html', data=result)


# Reading Time
def readingTime(mytext):
    total_words = len([token.text for token in nlp(mytext)])
    estimatedTime = total_words/200.0
    return estimatedTime


@app.route('/getsummarizeddata', methods=['POST', 'GET'])
def getsummarizeddata():
    if request.method == 'POST':
        result = getcombinedchats(request.form['meeting'])
        data = meetingnames()
        final_reading_time = readingTime(result[0][1])
        final_summary = text_summarizer(result[0][1])
        summary_reading_time = readingTime(final_summary)
        # print(final_reading_time, summary_reading_time, "final"+final_summary,)
    return render_template("summarized.html", result=result, data=data, sumtext=final_summary, final_reading_time=final_reading_time, summary_reading_time=summary_reading_time)


@app.route('/getvoicedata', methods=['POST', 'GET'])
def getvoicedata():
    if request.method == 'POST':
        result = getvoices(request.form['meeting'])
        data = meetingnames()
        return render_template("voicechats.html", result=result, data=data)


@app.route('/store', methods=['POST', 'GET'])
def store():
    if request.method == 'POST':
        speechData = request.form['speechData']
        meeting = request.form['meeting']
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        status = storedata(speechData, meeting, dt_string)
        if status == 1:
            return render_template("userhome.html")
        else:
            return render_template("userhome.html")
    else:
        return render_template("userhome.html")


@app.route('/regact', methods=['POST', 'GET'])
def regact():
    if request.method == 'POST':
        status = ureg(request.form['name'],
                      request.form['email'], request.form['password'], request.form['mob'])
        if status == 1:
            return render_template("login.html", utype="user")
        else:
            return render_template("registration.html")
    else:
        return render_template("registration.html")


@app.route('/logact', methods=['POST', 'GET'])
def logact():
    if request.method == 'POST':
        status = uloginact(
            request.form['utype'], request.form['email'], request.form['password'])
        print("status", status)
        if status:
            if request.form['utype'] == "user":
                session['name'] = status
                result = meetingnames()
                return render_template("userhome.html", data=result)
            else:
                return render_template("adminhome.html")
        else:
            return render_template("login.html")
    else:
        return render_template("login.html")


@app.route('/addmeetingact', methods=['POST', 'GET'])
def addmeetingact():
    if request.method == 'POST':
        status = aaddmeeting(request.form['meeting'])
        if status == 1:
            return render_template("addmeeting.html")
        else:
            return render_template("addmeeting.html")
    else:
        return render_template("addmeeting.html")


@app.route('/combine/<string:mname>')
def combine(mname):
    data = getvoices(mname)
    chats = ""
    for a, b, c, d in data:
        chats = chats+" "+b+"."
    status=storecombinedchats(chats, mname)
    result = meetingnames()
    final_summary = text_summarizer(chats)
    if status==1:
        return render_template('voicechats.html', chats=final_summary, data=result)
    else:
        data = meetingnames()
        return render_template("voicechats.html", data=data)


if __name__ == '__main__':
    app.run(debug=True)
