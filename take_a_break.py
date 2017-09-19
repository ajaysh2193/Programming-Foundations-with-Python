import time
import webbrowser

print("The work is started at "+time.ctime())
total_breaks=3
break_count=0

while(break_count<total_breaks):
    time.sleep(7200)
    webbrowser.open("https://www.youtube.com/watch?v=Dj5ot7zq1wk")
    break_count = break_count + 1
