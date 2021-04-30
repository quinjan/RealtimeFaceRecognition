from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys
import cv2
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread, QSize
import numpy as np


class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    

    def __init__(self):
        super().__init__()
        self._run_flag = True
        self.face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.captureFlag = False
    
    def face_extractor(self, img):
        # Function detects faces and returns the cropped face
        # If no face detected, it returns the input image
        #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = self.face_classifier.detectMultiScale(img, 1.3, 5)
        
        if faces is ():
            cropped_face = None
            return cropped_face, img
        
        # Crop all faces found
        for (x,y,w,h) in faces:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            x=x-10
            y=y-10
            cropped_face = img[y:y+h+50, x:x+w+50]
        return cropped_face, img

    def run(self):
        # capture from web cam
        cap = cv2.VideoCapture(0)
        count = 0
        while self._run_flag:
            ret, cv_img = cap.read()
            cropped_face, img = self.face_extractor(cv_img)
            print(count)
            print(self.captureFlag)
            if (cropped_face is not None) and (self.captureFlag == True) and (count<=120):
                count += 1
                face = cv2.resize(cropped_face, (400, 400))
                #face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                # Save file in specified directory with unique name
                if count<=100:
                    file_name_path = 'Dataset/Train/0/0_' + str(count) + '.jpg'
                else:
                    file_name_path = 'Dataset/Validate/0/0_' + str(count-100) + '.jpg'
                
                cv2.imwrite(file_name_path, face)

                if(count == 120):
                    self.captureFlag = False
                    count = 0

            if ret:
                self.change_pixmap_signal.emit(img)
        # shut down capture system
        cap.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt live label demo")
        self.disply_width = 640
        self.display_height = 480
        # create the label that holds the image
        self.image_label = QLabel(self)
        self.image_label.resize(self.disply_width, self.display_height)
        #create push button
        self.btn_capture = QPushButton()
        self.btn_capture.setObjectName(u"pushButton_capture")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_capture.sizePolicy().hasHeightForWidth())
        self.btn_capture.setSizePolicy(sizePolicy2)
        self.btn_capture.setMinimumSize(QSize(100, 50))
        self.btn_capture.setMaximumSize(QSize(16777215, 16777215))
        self.btn_capture.setText(u"Capture")
        # create a vertical box layout and add the two labels
        vbox = QVBoxLayout()
        vbox.addWidget(self.image_label)
        vbox.addWidget(self.btn_capture)
        # set the vbox layout as the widgets layout
        self.setLayout(vbox)

        # create the video capture thread
        self.thread = VideoThread()
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.btn_capture.clicked.connect(self.btn_capture_pressed)
        # start the thread
        self.thread.start()

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()



    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.image_label.setPixmap(qt_img)
    
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

    def btn_capture_pressed(self):
        self.thread.captureFlag = True
    
if __name__=="__main__":
    app = QApplication(sys.argv)
    a = App()
    a.show()
    sys.exit(app.exec_())