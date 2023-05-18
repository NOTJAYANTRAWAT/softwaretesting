import tkinter as Tkinter
import unittest
from datetime import datetime


class StopwatchTest(unittest.TestCase):
    def setUp(self):
        self.root = Tkinter.Tk()
        self.root.withdraw()  # Hide the GUI window during testing
        self.app = StopwatchApp(self.root)

    def test_start_button(self):
        # Simulate clicking the "Start" button
        self.app.start.invoke()
        self.assertTrue(self.app.running)

    def test_stop_button(self):
        # Simulate clicking the "Stop" button
        self.app.stop.invoke()
        self.assertFalse(self.app.running)

    def test_reset_button(self):
        # Simulate clicking the "Reset" button
        self.app.reset.invoke()
        self.assertEqual(self.app.counter, 0)
        self.assertEqual(self.app.label.cget("text"), "00:00:00")

    def tearDown(self):
        self.root.destroy()


class StopwatchApp:
    def __init__(self, root):
        self.counter = 0
        self.running = False
        self.root = root
        self.label = Tkinter.Label(self.root, text='Ready!', fg='black', font='Verdana 30 bold')
        self.label.pack()
        f = Tkinter.Frame(self.root)
        self.start = Tkinter.Button(f, text='Start', width=6, command=self.start_button_clicked)
        self.stop = Tkinter.Button(f, text='Stop', width=6, state='disabled', command=self.stop_button_clicked)
        self.reset = Tkinter.Button(f, text='Reset', width=6, state='disabled', command=self.reset_button_clicked)
        f.pack(anchor='center', pady=5)
        self.start.pack(side='left')
        self.stop.pack(side='left')
        self.reset.pack(side='left')

    def counter_label(self):
        if self.running:
            if self.counter == 0:
                display = 'Ready!'
            else:
                tt = datetime.utcfromtimestamp(self.counter)
                string = tt.strftime('%H:%M:%S')
                display = string
            self.label['text'] = display
            self.label.after(1000, self.counter_label)
            self.counter += 1

    def start_button_clicked(self):
        self.running = True
        self.counter_label()
        self.start['state'] = 'disabled'
        self.stop['state'] = 'normal'
        self.reset['state'] = 'normal'

    def stop_button_clicked(self):
        self.running = False
        self.start['state'] = 'normal'
        self.stop['state'] = 'disabled'
        self.reset['state'] = 'normal'

    def reset_button_clicked(self):
        self.counter = 0
        if not self.running:
            self.reset['state'] = 'disabled'
            self.label['text'] = '00:00:00'
        else:
            self.label['text'] = '00:00:00'


if __name__ == '__main__':
    unittest.main()
