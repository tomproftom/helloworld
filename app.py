import requests
from flask import Flask, render_template, request


app = Flask(__name__)
app.config['SERVER_NAME'] = "192.168.1.194"


@app.route('/', methods=['GET', 'POST'])
def index():

    requestlist = []
    if request.method == 'POST':
        string1 = request.form.get('city')
        string2 = request.form.get('state')
        string3 = request.form.get('ip')
        string4 = request.form.get('tested')

        requestlist.append(string1)
        requestlist.append(string2)
        requestlist.append(string3)
        requestlist.append(string4)
                  
        print (requestlist[0])
        print('$$$')
        print (requestlist[1])
        print (requestlist[2])
        print (requestlist[3])
        print(requestlist)

       
    return render_template('layout.html')

##to run :::: flask run execute the following###
    ###export FLASK_APP=app.py###

if __name__ == "__main__":
    app.run()