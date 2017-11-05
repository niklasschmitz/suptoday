from flask import Flask, request, redirect
import twilio.twiml
import requests
import ListingsParser

app = Flask(__name__)

@app.route("/" , methods=['POST'])
def incoming_message():
    
    from_number = request.values.get('From', None)
    message = request.values.get('Body')
    
    print(from_number + ':' + message) #print on the console for debugging
    
    ra_events_url = 'https://www.residentadvisor.net/events.aspx'
    r = requests.get(ra_events_url, stream=True)
    stringhtml = r.content
    
    reply = parse_listings_into_sms(stringhtml)
    
    resp = twilio.twiml.Response()
    resp.message(reply)
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

