from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/', methods=['POST'])
def whatsbot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    message = resp.message()
    responded = False

    greetings = " Welcome to Ficksburg Food Court, where we deliver anywhere and anytime between 9am-4pm Monday-Saturday for R25. Choose your actions\n1.Order\n2.Ask for assistance\n3.Delivery status\n4.Exit\n5.Payments"
    order =  "Where would you like to order food Wimpy, Imperani, KFC ,Wild BBQ"
    assistant = "We will connect you to customer service"
    delivery = "We wil call in 5 minutes to let you know "
    payments = "We accept cash only"
    leave =  "Bye see you soon"

    if incoming_msg not in ["1","order","2","ask for assistance","3","delivery status","4","exit","5","payments","wimpy","imperani","kfc","wild bbq"]:
        message.body(greetings)
        responded = True

    if incoming_msg == "1" or "order" in incoming_msg:
        message.body(order)
        responded = True

    if incoming_msg == "wimpy" in incoming_msg:
        message.media("https://food-menu-6924.twil.io/Breakfast_Griills_.pdf")
        responded = True

    if incoming_msg == "kfc" in incoming_msg:
        message.media("https://food-menu-6924.twil.io/KFC.pdf")
        responded = True

    if incoming_msg == "imperani" in incoming_msg:
        message.media("https://food-menu-6924.twil.io/Imperani%20menu.pdf")
        responded = True

    if incoming_msg == "wild bbq" in incoming_msg:
        message.media("https://food-menu-6924.twil.io/BBq.jpg")
        responded = True

    if incoming_msg == "2" or "ask for assistance" in incoming_msg:
        message.body(assistant)
        responded = True

    if incoming_msg == "3" or "delivery status" in incoming_msg:
        message.body(delivery)
        responded = True

    if incoming_msg == "4" or "exit" in incoming_msg:
        message.body(leave)
        responded = True
        
    if incoming_msg == "5" or "payments" in incoming_msg:
        message.body(payments)
        responded = True

    if not responded:
        message.body("Sorry I do not understand, type hi to go back to the main menu")
    return str(resp)


if __name__ == '__main__':
    app.run()























