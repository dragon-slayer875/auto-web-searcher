import webbrowser
import pyautogui
import threading

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

i=int(input("Enter start point: "))
f=int(input("Enter end point: "))
counter = i

def open_tab_timer():
    global counter
    if counter < f:
        threading.Timer(3.0, open_tab_timer).start()
        url = "https://www.bing.com/search?q="+str(counter)
        webbrowser.get('edge').open(url)
        counter+=1
    else:
        print("done")

open_tab_timer()

    
    

    
    