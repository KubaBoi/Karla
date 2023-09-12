import signal
import sys

def signal_handler(signal, frame):
    print('You pressed Ctrl+C - or killed me with -2')
    with open("C:\\Users\\Jakub Anderle\\IdeaProjects\\Karla\\smazat.txt", "x", encoding="utf-8") as f:
        f.write("uauaua")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.)

while True:
    pass