#!/usr/bin/env python3

# Import modules
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GLib', '2.0')
from gi.repository import Gtk, GLib
import os

# "_tr" arbitrary variable will be recognized by gettext application for extracting texts to be translated
import locale
from locale import gettext as _tr

from Performance import Performance


# Define class
class MainGUI:

    # ----------------------- Always called when object is generated -----------------------
    def __init__(self):

        # Configurations for language translation support
        locale.bindtextdomain("system-monitoring-center", "/usr/share/locale")
        locale.textdomain("system-monitoring-center")
        locale.setlocale(locale.LC_ALL, os.environ.get("LANG"))

        # Get GUI objects from file
        builder = Gtk.Builder()
        builder.add_from_file(os.path.dirname(os.path.realpath(__file__)) + "/../ui/MainWindow.ui")

        # Get GUI objects
        self.window1 = builder.get_object('window1')
        self.headerbar1 = builder.get_object('headerbar1')
        self.button1 = builder.get_object('button1')
        self.grid10 = builder.get_object('grid10')
        self.stack1 = builder.get_object('stack1')
        self.radiobutton1 = builder.get_object('radiobutton1')
        self.radiobutton2 = builder.get_object('radiobutton2')
        self.radiobutton3 = builder.get_object('radiobutton3')
        self.radiobutton5 = builder.get_object('radiobutton5')
        self.radiobutton6 = builder.get_object('radiobutton6')
        self.radiobutton8 = builder.get_object('radiobutton8')
        self.grid1 = builder.get_object('grid1')
        self.grid2 = builder.get_object('grid2')
        self.grid3 = builder.get_object('grid3')
        self.grid5 = builder.get_object('grid5')
        self.grid6 = builder.get_object('grid6')
        self.grid8 = builder.get_object('grid8')
        # Get Main GUI - Performance tab GUI objects
        self.stack1001 = builder.get_object('stack1001')
        self.radiobutton1001 = builder.get_object('radiobutton1001')
        self.radiobutton1002 = builder.get_object('radiobutton1002')
        self.radiobutton1003 = builder.get_object('radiobutton1003')
        self.radiobutton1004 = builder.get_object('radiobutton1004')
        self.radiobutton1005 = builder.get_object('radiobutton1005')
        self.radiobutton1006 = builder.get_object('radiobutton1006')
        self.grid1001 = builder.get_object('grid1001')
        self.grid1002 = builder.get_object('grid1002')
        self.grid1003 = builder.get_object('grid1003')
        self.grid1004 = builder.get_object('grid1004')
        self.grid1005 = builder.get_object('grid1005')
        self.grid1006 = builder.get_object('grid1006')
        self.grid1007 = builder.get_object('grid1007')
        self.grid1008 = builder.get_object('grid1008')

        # Connect GUI signals
        self.window1.connect("destroy", self.on_window1_destroy)
        self.window1.connect("delete_event", self.on_window1_delete)
        self.window1.connect("show", self.on_window1_show)
        self.button1.connect("clicked", self.on_button1_clicked)
        self.radiobutton1.connect("toggled", self.on_main_gui_tab_radiobuttons_toggled)
        self.radiobutton2.connect("toggled", self.on_main_gui_tab_radiobuttons_toggled)
        self.radiobutton3.connect("toggled", self.on_main_gui_tab_radiobuttons_toggled)
        self.radiobutton5.connect("toggled", self.on_main_gui_tab_radiobuttons_toggled)
        self.radiobutton6.connect("toggled", self.on_main_gui_tab_radiobuttons_toggled)
        self.radiobutton8.connect("toggled", self.on_main_gui_tab_radiobuttons_toggled)
        # Connect Main GUI - Performance tab GUI signals
        self.radiobutton1001.connect("toggled", self.on_main_gui_tab_radiobuttons_toggled)
        self.radiobutton1002.connect("toggled", self.on_main_gui_tab_radiobuttons_toggled)
        self.radiobutton1003.connect("toggled", self.on_main_gui_tab_radiobuttons_toggled)
        self.radiobutton1004.connect("toggled", self.on_main_gui_tab_radiobuttons_toggled)
        self.radiobutton1005.connect("toggled", self.on_main_gui_tab_radiobuttons_toggled)
        self.radiobutton1006.connect("toggled", self.on_main_gui_tab_radiobuttons_toggled)


    # ----------------------- Called for running code/functions when window is closed -----------------------
    def on_window1_destroy(self, widget):

        Gtk.main_quit()


    # ----------------------- Called for running code/functions when window is closed -----------------------
    # Window size is get by this event in order to get current window size. It gives pre-defined window size (it can be defined in the window .ui files) if ".get_size()" is used in "window destroy event" function.
    def on_window1_delete(self, widget, data=None):

        # Get window state (if full screen or not), window size (width, height) and save
        if Config.remember_window_size[0] == 1:
            main_window_state = widget.is_maximized()
            if main_window_state == True:
                main_window_state = 1
            if main_window_state == False:
                main_window_state = 0
            main_window_width, main_window_height = widget.get_size()
            remember_window_size_value = Config.remember_window_size[0]
            Config.remember_window_size = [remember_window_size_value, main_window_state, main_window_width, main_window_height]
            Config.config_save_func()


    # ----------------------- Called for running code/functions when GUI is shown -----------------------
    # Some functions (such as hardware selection, performance backround function, main menu gui importing, etc.) are run after main window is shown in order to reduce window display delay.
    def on_window1_show(self, widget):

        # Read and get config data
        global Config
        from Config import Config

        # Resize/set state (full screen or not) of the main window if "remember window size" option is enabled.
        remember_window_size = Config.remember_window_size
        if remember_window_size[0] == 1:
            if remember_window_size[1] == 1:
                widget.maximize()
            if remember_window_size[1] == 0:
                widget.resize(remember_window_size[2], remember_window_size[3])

        # Run "Performance" module in order to provide performance data to Performance tab, performance summary on the headerbar and Floating Summary window.
        global Performance
        from Performance import Performance

        # Add performance summary widgets to the main window headerbar.
        if Config.performance_summary_on_the_headerbar == 1:
            from PerformanceSummaryHeaderbar import PerformanceSummaryHeaderbar
            self.headerbar1.pack_start(PerformanceSummaryHeaderbar.grid101)

        # Show Floating Summary Window on application start.
        if Config.show_floating_summary == 1:
            from FloatingSummary import FloatingSummary
            FloatingSummary.window3001.show()

        # Define these settings (they are not saved to file) in order to avoid error on the first call of "main_gui_tab_loop_func" function.
        Config.current_main_tab = -1
        Config.performance_tab_current_sub_tab = -1

        # Start loop function to run loop functions of opened tabs to get data of them.
        self.main_gui_tab_loop_func()

        # Run default tab function after main window is shown.
        self.main_gui_default_tab_func()

        # Run main tab function after main window is shown (this function is also called when main tab checkbuttons are toggled).
        self.main_gui_tab_switch_func()

        # Show information for warning the user if the application has been run with root privileges (if UID=0). Information is shown just below the application window headerbar.
        if os.geteuid() == 0:
            # Generate a new label for the information. This label does not exist in the ".ui" UI file.
            label_root_warning = Gtk.Label(label=_tr("Warning! The application has been run with root privileges, you may harm your system."))
            css = b"label {background: rgba(100%,0%,0%,1.0);}"
            style_provider = Gtk.CssProvider()
            style_provider.load_from_data(css)
            label_root_warning.get_style_context().add_provider(style_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
            self.grid10.insert_row(0)
            # Attach the label to the grid at (0, 0) position.
            self.grid10.attach(label_root_warning, 0, 0, 1, 1)
            label_root_warning.set_visible(True)


    # ----------------------- "Main Menu" Button -----------------------
    def on_button1_clicked(self, widget):

        from MainMenusDialogs import MainMenusDialogs
        MainMenusDialogs.popover1001p.set_relative_to(widget)
        MainMenusDialogs.popover1001p.set_position(Gtk.PositionType.BOTTOM)
        MainMenusDialogs.popover1001p.popup()


    # ----------------------- "Performance, Processes, Users, Startup, Services, System, CPU, RAM, Disk, Network, GPU, Sensors" Radiobuttons -----------------------
    def on_main_gui_tab_radiobuttons_toggled(self, widget):

        if widget.get_active() == True:
            self.main_gui_tab_switch_func()


    # ----------------------------------- MainGUI - Default Tab Function (switches to default tab on initial run) -----------------------------------
    def main_gui_default_tab_func(self):

        default_main_tab = Config.default_main_tab
        if default_main_tab == 0:
             self.radiobutton1.set_active(True)
        elif default_main_tab == 1:
             self.radiobutton2.set_active(True)
        elif default_main_tab == 2:
             self.radiobutton3.set_active(True)
        elif default_main_tab == 3:
             self.radiobutton5.set_active(True)
        elif default_main_tab == 4:
             self.radiobutton6.set_active(True)
        elif default_main_tab == 5:
             self.radiobutton8.set_active(True)

        performance_tab_default_sub_tab = Config.performance_tab_default_sub_tab
        if performance_tab_default_sub_tab == 0:
             self.radiobutton1001.set_active(True)
        elif performance_tab_default_sub_tab == 1:
             self.radiobutton1002.set_active(True)
        elif performance_tab_default_sub_tab == 2:
             self.radiobutton1003.set_active(True)
        elif performance_tab_default_sub_tab == 3:
             self.radiobutton1004.set_active(True)
        elif performance_tab_default_sub_tab == 4:
             self.radiobutton1005.set_active(True)
        elif performance_tab_default_sub_tab == 5:
             self.radiobutton1006.set_active(True)


    # ----------------------------------- MainGUI - Main Function Run Function (runs main functions (Performance, Processes, etc.) when their stack page is selected) -----------------------------------
    def main_gui_tab_switch_func(self):

        # Local definition of this variable is made for lower CPU usage becuse this variable is used multiple times.
        remember_last_opened_tabs_on_application_start = Config.remember_last_opened_tabs_on_application_start

        # Switch to "Performance" tab
        if self.radiobutton1.get_active() == True:
            self.stack1.set_visible_child(self.grid1)
            if remember_last_opened_tabs_on_application_start == 1:
                # No need to save Config values after this value is defined. Because save operation is performed for Performance tab sub-tabs (CPU, RAM, Disk, Network, GPU, Sensors tabs).
                Config.default_main_tab = 0
            # This value is used in order to detect the current tab without checking GUI obejects for lower CPU usage. This value is not saved.
            Config.current_main_tab = 0

            # Switch to "CPU" tab
            if self.radiobutton1001.get_active() == True:
                self.stack1001.set_visible_child(self.grid1001)
                if remember_last_opened_tabs_on_application_start == 1:
                    Config.performance_tab_default_sub_tab = 0
                    Config.config_save_func()
                # This value is used in order to detect the current tab without checking GUI obejects for lower CPU usage. This value is not saved.
                Config.performance_tab_current_sub_tab = 0
                # Attach the grid to the grid (on the Main Window) at (0, 0) position if not attached.
                if self.grid1001.get_child_at(0,0) == None:
                    global Cpu
                    from Cpu import Cpu
                    self.grid1001.attach(Cpu.grid1101, 0, 0, 1, 1)
                # Run loop Cpu loop function in order to get data without waiting update interval.
                GLib.idle_add(Cpu.cpu_loop_func)
                return

            # Switch to "RAM" tab
            elif self.radiobutton1002.get_active() == True:
                self.stack1001.set_visible_child(self.grid1002)
                if remember_last_opened_tabs_on_application_start == 1:
                    Config.performance_tab_default_sub_tab = 1
                    Config.config_save_func()
                Config.performance_tab_current_sub_tab = 1
                if self.grid1002.get_child_at(0,0) == None:
                    global Ram
                    from Ram import Ram
                    self.grid1002.attach(Ram.grid1201, 0, 0, 1, 1)
                GLib.idle_add(Ram.ram_loop_func)
                return

            # Switch to "Disk" tab
            elif self.radiobutton1003.get_active() == True:
                self.stack1001.set_visible_child(self.grid1003)
                if remember_last_opened_tabs_on_application_start == 1:
                    Config.performance_tab_default_sub_tab = 2
                    Config.config_save_func()
                Config.performance_tab_current_sub_tab = 2
                if self.grid1003.get_child_at(0,0) == None:
                    global Disk
                    from Disk import Disk
                    self.grid1003.attach(Disk.grid1301, 0, 0, 1, 1)
                GLib.idle_add(Disk.disk_loop_func)
                return

            # Switch to "Network" tab
            elif self.radiobutton1004.get_active() == True:
                self.stack1001.set_visible_child(self.grid1004)
                if remember_last_opened_tabs_on_application_start == 1:
                    Config.performance_tab_default_sub_tab = 3
                    Config.config_save_func()
                Config.performance_tab_current_sub_tab = 3
                if self.grid1004.get_child_at(0,0) == None:
                    global Network
                    from Network import Network
                    self.grid1004.attach(Network.grid1401, 0, 0, 1, 1)
                GLib.idle_add(Network.network_loop_func)
                return

            # Switch to "GPU" tab
            elif self.radiobutton1005.get_active() == True:
                self.stack1001.set_visible_child(self.grid1005)
                if remember_last_opened_tabs_on_application_start == 1:
                    Config.performance_tab_default_sub_tab = 4
                    Config.config_save_func()
                Config.performance_tab_current_sub_tab = 4
                if self.grid1005.get_child_at(0,0) == None:
                    global Gpu
                    from Gpu import Gpu
                    self.grid1005.attach(Gpu.grid1501, 0, 0, 1, 1)
                GLib.idle_add(Gpu.gpu_loop_func)
                return

            # Switch to "Sensors" tab
            elif self.radiobutton1006.get_active() == True:
                self.stack1001.set_visible_child(self.grid1006)
                if remember_last_opened_tabs_on_application_start == 1:
                    Config.performance_tab_default_sub_tab = 5
                    Config.config_save_func()
                Config.performance_tab_current_sub_tab = 5
                if 'Sensors' not in globals():
                    global Sensors
                    import Sensors
                    Sensors.sensors_import_func()
                    Sensors.sensors_gui_func()
                    self.grid1006.attach(Sensors.grid1601, 0, 0, 1, 1)
                    Sensors.sensors_initial_func()
                Sensors.sensors_loop_func()
                return

        # Switch to "Processes" tab
        elif self.radiobutton2.get_active() == True:
            self.stack1.set_visible_child(self.grid2)
            if remember_last_opened_tabs_on_application_start == 1:
                Config.default_main_tab = 1
                Config.config_save_func()
            Config.current_main_tab = 1
            if 'Processes' not in globals():
                global Processes
                import Processes
                Processes.processes_import_func()
                Processes.processes_gui_func()
                self.grid2.attach(Processes.grid2101, 0, 0, 1, 1)
                Processes.processes_initial_func()
            Processes.processes_loop_func()
            return

        # Switch to "Users" tab
        elif self.radiobutton3.get_active() == True:
            self.stack1.set_visible_child(self.grid3)
            if remember_last_opened_tabs_on_application_start == 1:
                Config.default_main_tab = 2
                Config.config_save_func()
            Config.current_main_tab = 2
            if 'Users' not in globals():
                global Users
                import Users
                Users.users_import_func()
                Users.users_gui_func()
                self.grid3.attach(Users.grid3101, 0, 0, 1, 1)
                Users.users_initial_func()
            Users.users_loop_func()
            return

        # Switch to "Startup" tab
        elif self.radiobutton5.get_active() == True:
            self.stack1.set_visible_child(self.grid5)
            if remember_last_opened_tabs_on_application_start == 1:
                Config.default_main_tab = 3
                Config.config_save_func()
            Config.current_main_tab = 3
            if 'Startup' not in globals():
                global Startup
                import Startup
                Startup.startup_import_func()
                Startup.startup_gui_func()
                self.grid5.attach(Startup.grid5101, 0, 0, 1, 1)
                Startup.startup_initial_func()
            Startup.startup_loop_func()
            return

        # Switch to "Services" tab
        elif self.radiobutton6.get_active() == True:
            self.stack1.set_visible_child(self.grid6)
            if remember_last_opened_tabs_on_application_start == 1:
                Config.default_main_tab = 4
                Config.config_save_func()
            Config.current_main_tab = 4
            if 'Services' not in globals():
                global Services
                import Services
                Services.services_import_func()
                Services.services_gui_func()
                self.grid6.attach(Services.grid6101, 0, 0, 1, 1)
                Services.services_initial_func()
            return

        # Switch to "System" tab
        elif self.radiobutton8.get_active() == True:
            self.stack1.set_visible_child(self.grid8)
            if remember_last_opened_tabs_on_application_start == 1:
                Config.default_main_tab = 5
                Config.config_save_func()
            Config.current_main_tab = 5
            if self.grid8.get_child_at(0,0) == None:
                global System
                from System import System
                self.grid8.attach(System.grid8101, 0, 0, 1, 1)
            return


    # ----------------------- Called for running loop functions of opened tabs to get data -----------------------
    # "*args" is used in order to prevent "" warning and obtain a repeated function by using "GLib.timeout_source_new()". "GLib.timeout_source_new()" is used instead of "GLib.timeout_add()" to be able to change the update interval and run the loop again without waiting ending the previous update interval.
    def main_gui_tab_loop_func(self, *args):

        # Destroy GLib source for preventing it repeating the function.
        try:
            self.main_glib_source.destroy()
        # "try-except" is used in order to prevent errors if this is first run of the function.
        except AttributeError:
            pass
        self.main_glib_source = GLib.timeout_source_new(Config.update_interval * 1000)

        current_main_tab = Config.current_main_tab
        performance_tab_current_sub_tab = Config.performance_tab_current_sub_tab

        Performance.performance_background_loop_func()

        if Config.performance_summary_on_the_headerbar == 1:
            from PerformanceSummaryHeaderbar import PerformanceSummaryHeaderbar
            GLib.idle_add(PerformanceSummaryHeaderbar.performance_summary_headerbar_loop_func)

        if Config.show_floating_summary == 1:
            from FloatingSummary import FloatingSummary
            GLib.idle_add(FloatingSummary.floating_summary_loop_func)

        if current_main_tab == 0:
            if performance_tab_current_sub_tab == 0:
                GLib.idle_add(Cpu.cpu_loop_func)
            if performance_tab_current_sub_tab == 1:
                GLib.idle_add(Ram.ram_loop_func)
            if performance_tab_current_sub_tab == 2:
                GLib.idle_add(Disk.disk_loop_func)
            if performance_tab_current_sub_tab == 3:
                GLib.idle_add(Network.network_loop_func)
            if performance_tab_current_sub_tab == 4:
                GLib.idle_add(Gpu.gpu_loop_func)
            if performance_tab_current_sub_tab == 5:
                GLib.idle_add(Sensors.sensors_loop_func)
        if current_main_tab == 1:
            GLib.idle_add(Processes.processes_loop_func)
        if current_main_tab == 2:
            GLib.idle_add(Users.users_loop_func)
        if current_main_tab == 3:
            GLib.idle_add(Startup.startup_loop_func)
        # if current_main_tab == 4:
        #     pass
        # if current_main_tab == 5:
        #     pass

        # GLib.timeout_add(Config.update_interval * 1000, self.main_gui_tab_loop_func)

        self.main_glib_source.set_callback(self.main_gui_tab_loop_func)
        # Attach GLib.Source to MainContext. Therefore it will be part of the main loop until it is destroyed. A function may be attached to the MainContext multiple times.
        self.main_glib_source.attach(GLib.MainContext.default())


# Generate object
MainGUI = MainGUI()

