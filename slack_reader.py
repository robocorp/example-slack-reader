from slack_sdk import WebClient
from time import sleep

MESSAGES_PER_PAGE = 200

class slack_reader:
    def list_channels(self, token):
        response = WebClient(token=token).conversations_list()
        return {channel["name"]: channel for channel in response["channels"]}

    def retrieve_messages(self, token, channel_id, limit=1000):
        client = WebClient(token=token)

        # get first page
        page = 1
        response = client.conversations_history(
            channel=channel_id,
            limit=MESSAGES_PER_PAGE
        )
        messages_all = response['messages']

        while len(messages_all) <= limit and response['has_more']:
            page += 1
            sleep(1)   # need to wait 1 sec before next call due to rate limits
            response = client.conversations_history(
                channel=channel_id,
                limit=MESSAGES_PER_PAGE,
                cursor=response['response_metadata']['next_cursor']
            )
            messages = response['messages']
            messages_all = messages_all + messages

        return messages_all[0:limit]
