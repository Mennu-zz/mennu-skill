from mycroft import MycroftSkill, intent_file_handler


class Mennu(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('mennu.intent')
    def handle_mennu(self, message):
        self.speak_dialog('mennu')


def create_skill():
    return Mennu()

