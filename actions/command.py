from netconnect.juniper import JuniperDriver
from st2common.runners.base_action import Action


class CommandAction(Action):
    def run(self, device, command):

        dev = JuniperDriver(device=device, username='vagrant', password='Vagrant',
                            disable_host_key_checking=True)
        dev.login()
        dev.enable_api()
        return dev.send_commands([command])
