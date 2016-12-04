from flask import Flask, request, redirect
import twilio.twiml
import requests
import Event
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
    
    lp=ListingsParser.ListingsParser()
    lp.find_and_save_top_three_events(stringhtml)
    
    resp = twilio.twiml.Response()
    reply = c.getSMS()
    resp.message(reply)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

