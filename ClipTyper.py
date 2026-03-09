import wx
import pyperclip
import pyautogui as pg
import threading


class ClipTyper:
    @staticmethod
    def get_clipboard_text():
        try:
            return pyperclip.paste() or ""
        except Exception as e:
            wx.MessageBox(f"Error accessing clipboard: {e}", "Error", wx.ICON_ERROR | wx.OK)
            return ""

    @staticmethod
    def send_text(text):
        pg.write(text, interval=0.001)


class ClipTyperWindow(wx.Frame):
    def __init__(self):
        super().__init__(
            None,
            title="ClipTyper",
            size=(400, 180),
            style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX) | wx.STAY_ON_TOP
        )
        self.SetBackgroundColour(wx.WHITE)
        self.countdown = 0
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self._on_timer)
        self._create_ui()
        self.Show()

    def _create_ui(self):
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, faceName="Lucida Console")
        
        self.paste_button = wx.Button(panel, label="Paste by typing.", size=(-1, 60))
        self.paste_button.SetFont(font)
        self.paste_button.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.paste_button.Bind(wx.EVT_BUTTON, self.on_paste_button_clicked)
        sizer.Add(self.paste_button, 1, wx.ALL | wx.EXPAND, 20)

        panel.SetSizer(sizer)

    def on_paste_button_clicked(self, event):
        self.clipboard_text = ClipTyper.get_clipboard_text()
        if not self.clipboard_text or len(self.clipboard_text) > 100_000:
            msg = "Clipboard is empty." if not self.clipboard_text else "Text exceeds 100,000 characters."
            wx.MessageBox(msg, "Error", wx.ICON_ERROR | wx.OK)
            return

        self.paste_button.Disable()
        self.countdown = 3
        self._update_button_label()
        self.timer.Start(1000)

    def _on_timer(self, event):
        self.countdown -= 1
        if self.countdown > 0:
            self._update_button_label()
        else:
            self.timer.Stop()
            self.paste_button.SetLabel("Pasting...")
            threading.Thread(target=self._paste_text, daemon=True).start()

    def _update_button_label(self):
        self.paste_button.SetLabel(f"Pasting in {self.countdown}s...")

    def _paste_text(self):
        ClipTyper.send_text(self.clipboard_text)
        wx.CallAfter(self._reset_ui)

    def _reset_ui(self):
        self.paste_button.SetLabel("Paste by typing.")
        self.paste_button.Enable()


def main():
    app = wx.App(False)
    frame = ClipTyperWindow()
    app.MainLoop()


if __name__ == "__main__":
    main()
