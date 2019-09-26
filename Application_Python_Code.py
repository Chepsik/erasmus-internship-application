#   This Application is generated from .ui file.
#
#   The individual elements are responsible for:
#   label_16,_14,_13,_7,_9,_10 - Showing images,
#   label_19 - Informations about frame,
#   label_30 - Informations about wrong/good Input Data
#   line_edit(0),_3,_8 - INPUT for N_mols, frames, points
#   pushButton_4 - Generate frames
#   pushButton(0),_2 - Next/Previous frame


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import scipy as scipy
import matplotlib.pyplot as plt
import pylab
from itertools import chain
import random
from scipy.spatial.distance import pdist, squareform
from scipy.special import erf
from PIL import Image
import os
import glob
import copy
import shutil

random.seed(1209)

N_mols = 100                            # number of molecules
frames = 20                             # number of generated frames
points = 30                             # number of visible points

pix_size = 110                          # pixel size
pixels=32                               # number of pixels
stdev = np.true_divide(25,pix_size)     # super_res microscope localiz precision
min_d = np.true_divide(5,pix_size)      # molecular diameter in pixels

ren_fact=5                              # image rendering factor


class Ui_ImageWindow(object):           # Main Application Class
    # INTERFACE START
    def setupUi(self, ImageWindow):
        ImageWindow.setObjectName("ImageWindow")
        ImageWindow.resize(1286, 736)
        self.gridLayout_9 = QtWidgets.QGridLayout(ImageWindow)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(ImageWindow)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(ImageWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(200, 200))
        self.label_7.setMaximumSize(QtCore.QSize(400, 400))
        self.label_7.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 2, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(ImageWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(200, 200))
        self.label_9.setMaximumSize(QtCore.QSize(400, 400))
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(ImageWindow)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 3, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem6, 1, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 1, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem8, 2, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(ImageWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(200, 200))
        self.label_10.setMaximumSize(QtCore.QSize(400, 400))
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(ImageWindow)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 0, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem9, 3, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem10, 1, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem11, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 0, 2, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.pushButton_2 = QtWidgets.QPushButton(ImageWindow)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem13)
        self.horizontalSlider = QtWidgets.QSlider(ImageWindow)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(300, 0))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_2.addWidget(self.horizontalSlider)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem14)
        self.pushButton = QtWidgets.QPushButton(ImageWindow)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem15)
        self.gridLayout_9.addLayout(self.horizontalLayout_2, 4, 1, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem16, 3, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem17, 4, 2, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem18, 5, 1, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem19, 4, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(ImageWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QtCore.QSize(200, 200))
        self.label_13.setMaximumSize(QtCore.QSize(400, 400))
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.gridLayout_6.addWidget(self.label_13, 4, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(ImageWindow)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_6.addWidget(self.label_12, 2, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem20, 2, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(ImageWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QtCore.QSize(200, 200))
        self.label_14.setMaximumSize(QtCore.QSize(400, 400))
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.gridLayout_7.addWidget(self.label_14, 2, 1, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem21, 3, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(ImageWindow)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_7.addWidget(self.label_15, 0, 1, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem22, 1, 1, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem23, 2, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_7, 0, 1, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_17 = QtWidgets.QLabel(ImageWindow)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_8.addWidget(self.label_17, 0, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(ImageWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMinimumSize(QtCore.QSize(200, 200))
        self.label_16.setMaximumSize(QtCore.QSize(400, 500))
        self.label_16.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.gridLayout_8.addWidget(self.label_16, 2, 1, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem24, 2, 0, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem25, 1, 1, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem26, 3, 1, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem27, 2, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_8, 0, 2, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_5, 3, 1, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_18 = QtWidgets.QLabel(ImageWindow)
        self.label_18.setObjectName("label_18")
        self.gridLayout_12.addWidget(self.label_18, 0, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(ImageWindow)
        self.label_19.setObjectName("label_19")
        self.gridLayout_12.addWidget(self.label_19, 0, 1, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_12, 4, 0, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        spacerItem28 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem28, 3, 0, 1, 1)
        spacerItem29 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem29, 1, 0, 1, 1)
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_20 = QtWidgets.QLabel(ImageWindow)
        self.label_20.setObjectName("label_20")
        self.gridLayout_13.addWidget(self.label_20, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(ImageWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QtCore.QSize(100, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_13.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(ImageWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(100, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_13.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(ImageWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setMaximumSize(QtCore.QSize(100, 30))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_13.addWidget(self.lineEdit_8, 3, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(ImageWindow)
        self.label_23.setObjectName("label_23")
        self.gridLayout_13.addWidget(self.label_23, 3, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(ImageWindow)
        self.label_22.setObjectName("label_22")
        self.gridLayout_13.addWidget(self.label_22, 2, 0, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.gridLayout_10.addLayout(self.gridLayout_13, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(ImageWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_10.addWidget(self.label, 0, 0, 1, 1)
        spacerItem30 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem30, 5, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(ImageWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_10.addWidget(self.pushButton_4, 4, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        spacerItem31 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem31, 1, 0, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gridLayout_9.addLayout(self.gridLayout_11, 3, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(ImageWindow)
        self.label_30.setObjectName("label_30")
        self.gridLayout_11.addWidget(self.label_30, 2, 0, 1, 1)
        QtCore.QMetaObject.connectSlotsByName(ImageWindow)
        
        # ON PUSH BUTTON/SLIDER EVENTS
        self.pushButton_4.clicked.connect(self.CreateImages)            # OnPlayButton event
        self.horizontalSlider.valueChanged.connect(self.LoadImages)     # OnChangeValueOfSlider event
        self.pushButton.clicked.connect(self.NextFrame)                 # OnNextButton event
        self.pushButton_2.clicked.connect(self.PreviousFrame)           # OnPreviousButton event

        self.retranslateUi(ImageWindow)
        print('Generate Window - DONE')

    #CHANGING DEFAULT TEXT IN LABELS - START
    def retranslateUi(self, ImageWindow):
        _translate = QtCore.QCoreApplication.translate
        ImageWindow.setWindowTitle(_translate("ImageWindow", "Form"))
        self.label_6.setText(_translate("ImageWindow", "Super Resolution Image"))
        self.label_8.setText(_translate("ImageWindow", "Super Resolution Sum Image"))
        self.label_11.setText(_translate("ImageWindow", "Conventional Image"))
        self.pushButton_2.setText(_translate("ImageWindow", "Previous"))
        self.pushButton.setText(_translate("ImageWindow", "Next"))
        self.label_12.setText(_translate("ImageWindow", "Plot Image"))
        self.label_15.setText(_translate("ImageWindow", "Points"))
        self.label_17.setText(_translate("ImageWindow", "Final Plot Image"))
        self.label_18.setText(_translate("ImageWindow", "Frame: "))
        self.label_19.setText(_translate("ImageWindow", "--"))
        self.label_30.setText(_translate("ImageWindow", "CONSOLE: "))
        self.label_20.setText(_translate("ImageWindow", "Number of molecules"))
        self.lineEdit.setInputMask(_translate("ImageWindow", "9999"))
        self.lineEdit_3.setInputMask(_translate("ImageWindow", "9999"))
        self.lineEdit_8.setInputMask(_translate("ImageWindow", "9999"))
        self.label_23.setText(_translate("ImageWindow", "Points/Frame"))
        self.label_22.setText(_translate("ImageWindow", "Frames"))
        self.label.setText(_translate("ImageWindow", "Options"))
        self.pushButton_4.setText(_translate("ImageWindow", "Play"))
        self.lineEdit_3.setText(_translate("ImageWindow", "20"))
        self.lineEdit_8.setText(_translate("ImageWindow", "30"))
        self.lineEdit.setText(_translate("ImageWindow", "100"))
        print('RetranslateUI - DONE')
        self.CreateFolders()
    #CHANGING DEFAULT TEXT IN LABELS - END

    #INTERFACE END


    ## INTERFACE FUNCTIONS CALLED BY USERS - START
    def CreateImages(self):                                                 # After Clicking Play Button Function
        print('Function')
        Mol_N = int(self.lineEdit.text())                                   # Read Input Mol_N
        print('N_mols: ',Mol_N)
        Frame_N = int(self.lineEdit_3.text())                               # Read Input Frame_N
        print('Frames: ',Frame_N)
        Points_N = int(self.lineEdit_8.text())                              # Read Input Points_N
        print('Points: ',Points_N)

        if Mol_N >= Points_N and Frame_N >= 10 and Points_N != 0:           # Conditions to enter the function
            [xn,yn] = self.generate_molecules(pixels,Mol_N,min_d)           # Calling generate molecules function
            print('Points - DONE.')
            self.frame_simulation(pixels,xn,yn,stdev, Frame_N, Points_N)    # Calling generate frames function - passing points generated above
            print('Images - DONE.')
            self.Refresh()                                                  # Refresh images function
            self.horizontalSlider.setMaximum(Frame_N-1)
            self.label_30.setText("CONSOLE: OK")
        elif Mol_N < Points_N:                                              # Wrong parameters
            self.label_30.setText("CONSOLE: N_mols to low")
        elif Frame_N < 10:
            self.label_30.setText("CONSOLE: Frames to low (min = 10)")      # Wrong parameters
        elif Points_N == 0:
            self.label_30.setText("CONSOLE: Points to low (min = 1)")       # Wrong parameters

    def NextFrame(self):                                                    # Next frame function
        frame = self.horizontalSlider.value()                               # Takes value from the slider
        frame = frame + 1                                                   # Increment the value from slider
        self.horizontalSlider.setValue(frame)                               # Assigns the value to slider
        
    def PreviousFrame(self):                                                # Previous frame function
        frame = self.horizontalSlider.value()                               # Takes value from the slider
        frame = frame - 1                                                   # Decrement the value from slider
        self.horizontalSlider.setValue(frame)                               # Assigns the value to slider
                
    def LoadImages(self):
        frame = self.horizontalSlider.value()                               # Takes value from the slider
        frame = frame+1                                                     # Increment value from slider (Slider counts from 0 but we wants 1 frame)
        
        filename = 'image' + str(frame)                                     # Create variable that contain name of the image file
        script_dir = os.path.dirname(__file__)                              #
        results_dir = os.path.join(script_dir, 'Plot/')                     # Create paths to different folders with images 
        results_dir2 = os.path.join(script_dir, 'Image/')                   #
        results_dir3 = os.path.join(script_dir, 'SumImage/')                #

        self.label_19.setText(str(frame))                                   # Set number of appearing frame in the output widget

        pixmap = QtGui.QPixmap('Plot\zFinalImage.png')                      # Read the image from the folder
        pixmap =pixmap.scaled(self.label_16.width(), self.label_16.height())# Scale the size of the image to the size of the label
        self.label_16.setPixmap(pixmap)                                     # Set new image in the label
        self.label_16.repaint()                                             # Refresh the image in the label (in case of reading two different images with the same name)
        self.label_16.parentWidget().repaint()                              # Does the same but for the parent of the label widget
                                                                            # Rest of the functions work the same as above
        pixmap = QtGui.QPixmap('Plot\pointsImage.png')
        pixmap = pixmap.scaled(self.label_14.width(), self.label_14.height())
        self.label_14.setPixmap(pixmap)
        self.label_14.repaint()
        self.label_14.parentWidget().repaint()

        pixmap = QtGui.QPixmap(results_dir + filename)
        pixmap = pixmap.scaled(self.label_13.width(), self.label_13.height())
        self.label_13.setPixmap(pixmap)
        self.label_13.repaint()
        self.label_13.parentWidget().repaint()

        pixmap = QtGui.QPixmap(results_dir2 + filename)
        pixmap = pixmap.scaled(self.label_7.width(), self.label_7.height())
        self.label_7.setPixmap(pixmap)
        self.label_7.repaint()
        self.label_7.parentWidget().repaint()

        pixmap = QtGui.QPixmap(results_dir3 + filename)
        pixmap = pixmap.scaled(self.label_9.width(), self.label_9.height())
        self.label_9.setPixmap(pixmap)
        self.label_9.repaint()
        self.label_9.parentWidget().repaint()

        pixmap = QtGui.QPixmap('SumImage/convimg.TIFF')
        pixmap = pixmap.scaled(self.label_10.width(), self.label_10.height())
        self.label_10.setPixmap(pixmap)
        self.label_10.repaint()
        self.label_10.parentWidget().repaint()

    ## INTERFACE FUNCTIONS CALLED BY USERS - END


        
    ## UNDER INTERFACE FUNCTIONS CALLED BY INTERFACE FUNCTIONS - START

    def frame_simulation(self,pixels,xn,yn,stdev, howmanyframes, howmanypoints):

        # Create path for generating images
        script_dir = os.path.dirname(__file__)
        results_dir = os.path.join(script_dir, 'Plot/')
        results_dir2 = os.path.join(script_dir, 'Image/')
        results_dir3 = os.path.join(script_dir, 'SumImage/')

        # Delete files in the folders (delete all files even not images)
        files = glob.glob('Plot/*')
        for f in files:
            os.remove(f)
        files = glob.glob('Image/*')
        for f in files:
            os.remove(f)
        files = glob.glob('SumImage/*')
        for f in files:
            os.remove(f)
        print('Dir_Files - DONE')
        
        points = 0                                                                  # Bool whether the Points image was rendered or not
        n=xn.shape[-1]
        x=[]
        y=[]
        
        localization=np.random.geometric(p=0.2, size=n)                             # Generate random localizations of points
        
        for i in range(0,n):
            Xij = np.random.normal(loc=0,scale=stdev, size=int(localization[i]))    # Assign X
            Yij = np.random.normal(loc=0,scale=stdev, size=int(localization[i]))    # Assign Y
            x.append(xn[i] + Xij)                                                   # Append on x and y lists
            y.append(yn[i] + Yij)
        
        x_unchain= np.asarray(list(chain.from_iterable(x)))
        y_unchain= np.asarray(list(chain.from_iterable(y)))
        
        plot_memory_xn = 0                                                          # These functions stores points and coordinates
        plot_memory_yn = 0                                                          # where they appeared (used in generating FinalImage)
        plot_memory = []
        
        SUM_IM =  0                                                                 # SUM_IMAGE Variable
       
        for image in range(0,howmanyframes):                                        # This loop will be executed N_Frames times
            
            [newxn,newyn] = self.random_movement(xn,yn,n)                           # Generate random movement in exact frame
            xy = random.sample(range(newxn.shape[0]), howmanypoints)                # Take randomly N_Points from generated random movement points
            
            # Save points to memory
            plot_memory = np.append(plot_memory,xy)            
            plot_memory_xn = np.append(plot_memory_xn, newxn)          
            plot_memory_yn = np.append(plot_memory_yn, newyn)
            
            if points == 0:
                # Generate POINTS_IMAGE
                fig = plt.figure(1, figsize=(5.5,5.5))
                plt.xlim((0,pixels))
                plt.ylim((0,pixels))
                plt.scatter(xn,yn,c='b',marker='+')
                plt.axis('off')
                plt.gca().invert_yaxis()
                plt.savefig(results_dir + 'pointsImage', bbox_inches='tight')
                points = 1
                plt.close()

            # Generate PLOT_IMAGE  
            fig = plt.figure(1, figsize=(5.5,5.5))
            plt.scatter(newxn[xy],newyn[xy],c='r',marker='.')            
            plt.xlim((0,pixels))
            plt.ylim((0,pixels))
            plt.axis('off')
            plt.gca().invert_yaxis()
            filename = 'image' + str(image+1)
            plt.savefig(results_dir + filename, bbox_inches='tight')
            plt.close()

            # Generate IMAGE
            IM = self.map_into_image(newxn[xy],newyn[xy],pixels,ren_fact, stdev)
            im = Image.fromarray(IM)
            im.save(results_dir2 + filename + ".TIFF")
            
            # Generate SUMIMAGE 
            SUM_IM = np.float64(IM) + np.float64(SUM_IM)
            SUM_IM = SUM_IM / SUM_IM.max()
            SUM_IM = np.uint16(SUM_IM*(2**16-1))
      
            im = Image.fromarray(SUM_IM)
            im.save(results_dir3 + filename + ".TIFF")
            print('Created Images: ',image+1)            
        # Generate FINALIMAGE
        fig = plt.figure(1, figsize=(5.5,5.5))    
        plt.scatter(plot_memory_xn,plot_memory_yn,c='r',marker='.')
        plt.scatter(xn,yn,c='b',marker='+')        
        plt.axis('equal')
        plt.xlim((0,pixels))
        plt.ylim((0,pixels))
        plt.gca().invert_yaxis()
        plt.axis('off')    
        filename = 'zFinalImage'
        plt.savefig(results_dir + filename, bbox_inches='tight')
        plt.close()
        # Generate CONVIMG
        filename = 'convimg'
        WT = self.map_into_image(xn,yn,pixels,1, 240/pix_size)
        wt = Image.fromarray(WT)
        wt.save(results_dir3 + filename + ".TIFF")
        
        self.horizontalSlider.setValue(0)                                           # Set slider value to 0
        return [x_unchain,y_unchain]


    def CreateFolders(self):
        
        if os.path.exists("./Image"):                                               # check if path exist, if yes
            shutil.rmtree("./Image")                                                # remove content
        if os.path.exists("./Plot"):                                                # repeat it for every path
            shutil.rmtree("./Plot")
        if os.path.exists("./SumImage"):
            shutil.rmtree("./SumImage")
            
        os.mkdir("./Image")                                                         # Creat folders
        os.mkdir("./Plot")
        os.mkdir("./SumImage")


    def Refresh(self):                                                              
        app.processEvents()                                                         # Check Events in the application
        for image in range(0,20):                                                   # Loop start
            self.horizontalSlider.setValue(image)                                   # Change the value of slider
        self.horizontalSlider.setValue(0)                                           # Value of slider = 0
        self.LoadImages()                                                           # Call Load_Images functions

    ## UNDER INTERFACE FUNCTIONS CALLED BY INTERFACE FUNCTIONS - END  



    ## CALCULATION FUNCTIONS - START ##

    def random_movement(self,xn,yn,n):
        newxn = copy.copy(xn)                                                           # Generate exact copy of mother points
        newyn = copy.copy(yn)                                                           # We do this to avoid modification of mother points   
        for point in range(0,n):                                                        # For number of molecules:
            newxn[point] = newxn[point] + np.random.normal(loc=0,scale=stdev, size=1)   # Generate random x coordinate
            newyn[point] = newyn[point] + np.random.normal(loc=0,scale=stdev, size=1)   # Generate random y coordinate
            
        return [newxn,newyn]                                                            # Return new coordinates

    
    def generate_molecules(self,pixels,n,min_d):                                        # Generate Molecules function - called in CreateImages     
        xn=np.random.uniform(0,(pixels-1),n)                                            # Draw samples from a uniform distribution
        yn=np.random.uniform(0,(pixels-1),n)      
        z=np.stack((xn,yn), axis=-1)
        D = squareform(pdist(z)) + 1000*min_d*np.identity(n)
    
        while D.min()<min_d:
            ind1, ind2 = np.where(D < min_d)
            unique = (ind1 < ind2)
            ind1 = ind1[unique]

            xn[ind1]=xn[ind1]+np.random.normal(0,min_d,ind1.shape[-1])
            yn[ind1]=yn[ind1]+np.random.normal(0,min_d,ind1.shape[-1])
            z=np.stack((xn,yn), axis=-1)
            D = squareform(pdist(z)) + 1000*min_d*np.identity(n)
            
        return [xn,yn]


    def MolKernel(self,x_inx,y_inx,x_pos,y_pos,stdev):
        
        [xx,yy] = np.meshgrid(x_inx,y_inx)
        img_kernel = (0.5*(erf(np.true_divide((xx-x_pos+0.5),(np.sqrt(2)*stdev)))-erf(np.true_divide((xx-x_pos-0.5),(np.sqrt(2)*stdev)))))*(0.5*(erf(np.true_divide((yy-y_pos+0.5),(np.sqrt(2)*stdev)))-erf(np.true_divide((yy-y_pos-0.5),(np.sqrt(2)*stdev)))))
        img_kernel=img_kernel/img_kernel.sum()
        return img_kernel



    def map_into_image(self,x,y,pixels, fact, st):
        
        M=np.zeros((pixels*fact,pixels*fact))    
        xx=np.linspace(0,fact*pixels-1,fact*pixels)
        yy=np.linspace(0,fact*pixels-1,fact*pixels)   
        for i in range(0,x.shape[-1]):
            img=self.MolKernel(xx,yy,fact*x[i],fact*y[i],fact*st)
            M=M+img
        M=M/M.max()
        return np.asarray(np.uint16(M*(2**16-1)))


    ## CALCULATION FUNCTIONS - END ##
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ImageWindow = QtWidgets.QWidget()
    ui = Ui_ImageWindow()
    ui.setupUi(ImageWindow)
    ImageWindow.show()
    print('Window Called - DONE')
    ret = app.exec_()

    # Delete Created Dictionaries
    shutil.rmtree("./Image")                # Remove content of these folders
    shutil.rmtree("./Plot")
    shutil.rmtree("./SumImage")
    
    sys.exit(ret)
