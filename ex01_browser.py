import webbrowser

webbrowser.open('https://google.com')

help(webbrowser)

chrome = webbrowser.get('google-chrome %s').open('https://google.com')
