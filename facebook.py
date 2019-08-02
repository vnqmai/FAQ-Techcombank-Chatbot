from rasa_core.channels.facebook import FacebookInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import os
from rasa_core.utils import EndpointConfig

# load your trained agent
interpreter = RasaNLUInterpreter("models/faq-techcombank/nlu/")
MODEL_PATH = "models/faq-techcombank/core/"
action_endpoint = EndpointConfig(url="https://faq-techcombank-actions.herokuapp.com/webhook")

agent = Agent.load(MODEL_PATH, interpreter=interpreter)

input_channel = FacebookInput(
     fb_verify="rasa-chatbot",
     # you need tell facebook this token, to confirm your URL
     fb_secret="4676432e11fea67fbc56461fc54480b6",  # your app secret
     fb_access_token="EAAFDao4G8zwBAIDWtu5tIiVIrdFhDozCjFiviH9pWVAMLHrCqnfMEbMB69qo2ZB76qdRWFAfSaU7DZAVtfiSE7KXskmmkJVV2LTZBlacOAoal2BVIRUvRH1B9d6zyfZA5WkBSi5B2a1ZAX064LiQxZAc1EAUdbC4ZAFL1myzRxJg3DPgkS6E0y318sfeXjBgaMZD"
     # token for the page you subscribed to
)
# set serve_forever=False if you want to keep the server running
s = agent.handle_channels([input_channel], int(os.environ.get('PORT', 5004)), serve_forever=True)