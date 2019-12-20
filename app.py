from flask import Flask
import requests

app=Flask(__name__)

@app.route('/')
def hello():
    return 'hello world!'

api_url='https://api.telegram.org'
token='875634635:AAHdmSUu5-gIpZZd9uXSnxps9WEdoB2KFaQ'
chat_id= '620153402'

@app.route('/send/<text>')
def send(text):
    res=requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    return 'ok!'

    

app.run(debug=True)