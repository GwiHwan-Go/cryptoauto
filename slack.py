#send slack
#references : https://www.youtube.com/watch?v=s24dxIp-Cp0     2:40-->4:40
#!pip install requests

import requests
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "bot user oauth token"
message = "send what you want"

post_message(myToken,"#crypto-auto-trading",message)
