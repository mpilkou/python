#!/usr/bin/python3

import webbrowser, time
url = 'http://www.python.org/'
webbrowser.open(url)
time.sleep(5)
webbrowser.open_new(url)
time.sleep(5)
webbrowser.open_new_tab('http://www.python.org/')
