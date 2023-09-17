from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QFileDialog, QApplication
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,QPushButton,QWidget,QHBoxLayout,QMainWindow,QLabel
from PyQt5.QtCore import QTimer, QThread, pyqtSignal,QDateTime,QTime
class videoPlayer:
    def __init__(self):
        self.ui = uic.loadUi('video_1.ui')  # 加载designer设计的ui程序
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.ui.widget)
        #self.timer = QTimer(self)
        self.ui.bin_select.clicked.connect(self.openVideoFile)
        self.ui.bin_select.clicked.connect(self.distance())
    # 打开视频文件并播放
    def openVideoFile(self):
        self.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))
        self.player.play()
    def distance(self):
        self.ui.lineEdit.setText('stop')
if __name__ == "__main__":
    app = QApplication([])
    myPlayer = videoPlayer()
    myPlayer.ui.show()
    app.exec()
