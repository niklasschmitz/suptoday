from flask import Flask, request, redirect
import twilio.twiml
import requests
import contentRipper

app = Flask(__name__)

@app.route("/" , methods=['POST'])
def incoming_message():
    
    from_number = request.values.get('From', None)
    message = request.values.get('Body')
    
    print(from_number + ':' + message) #print on the console for debugging
    
    
    
    resp = twilio.twiml.Response()
    reply = stringToSMS(stringhtml)
    resp.message(reply)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
