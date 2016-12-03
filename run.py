from flask import Flask, request, redirect
import twilio.twiml
app = Flask(__name__)

@app.route("/" , methods=['POST'])
def incoming_message():

    from_number = request.values.get('From', None)
    message = request.values.get('Body')
    print(from_number + ':' + message)
    resp = twilio.twiml.Response()
    resp.message(message)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
