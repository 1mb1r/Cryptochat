
from mainn import *

## ==> GLOBALS

GLOBAL_STATE = 0

class UIFunctions():




    ## ==> MAXIMIZE RESTORE FUNCTION
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        # IF NOT MAXIMIZED
        if status == 0:
            self.showMaximized()

            # SET GLOBAL TO 1
            GLOBAL_STATE = 1

            # IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
            self.ui.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
   #         self.ui.drop_shadow_frame.setStyleSheet("background-color: rgb(216, 240, 255); border-radius: 0px;")
            self.ui.pushButton_3.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
    #        self.ui.drop_shadow_frame.setStyleSheet("background-color: rgb(216, 240, 255); border-radius: 10px;")
            self.ui.pushButton_3.setToolTip("Maximize")

    ## ==> UI DEFINITIONS
    def uiDefinitions(self):

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # SET DROPSHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        # APPLY DROPSHADOW TO FRAME
        self.ui.drop_shadow_frame.setGraphicsEffect(self.shadow)

        # MAXIMIZE / RESTORE
        self.ui.pushButton_2.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # MINIMIZE
        self.ui.pushButton_3.clicked.connect(lambda: self.showMinimized())

        # CLOSE
        self.ui.pushButton.clicked.connect(lambda: self.close())

        ## ==> CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QtWidgets.QSizeGrip(self.ui.frame)
        self.sizegrip.setStyleSheet("QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        self.sizegrip.setToolTip("Resize Window")
        self.sizegrip_2 = QtWidgets.QSizeGrip(self.ui.frame_21)
        self.sizegrip_2.setStyleSheet("QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        self.sizegrip_2.setToolTip("Resize Window")



    ## RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTAURED
    def returnStatus():
        return GLOBAL_STATE