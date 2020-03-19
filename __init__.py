from mycroft import MycroftSkill, intent_file_handler


class PumpController(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('controller.pump.intent')
    def handle_controller_pump(self, message):
        self.speak_dialog('controller.pump')


def create_skill():
    return PumpController()

