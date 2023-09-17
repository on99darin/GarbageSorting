class imageThread(QThread):
    showImage = pyqtSignal(object) # 这里可以不要，这里是定义信号的
    def __init__(self, image): # 在调用这个类的时候传入image这个参数
        super().__init__()
        self.image = image

    def run(self): # 在使用这个类的时候直接调用这个接口就行
        # self.showImage.emit(image_color)
        image = self.image
        (imageH, imageW) = image.shape[0:2]
        Qimag = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # pyqt中正常显示图片需要将opencv中的bgr转化为rgb
        QiM = QImage(Qimag.data, imageW, imageH,
                     imageW * 3, QImage.Format_RGB888) # 这也是将图像显示在界面中的必备步骤，QImage是从PyQt5.QtGui中导入的
        ui.hotImage.setPixmap(QPixmap.fromImage(QiM)) # ui.hotImage是pyqt中的lable控件，这个名字是你在画界面的时候自己定义的
