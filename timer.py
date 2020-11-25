import sys
from PyQt5 import QtCore

def timerEvent():
    global time
    time = time.addSecs(-1)
    print(time.toString("hh:mm:ss"))

app = QtCore.QCoreApplication(sys.argv)

timer = QtCore.QTimer()
time = QtCore.QTime(0,0,10)
timer.timeout.connect(timerEvent)
timer.start(1000)

sys.exit(app.exec_()) #파이참에서 실행시키면 카운트다운이 되긴하는데 이걸 UI랑 합치는 법을 모르겠음



