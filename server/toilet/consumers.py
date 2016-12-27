from channels import Group


def ws_connect(message):
    Group("stream").add(message.reply_channel)
