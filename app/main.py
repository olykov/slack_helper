import os
import time
import schedule
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from modules import Utils

client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])
me = os.environ['SLACK_USER_ID']

def set_a_status(status, dnd=False, dnd_duration=0, away=False):
    try:
        client.users_profile_set(user=me, profile=status)
        print(f"Status was updated to {status}")
        if dnd:
            client.dnd_setSnooze(user=me, num_minutes=dnd_duration)
        else:
            client.dnd_endDnd(user=me)

        if away:
            client.users_setPresence(presence="away")
        else:
            client.users_setPresence(presence="auto")
    except SlackApiError as e:
        assert e.response["ok"] is False
        assert e.response["error"]
        print(f"Got an error: {e.response['error']}")
        assert isinstance(e.response.status_code, int)
        print(f"Received a response status_code: {e.response.status_code}")

# Lunch - UTC time
schedule.every().day.at("12:31").do(set_a_status, Utils.status_lunch, False)
schedule.every().day.at("13:29").do(set_a_status, Utils.status_empty, False)

# Private time - UTC time
schedule.every().day.at("18:31").do(set_a_status, Utils.status_sleep, True, 810, True)
schedule.every().day.at("07:29").do(set_a_status, Utils.status_empty, False)

while True:
    schedule.run_pending()
    time.sleep(10)
