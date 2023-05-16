from ovos_plugin_manager.templates.gui import GUIExtension
from ovos_utils.log import LOG


class MobileExtension(GUIExtension):
    """ Mobile Platform Extension: This extension is responsible for managing the mobile GUI behaviours.
       This extension adds support for Homescreens and Homescreen Management and global page back navigation.

   Args:
       bus: MessageBus instance
       gui: GUI instance
       preload_gui (bool): load GUI skills even if gui client not connected
       permanent (bool): disable unloading of GUI skills on gui client disconnections
   """

    def __init__(self, config, bus=None, gui=None,
                 preload_gui=True, permanent=True):
        LOG.info("Mobile: Initializing")
        super().__init__(bus, gui, config, preload_gui, permanent)

    def register_bus_events(self):
        self.bus.on('mycroft.gui.screen.close', self.handle_show_homescreen)
        self.bus.on('mycroft.gui.forceHome', self.handle_show_homescreen)
        self.bus.on('mycroft.gui.screen.request.page.back', self.handle_page_back)
        self.gui.register_handler("mycroft.device.show.idle", self.handle_show_homescreen)
        self.gui.register_handler('mycroft.gui.screen.close', self.handle_show_homescreen)

    def handle_show_homescreen(self, message):
        self.homescreen_manager.show_homescreen()

    def handle_page_back(self, message):
        self.gui.handle_namespace_global_back({})
