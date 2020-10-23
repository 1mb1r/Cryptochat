import sys
from untitled_7 import Ui_MainWindow
import json
import subprocess
import datetime
import requests
from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import PKCS1_v1_5
from Cryptodome.Hash import SHA256
import Cryptodome.Random
import binascii
from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
import wallet
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ui_functions import *
import node
from node import *


cost = 0.01

class OneWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Вешаем на кнопку функцию PoemCheck
        self.ui.pushButton_5.clicked.connect(self.lock_chat)
        self.ui.pushButton_6.clicked.connect(self.check_user)
        text = str(self.ui.label_7.text())
        balance = 0
        self.ui.label_15.setText(str(balance))
        pub_key = "00000"
        self.ui.label_5.setText(pub_key)
        # self.ui.pushButton_4.clicked.connect(self.send_message(str(text)))    (lambda ch, text=text :
        # self.change_chat(text))
        self.ui.pushButton_4.clicked.connect(lambda ch, text=text: self.send_message(text))
        self.ui.textEdit.installEventFilter(self)
        self.ui.lineEdit.returnPressed.connect(self.check_user)
        self.ui.кнопка_добавл.clicked.connect(lambda: self.Add_New_user())

        #       self.pushButton_30.clicked.connect(self.change_chat)

        ########################################################################
        #     self.ui.pushButton_5.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        # PAGE 1
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_4))

        # PAGE 2
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_7))

        # PAGE 3
        #    self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_6))
        # добавить друга
        self.ui.btn_page_4.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_8))

        for i in range(3):
            self.widget_0 = QtWidgets.QWidget(self.ui.scrollAreaWidgetContents)
            self.widget_0.setMinimumSize(QtCore.QSize(400, 100))
            self.widget_0.setMaximumSize(QtCore.QSize(500, 100))
            self.widget_0.setLayoutDirection(QtCore.Qt.RightToLeft)
            #    self.widget_0.setStyleSheet("background-color: rgb(170, 255, 255);")
            self.widget_0.setObjectName("widget_0")
            self.ui.verticalLayout_41.addWidget(
                self.widget_0)  # ВВОЖУ МУСОРНЫЕ ВИДЖЕТЫ ЧТОБЫ ВСЕ БЫЛО НИЗКО В ПОЛЕ СКРОЛЛАРЕНЫ

        self.rewrite_users()
        self.ui.textEdit.setDisabled(True)
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_15.setEnabled(False)
        self.ui.pushButton_12.clicked.connect(self.new_wallet)
        self.ui.pushButton_15.clicked.connect(self.send_coin)

        def moveWindow(event):
            # RESTORE BEFORE MOVE
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # SET TITLE BAR
        self.ui.frame_4.mouseMoveEvent = moveWindow  # ПРИВЯЗКА К ФРЕЙМУ КОТОРЫЙ ПЕРЕМЕЩАЕМЫЙ
        ## ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)
        self.show()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def new_wallet(self):
        requests.post('http://localhost:5000/wallet')
        balance = node.get_balance_2
        self.ui.label_15.setText(str(balance))

    def send_coin(self):

        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_6)
        text = self.ui.label_7.text()

        self.ui.pushButton_19.setText(text)
        self.ui.pushButton_21.clicked.connect(self.send_coin_2(text))

    def send_coin_2(self, text):
        # with open('one.json') as f:
        #     templates_2 = json.load(f)
        # for i in templates_2:
        #     if text == i['name']:
        #         to_json_3 = {"ID_purse": i['ID_purse'],
        #                      "name": i['name']}  # ЗДЕСЬ ИДЕТ ПЕРЕСТАНОВКА ЧЕЛОВЕКУ КОТОРОМУ МЫ НАПИСАЛИ НА 1 МЕСТО
        #         templates_2.remove(to_json_3)
        #         templates_2.insert(0, to_json_3)
        #         with open('one.json', 'w') as f:
        #             json.dump(templates_2, f, ensure_ascii=False)  # ВПИСЫВАЕМ
        # self.rewrite_users()
        # status_now = "send"  # ТОПО ПОЛУЧАЕТ ИЛИ ПРИНИМАЕТ        В ЭТОЙ ФУНКЦИИ СТАТУС ПОСТОЯННЫЙ, Т.К МЫ ЗАПИСЫВАЕМ СООБЩ ОТПРАВЛЕННЫЕ САМИМ "АДМИНОМ"  SEND сенд имеется ввиду получатель, GET ОТПРАВИТЕЛЬ, и через проверку этого параметра сообщ будет висеть справа или слева
        # with open('one.json') as f:
        #     templates_2 = json.load(f)
        # for i in templates_2:
        #     #        print (i['name'])
        #     if text == i['name']:
        #         name_of_new_purse = i["ID_purse"]
        # with open('wallet-{}.txt'.format(node.port), mode='r') as f:
        #     keys = f.readlines()
        #     private_key = keys[1]
        # signer = PKCS1_v1_5.new(RSA.importKey(
        #     binascii.unhexlify(private_key)))
        # h = SHA256.new((str(node.open_key()) + str(name_of_new_purse) +
        #                 str(cost) + str(message)).encode('utf8'))
        # signature_1 = signer.sign(h)
        # signature = binascii.hexlify(signature_1).decode('ascii')
        # to_json_message = {"status": status_now, "ID_purse": name_of_new_purse, "message": message,
        #                    "time": "delivering", "signature": signature}
        #
        # print(to_json_message)
        # with open('two.json') as f:
        #     templates_4 = json.load(f)  # СЧИТЫВАЕМ
        # templates_4.append(to_json_message)  # ДОПОЛНЯЕМ
        #
        # with open('two.json', 'w') as f:
        #     json.dump(templates_4, f, ensure_ascii=False)  # ВПИСЫВАЕМ
        # node.add_transaction_client(name_of_new_purse, 0.01, message)
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_4)

    def rewrite_users(self):
        for i in reversed(range(self.ui.verticalLayout_5.count())):
            self.ui.verticalLayout_5.itemAt(i).widget().setParent(None)  # ОТЧИСТКА ПРАВОЙ СКРОЛЛЭРИИ
        #     global some_buttons
        #     self.some_buttons = []
        with open('one.json') as f:
            templates_3 = json.load(f)  # СЧИТЫВАЕМ

        for i in templates_3:
            #   print(i['ID_purse'])
            self.widget_00 = QtWidgets.QWidget(self.ui.scrollAreaWidgetContents_2)

            #     self.widget_00 = QPushButton('Button {}'.format(i +1), self)

            self.widget_00.setMinimumSize(QtCore.QSize(360, 60))
            self.widget_00.setMaximumSize(QtCore.QSize(360, 60))
            self.widget_00.setObjectName("widget_00")
            self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.widget_00)
            self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_32.setSpacing(0)
            self.horizontalLayout_32.setObjectName("horizontalLayout_32")
            self.pushButton_30 = QtWidgets.QPushButton(self.widget_00)
            #   self.pushButton_30 ##########################################################
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.pushButton_30.sizePolicy().hasHeightForWidth())
            self.pushButton_30.setSizePolicy(sizePolicy)
            self.pushButton_30.setMinimumSize(QtCore.QSize(0, 60))
            self.pushButton_30.setStyleSheet("QPushButton{\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "font: 12pt \"Lucida Sans\";\n"
                                             "border: 0px solid;\n"
                                             "background-color: rgb(33, 97, 160)\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:hover{\n"
                                             "border: ipx solid #828282;\n"
                                             "color: rgb(20, 120, 250);\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:hover:pressed{\n"
                                             "background-color: rgb(255, 255, 255);\n"
                                             "font: 9pt \\\"Lucida Sans\\\";\n"
                                             "\n"
                                             "\n"
                                             "color: black;\n"
                                             "border-radius: 10px;\n"
                                             ";")
            self.pushButton_30.setObjectName("pushButton_30")
            self.pushButton_30.setText(i['name'])
            self.horizontalLayout_32.addWidget(self.pushButton_30)
            self.ui.verticalLayout_5.addWidget(self.widget_00)

            #       self.some_buttons.append(self.pushButton_30)
            text = self.pushButton_30.text()
            self.pushButton_30.clicked.connect(lambda ch, text=text: self.change_chat(text))

            # ПЕРЕПИСЫВЕТСЯ СПИСОК КОНТАКТОВ

        for i in range(6):
            self.widget_f = QtWidgets.QWidget(self.ui.scrollAreaWidgetContents)
            self.widget_f.setMinimumSize(QtCore.QSize(400, 100))
            self.widget_f.setMaximumSize(QtCore.QSize(500, 100))
            self.widget_f.setLayoutDirection(QtCore.Qt.RightToLeft)
            #    self.widget_0.setStyleSheet("background-color: rgb(170, 255, 255);")
            self.widget_f.setObjectName("widget_0")
            self.ui.verticalLayout_5.addWidget(
                self.widget_f)  # ВВОЖУ МУСОРНЫЕ ВИДЖЕТЫ ЧТОБЫ ВСЕ БЫЛО  ВЫСОКО В ЛЕВОМ ПОЛЕ СКРОЛЛАРЕНЫ

    def change_chat(self, text):
        #     print(text)

        for i in reversed(range(self.ui.verticalLayout_41.count())):
            self.ui.verticalLayout_41.itemAt(i).widget().setParent(None)  # ОТЧИСТКА правой СКРОЛЛЭРИИ

        for i in range(3):
            self.widget_0 = QtWidgets.QWidget(self.ui.scrollAreaWidgetContents)
            self.widget_0.setMinimumSize(QtCore.QSize(400, 100))
            self.widget_0.setMaximumSize(QtCore.QSize(500, 100))
            self.widget_0.setLayoutDirection(QtCore.Qt.RightToLeft)
            #    self.widget_0.setStyleSheet("background-color: rgb(170, 255, 255);")
            self.widget_0.setObjectName("widget_0")
            self.ui.verticalLayout_41.addWidget(
                self.widget_0)  # СНОВА ВВОЖУ МУСОРНЫЕ ВИДЖЕТЫ ЧТОБЫ ВСЕ БЫЛО НИЗКО В ПОЛЕ СКРОЛЛАРЕНЫ

        with open('one.json') as f:
            templates_2 = json.load(f)
        for i in templates_2:
            #        print (i['name'])
            #  self.ui.textEdit.setPlaceholderText("Write and press ALT to send a message to user "+i['name'] + ". . .")
            if text == i['name']:
                self.ui.label_7.setText(i['name'])
                self.ui.textEdit.setPlaceholderText(
                    "Write and press ALT to send a message to user " + i['name'] + ". . .")
                self.ui.textEdit.setText("")
                self.ui.textEdit.setDisabled(False)
                self.ui.pushButton_4.setEnabled(True)
                self.ui.pushButton_15.setEnabled(True)

                # ЭТОТ ЗДОРОВЫЙ БЛОК ВЫВОДА СООБЩЕНИЯ В ОБЩЕМ ТО И НЕ НУЖЕН. ПРОСТО ДОБАВИЛ ДЛЯ НАГЛЯДНОСТИ
                # сюда надо добаввить функцию по выводу старых мейлов

                with open('two.json') as f:
                    templates_7 = json.load(f)
                for j in templates_7:
                    if i["ID_purse"] == j[
                        "ID_purse"]:  # для этого пользователя из первого перебираем пользователей и находим блоки связанные с ним во 2 джисоне
                        message = j['message']
                        time = j['time']
                        if j["status"] == "send":

                            self.create_right_message(message, time)  # должно выводиться НАШЕ сообщение СПРАВА

                        else:

                            self.create_left_message(message, time)  # должно выводиться СООБЩЕНИЕ СОБЕСЕДНИКА СЛЕВО

    def create_right_message(self, message, time):
        #       print("в этом месте вставить функцию для вывода старых сообщений пользователя " + i['name'])
        #      mail = "в этом месте вставить функцию для вывода старых сообщений пользователя " + i['name']
        self.widget_5 = QtWidgets.QWidget(self.ui.scrollAreaWidgetContents)
        self.widget_5.setMinimumSize(QtCore.QSize(300, 90))
        self.widget_5.setMaximumSize(QtCore.QSize(300, 100))
        self.widget_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.widget_5.setStyleSheet("background-color: rgb(99,206,241);\n"
                                    "border: 1px solid #97C6E3;\n")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_28.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.label_13 = QtWidgets.QLabel(self.widget_5)
        self.label_13.setStyleSheet("font: 10pt \"Lucida Sans\";\n"
                                    "color: rgb(74, 128, 255);\n"
                                    "")
        self.label_13.setObjectName("label_13")
        self.label_13.setText("You  " + str(time))  # user_name +
        self.label_13.setStyleSheet("border: none;\n")
        self.verticalLayout_28.addWidget(self.label_13)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.widget_5)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_5.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Lucida Sans\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">что то тут должно быть но я хз</p></body></html>")
        self.textBrowser_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)  #############################
        self.textBrowser_5.setText(message)
        self.textBrowser_5.setStyleSheet("border: none;\n")
        self.verticalLayout_28.addWidget(self.textBrowser_5)
        self.ui.verticalLayout_41.addWidget(self.widget_5)

    def create_left_message(self, message, time):
        #       print("в этом месте вставить функцию для вывода старых сообщений пользователя " + i['name'])
        #      mail = "в этом месте вставить функцию для вывода старых сообщений пользователя " + i['name']
        self.widget_5 = QtWidgets.QWidget(self.ui.scrollAreaWidgetContents)
        self.widget_5.setMinimumSize(QtCore.QSize(300, 90))
        self.widget_5.setMaximumSize(QtCore.QSize(300, 100))
        self.widget_5.setLayoutDirection(QtCore.Qt.LeftToRight)  # ПАРАМЕТР СТОРОНЫ СООБЩЕНИЯ
        self.widget_5.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_28.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.label_13 = QtWidgets.QLabel(self.widget_5)
        self.label_13.setStyleSheet("font: 10pt \"Lucida Sans\";\n"
                                    "color: rgb(74, 128, 255);\n"
                                    "")
        self.label_13.setObjectName("label_13")
        self.label_13.setText(str(time))  # user_name +
        self.verticalLayout_28.addWidget(self.label_13)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.widget_5)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_5.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Lucida Sans\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">что то тут должно быть но я хз</p></body></html>")
        self.textBrowser_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)  #############################
        self.textBrowser_5.setText(message)
        self.verticalLayout_28.addWidget(self.textBrowser_5)
        self.ui.verticalLayout_41.addWidget(self.widget_5)

    def Add_New_user(self):
        name_of_new_user = self.ui.ввод_имени_польз.text()  # ПЕРЕМЕННАЯ ИМЕНИ НОВОГО ПОЛЬЗОВАТЕЛЯ
        name_of_new_purse = self.ui.lineEdit_кошелька.text()  # ПЕРЕМЕННАЯ КАШЕЛЬКА

        #    if ...        СЮДА ВПИХНЕШЬ ПРОВЕРКУ ЧЕРЕЗ IF             ТИПО ЕСТЬ ТАКОЙ КАШЕЛЕК ИЛИ НЕТ
        #    self.ui.label_статус.setText("НЕТ БЛЯДЬ ТАКОГО")

        to_json = {"ID_purse": name_of_new_purse, "name": name_of_new_user}

        with open('one.json') as f:
            templates = json.load(f)  # СЧИТЫВАЕМ
        templates.append(to_json)  # ДОПОЛНЯЕМ

        with open('one.json', 'w') as f:
            json.dump(templates, f, ensure_ascii=False)  # ВПИСЫВАЕМ
        #    jooo = templates['user']

        self.rewrite_users()

        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_4)
        self.ui.ввод_имени_польз.setText("")
        self.ui.lineEdit_кошелька.setText("")  # чищу поля ввода

    def checking(self, first, second):
        return first == second

    def load_messages(self, our_pub_key):
        with open('blockchain-5000.txt', mode='r') as f:
            file_content = f.readlines()
            blockchain = json.loads(file_content[0][:-1])
            for block in blockchain:
                for tx in block['transactions']:
                    if tx['recipient'] == our_pub_key:
                        with open('two.json') as f:
                            templates_5 = json.load(f)
                            checker = 0
                        for i in templates_5:
                            check = self.checking(i['signature'], tx['signature'])
                            if check:
                                checker = checker + 1
                        if checker == 0:
                            self.add_received_message_to_json(tx['msg'], tx['sender'], "recipient", block['timestamp'], tx['signature'])
                    elif tx['sender'] == our_pub_key:
                        with open('two.json') as f:
                            templates_5 = json.load(f)
                            checker = 0
                        for i in templates_5:
                            check = self.checking(i['signature'], tx['signature'])
                            if check == True:
                                checker = checker + 1
                        if checker == 0:
                            self.add_received_message_to_json(tx['msg'], tx['recipient'], "sender", block['timestamp'],  tx['signature'])

    # #   self.pushButton_30.clicked.connect(self.change_chat)
    def load_contacts(self, our_pub_key):
        with open('blockchain-5000.txt', mode='r') as f:
            file_content = f.readlines()
            blockchain = json.loads(file_content[0][:-1])
            for block in blockchain:
                for tx in block['transactions']:
                    if tx['recipient'] == our_pub_key:
                        with open('one.json') as f:
                            templates_5 = json.load(f)
                            checker = 0
                        for i in templates_5:
                            check = self.checking(i['ID_purse'], tx['sender'])
                            if check == True:
                                checker = checker + 1
                        if checker == 0:
                            self.Add_New_user_2(tx['sender'])
                    elif tx['sender'] == our_pub_key:
                        with open('one.json') as f:
                            templates_5 = json.load(f)
                            checker = 0
                        for i in templates_5:
                            check = self.checking(i['ID_purse'], tx['recipient'])
                            if check == True:
                                checker = checker + 1
                        if checker == 0:
                            self.Add_New_user_2(tx['recipient'])

    def add_received_message_to_json(self, msg, pub_key, status, time, signature):
        to_json_message_2 = {"status": status, "ID_purse": pub_key, "message": msg, "time": time, "signature": signature}
        with open('two.json') as f:
            templates_6 = json.load(f)  # СЧИТЫВАЕМ
            templates_6.append(to_json_message_2)  # ДОПОЛНЯЕМ
        with open('two.json', 'w') as f:
            json.dump(templates_6, f, ensure_ascii=False)  # ВПИСЫВАЕМ
            # записываем параметры ПОЛУЧЕННОГО сообщения во 2 джисон

    def Add_New_user_2(self, pub_key):  # УСЛИ НАМ ПИШЕТ НОВЫЙ ЧЕЛ ТО ЭТА ФУНКЦИЯ ДОБАВЛЯЕТ ЕГО В СПИСОК КОНТАКТОВ
        #  СТАРАЯ Add_New_user НЕ ПОДХОДИТ Т.К ТУТ ОДИН ПАРАМЕТР ИМЕНИ ЗАДАЕТ ПОЛЬЗОВАТЕЛЬ, А ВТОРОЙ ТИП НОМЕРА КОШЕЛЬКА БАРАТСЯ ИЗ БЛОКА,   КСТА ЕГО СЮДА ТОЖ МОЖЕШЬ ЧЕРЕЗ ПАРАМЕТРЫ ФУНКЦИИ ЗАКИНУТЬ
        name_of_new_user = "Stranger"  # ПЕРЕМЕННАЯ ИМЕНИ НОВОГО ПОЛЬЗОВАТЕЛЯ
        name_of_new_purse = pub_key  # ПЕРЕМЕННАЯ КАШЕЛЬКА БЕРЕТСЯ ИЗ БЛОКА

        to_json = {"ID_purse": name_of_new_purse, "name": name_of_new_user}

        with open('one.json') as f:
            templates = json.load(f)  # СЧИТЫВАЕМ
        templates.append(to_json)  # ДОПОЛНЯЕМ

        with open('one.json', 'w') as f:
            json.dump(templates, f, ensure_ascii=False)  # ВПИСЫВАЕМ
        #    jooo = templates['user']

        self.rewrite_users()

        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_4)
        self.ui.ввод_имени_польз.setText("")
        self.ui.lineEdit_кошелька.setDisabled(False)

    def lock_chat(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)

    def check_user(self):
        password_of_user = "123"
        password = self.ui.lineEdit.text()  ###########################
        if (password == password_of_user):
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
            self.ui.lineEdit.setText('')
            with app.app_context():
                node.load_keys_2()
            balance = node.get_balance_2()
            self.ui.label_15.setText(str(balance))
            self.ui.label_5.setText(str(node.open_key()))
            self.load_contacts(node.open_key())
            self.load_messages(node.open_key())
        else:
            self.ui.lineEdit.setText('')
            self.ui.lineEdit.repaint()
            self.ui.lineEdit.setPlaceholderText("Incorrect password! ")

    def send_message(self, text):
        message = self.ui.textEdit.toPlainText()  ##############################

        if message != '':
            text = self.ui.label_7.text()
            self.ui.textEdit.setPlaceholderText("Write and press ALT to send a message. . .")
            with open('one.json') as f:
                templates_2 = json.load(f)
            for i in templates_2:
                if text == i['name']:
                    to_json_3 = {"ID_purse": i['ID_purse'],
                                 "name": i['name']}  # ЗДЕСЬ ИДЕТ ПЕРЕСТАНОВКА ЧЕЛОВЕКУ КОТОРОМУ МЫ НАПИСАЛИ НА 1 МЕСТО
                    templates_2.remove(to_json_3)
                    templates_2.insert(0, to_json_3)
                    with open('one.json', 'w') as f:
                        json.dump(templates_2, f, ensure_ascii=False)  # ВПИСЫВАЕМ
            self.rewrite_users()

            self.cleantextEdit()
            #        user_name = "andrey"
            now = datetime.datetime.now()
            time = now.strftime("%H:%M")

            message = message.rstrip("\n")  # чущу блядские мусорные \n в конце мейла
            ############################################################################
            # СЮДА ВСТАВИТЬ ФУНКЦИЮ ОТПРАВКИ МЕЙЛА
            message = message + "\n"
            #  print(message)

            self.widget_5 = QtWidgets.QWidget(self.ui.scrollAreaWidgetContents)
            self.widget_5.setMinimumSize(QtCore.QSize(300, 90))
            self.widget_5.setMaximumSize(QtCore.QSize(300, 100))
            self.widget_5.setLayoutDirection(QtCore.Qt.RightToLeft)
            self.widget_5.setStyleSheet("background-color: rgb(170, 255, 255);")
            self.widget_5.setObjectName("widget_5")
            self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.widget_5)
            self.verticalLayout_28.setContentsMargins(11, 11, 11, 11)
            self.verticalLayout_28.setObjectName("verticalLayout_28")
            self.label_13 = QtWidgets.QLabel(self.widget_5)
            self.label_13.setStyleSheet("font: 10pt \"Lucida Sans\";\n"
                                        "color: rgb(74, 128, 255);\n"
                                        "")
            self.label_13.setObjectName("label_13")
            self.label_13.setText("you   in  " + time)  # user_name +
            self.verticalLayout_28.addWidget(self.label_13)
            self.textBrowser_5 = QtWidgets.QTextBrowser(self.widget_5)
            self.textBrowser_5.setObjectName("textBrowser_5")
            self.textBrowser_5.setHtml(
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Lucida Sans\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">что то тут должно быть но я хз</p></body></html>")
            self.textBrowser_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)  #############################
            self.textBrowser_5.setText(message)
            self.verticalLayout_28.addWidget(self.textBrowser_5)
            self.ui.verticalLayout_41.addWidget(self.widget_5)
            ################################################################################3
            status_now = "send"  # ТОПО ПОЛУЧАЕТ ИЛИ ПРИНИМАЕТ        В ЭТОЙ ФУНКЦИИ СТАТУС ПОСТОЯННЫЙ, Т.К МЫ ЗАПИСЫВАЕМ СООБЩ ОТПРАВЛЕННЫЕ САМИМ "АДМИНОМ"  SEND сенд имеется ввиду получатель, GET ОТПРАВИТЕЛЬ, и через проверку этого параметра сообщ будет висеть справа или слева
            with open('one.json') as f:
                templates_2 = json.load(f)
            for i in templates_2:
                #        print (i['name'])
                if text == i['name']:
                    name_of_new_purse = i["ID_purse"]
            with open('wallet-{}.txt'.format(node.port), mode='r') as f:
                keys = f.readlines()
                private_key = keys[1]
            signer = PKCS1_v1_5.new(RSA.importKey(
                binascii.unhexlify(private_key)))
            h = SHA256.new((str(node.open_key()) + str(name_of_new_purse) +
                            str(cost) + str(message)).encode('utf8'))
            signature_1 = signer.sign(h)
            signature =  binascii.hexlify(signature_1).decode('ascii')
            to_json_message = {"status": status_now, "ID_purse": name_of_new_purse, "message": message,
                               "time": "delivering", "signature": signature}

            print(to_json_message)
            with open('two.json') as f:
                templates_4 = json.load(f)  # СЧИТЫВАЕМ
            templates_4.append(to_json_message)  # ДОПОЛНЯЕМ

            with open('two.json', 'w') as f:
                json.dump(templates_4, f, ensure_ascii=False)  # ВПИСЫВАЕМ
            node.add_transaction_client(name_of_new_purse, 0.01, message)
            ############################################################################
        else:
            self.ui.textEdit.setPlaceholderText("Please, enter the message...")

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress and obj is self.ui.textEdit:
            if event.key() == QtCore.Qt.Key_Alt and self.ui.textEdit.hasFocus():
                text = self.ui.label_7.text()
                self.send_message(text)
                self.ui.textEdit.setText('')

        return super().eventFilter(obj, event)

        self.ui.textEdit.setText('')

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def cleantextEdit(self):
        self.ui.textEdit.setText('')

    #     self.ui.textEdit.Text.TrimEnd('\n', '\r')   #  мусор
    #     self.ui.textEdit.setDisabled(True) #  сбиваю курсор после отправки
    #     self.ui.textEdit.setDisabled(False)

    def main():
        app = QtWidgets.QApplication(sys.argv)
        window = OneWindow()
        window.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    OneWindow.main()
