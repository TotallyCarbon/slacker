from slacker import Slacker

slack = Slacker('xoxb-12636740661-ErLaLmki3qXoaKIZEFODnTNC')

# Send a message to #general channel
slack.chat.post_message('#general', 'test')
