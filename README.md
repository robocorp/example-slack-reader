# example-slack-reader
Example robot that uses Slack's API to read message history from a channel

## Slack Setup

Easy way to read messages from slack is with Slack's APIs. https://api.slack.com/messaging/retrieving

To enable API access you need to configure Slack properly:

### Step 1

Create a Slack app https://github.com/slackapi/python-slack-sdk/blob/main/tutorial/01-creating-the-slack-app.md 
Remember to add permission scopes. Here you can see the required scopes for each API call https://api.slack.com/methods e.g. channels:read, groups:read, im:read and mpim:read

### Step 2

Install the app that you created to your Slack workspace

### Step 3

Copy "Bot User OAuth Token" from "OAuth & Permissions" -page to Robocorp Vault. This example uses secret name "slack" and key "token".

### Step 4

Invite the app to channels and retrieve messages
