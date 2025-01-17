import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.1')
from gi.repository import Gtk, WebKit2

class SimpleBrowser:
    def __init__(self):
        # Create a GTK Window
        self.window = Gtk.Window()
        self.window.set_default_size(800, 600)
        self.window.set_title("Simple Web Browser")

        # Create a WebKit WebView
        self.webview = WebKit2.WebView()

        # Create a Text Entry for URL
        self.url_entry = Gtk.Entry()
        self.url_entry.set_placeholder_text("Enter URL and press Enter")
        self.url_entry.connect("activate", self.load_url)

        # Create a vertical box to pack widgets
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        vbox.pack_start(self.url_entry, False, False, 0)
        vbox.pack_start(self.webview, True, True, 0)

        # Add the box to the window
        self.window.add(vbox)

        # Load a default web page
        self.webview.load_uri("https://www.example.com")

        # Show all components
        self.window.connect("destroy", Gtk.main_quit)
        self.window.show_all()

    def load_url(self, widget):
        url = self.url_entry.get_text()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        self.webview.load_uri(url)

# Run the browser
if __name__ == "__main__":
    app = SimpleBrowser()
    Gtk.main()
