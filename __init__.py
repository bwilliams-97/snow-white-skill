from mycroft import MycroftSkill, intent_file_handler


class SnowWhite(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('white.snow.intent')
    def handle_white_snow(self, message):
        self.speak_dialog('white.snow')


def create_skill():
    return SnowWhite()

