"""
Автор: Пронин Роман Андреевич
Описание программы: приложение для людей, ведущих здоровый образ жизни
Версия: v1.0
Cendres_Chaudes
"""


import sys
import re
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
import mysql.connector
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import pyqtgraph as pg

from intro_frame import *
from auth_frame import *
from reg_frame import *
from mainwindow_frame import *
from progfood_main_frame import *
from progfood_rowchange_frame import *
from progfood_foodbase_frame import *
from progfood_addnewfood_frame import *
from trainingres_main_frame import *
from trainingres_addresult_frame import *
from trainingres_resultchange_frame import *
from trainingres_exercisebase_frame import *
from weather_frame import *
#from achievements_frame import *
from changeinfo_frame import *
from about_frame import *


def close_program():
    sys.exit(app.exec_())


class MessageBoxWindow(QtWidgets.QMessageBox):
    def __init__(self, title, text, icon_type):
        super(MessageBoxWindow, self).__init__()
        self.setWindowTitle(f'{title}')
        self.setText(f'{text}')
        if icon_type == 'Warning':
            self.setIcon(QtWidgets.QMessageBox.Warning)
        elif icon_type == 'Critical':
            self.setIcon(QtWidgets.QMessageBox.Critical)
        elif icon_type == 'Information':
            self.setIcon(QtWidgets.QMessageBox.Information)
        elif icon_type == 'Question':
            self.setIcon(QtWidgets.QMessageBox.Question)
        self.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.show()


class IntroWindow(QtWidgets.QDialog):
    def __init__(self):
        super(IntroWindow, self).__init__()
        self.ui = Ui_Intro()
        self.ui.setupUi(self)
        self.setFixedSize(550, 260)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        QtCore.QTimer.singleShot(3000, self.open_authorization_window)

    def open_authorization_window(self):
        self.close()
        self.authorization_UI = AuthorizationWindow()
        self.authorization_UI.show()


class AuthorizationWindow(QtWidgets.QDialog):
    def __init__(self):
        super(AuthorizationWindow, self).__init__()
        self.ui = Ui_Authorization()
        self.ui.setupUi(self)
        self.setFixedSize(310, 420)
        self.ui.pushButton_enterProgram.clicked.connect(self.enter_program)
        self.ui.pushButton_openRegWindow.clicked.connect(self.open_registration_window)
        self.ui.pushButton_closeProgram.clicked.connect(close_program)

    def enter_program(self):
        curs = mycon.cursor(buffered=True)
        info_auth = (self.ui.lineEdit_inputLogin.text(),
                      self.ui.lineEdit_inputPassword.text())
        query = 'SELECT * FROM user_authorization WHERE login = %s and password = %s'
        curs.execute(query, (info_auth[0], info_auth[1]))
        if True:
            self.close()
            print(info_auth[0])
            global user_info
            query = 'SELECT * FROM user_authorization WHERE login = %s'
            curs.execute(query, (info_auth[0],))
            user_auth = list(*curs)
            query = 'SELECT * FROM user_info WHERE ID = %s'
            curs.execute(query, (user_auth[0],))
            user_info = list(*curs)
            user_info = {'ID': user_auth[0], 'login': user_auth[1], 'password': user_auth[2],
                         'name': user_info[1], 'surname': user_info[2], 'patronymic': user_info[3],
                         'gender': user_info[4], 'birthdate': str(user_info[5]), 'country': user_info[6],
                         'city': user_info[7]}
            print(user_info)
            self.mainwindow_UI = MainWindow()
            self.mainwindow_UI.show()
        else:
            self.message = MessageBoxWindow('Ошибка!',
                                            'Введены неверно логин и/или пароль или данный аккаунт пользователя не существует.',
                                            'Critical')

    def open_registration_window(self):
        self.close()
        self.registration_UI = RegistrationWindow()
        self.registration_UI.show()


class RegistrationWindow(QtWidgets.QDialog):
    def __init__(self):
        super(RegistrationWindow, self).__init__()
        self.ui = Ui_Registration()
        self.ui.setupUi(self)
        self.setFixedSize(310, 845)
        self.ui.pushButton_acceptReg.clicked.connect(self.accept_registration)
        self.ui.pushButton_closeWindow.clicked.connect(self.close_registration_window)
        self.ui.pushButton_closeProgram.clicked.connect(close_program)

    def accept_registration(self):
        if self.ui.radioButton_man.isChecked():
            gender = 'Мужской'
        else:
            gender = 'Женский'
        if len(self.ui.lineEdit_inputFIO.text().split(' ')) == 2:
            surname, name = self.ui.lineEdit_inputFIO.text().split(' ')
            patronymic = ''
        else:
            surname, name, patronymic = self.ui.lineEdit_inputFIO.text().split(' ')
        info_input = (name,
                      surname,
                      patronymic,
                      gender,
                      self.ui.lineEdit_inputBirthdate.text(),
                      self.ui.lineEdit_inputCountry.text(),
                      self.ui.lineEdit_inputCity.text(),
                      self.ui.lineEdit_inputLogin.text(),
                      self.ui.lineEdit_inputPassword.text())
        try:
            if (name == '' or surname == '' or self.ui.lineEdit_inputBirthdate.text() == ''
                or self.ui.lineEdit_inputCountry.text() == '' or self.ui.lineEdit_inputCity.text() == ''
                or self.ui.lineEdit_inputLogin.text() == '' or self.ui.lineEdit_inputPassword.text() == ''):
                raise Exception

            birthdate_check = re.search(r'\d{4}-\d{2}-\d{2}', f'{self.ui.lineEdit_inputBirthdate.text()}')
            if birthdate_check.group(0) != self.ui.lineEdit_inputBirthdate.text():
                raise Exception

            if self.ui.lineEdit_inputLogin.text()[0].isdigit():
                raise Exception

            if self.ui.lineEdit_inputPassword.text() != self.ui.lineEdit_inputSamePassword.text():
                raise Exception

            current_year = datetime.datetime.today().year
            current_month = datetime.datetime.today().month
            current_day = datetime.datetime.today().day
            bd_year, bd_month, bd_day = (self.ui.lineEdit_inputBirthdate.text()[:4],
                                         self.ui.lineEdit_inputBirthdate.text()[5:7],
                                         self.ui.lineEdit_inputBirthdate.text()[8:])
            if int(bd_year) > current_year:
                raise Exception
            if int(bd_month) < 1 or int(bd_month) > 12:
                raise Exception
            if (int(bd_day) < 1
                or (int(bd_day) > 28 and bd_month == '02' and (int(bd_year)//4 != 0 or int(bd_year)//100 != 0 or int(bd_year)//400 != 0))
                or (int(bd_day) > 29 and bd_month == '02' and (int(bd_year)//4 == 0 or int(bd_year)//100 == 0 or int(bd_year)//400 == 0))
                or (int(bd_day) > 30 and (bd_month == '04' or bd_month == '06' or bd_month == '09' or bd_month == '11'))
                or (int(bd_day) > 31 and (bd_month == '01' or bd_month == '03' or bd_month == '05' or bd_month == '07' or bd_month == '08' or bd_month == '010'  or bd_month == '12'))):
                raise Exception
        except:
            self.message = MessageBoxWindow('Ошибка!',
                                            'Неверно заполнены поля. Пожалуйста, проверьте еще раз.',
                                            'Critical')
        else:
            curs = mycon.cursor()
            query = ('INSERT INTO user_info (name, surname, patronymic, gender, birthdate, country, city) '
                     'VALUES (%s, %s, %s, %s, %s, %s, %s)')
            curs.execute(query, (info_input[0], info_input[1], info_input[2],
                                 info_input[3], info_input[4], info_input[5],
                                 info_input[6]))
            query = ('INSERT INTO user_authorization (ID, login, password) '
                     'VALUES ((SELECT ID FROM user_info ORDER BY ID DESC LIMIT 0,1), %s, %s)')
            curs.execute(query, (info_input[-2], info_input[-1]))
            curs.close()
            mycon.commit()
            self.close()
            self.authorization_UI = AuthorizationWindow()
            self.authorization_UI.show()

    def close_registration_window(self):
        self.close()
        self.authorization_UI = AuthorizationWindow()
        self.authorization_UI.show()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(360, 540)
        self.ui.pushButton_progFood.clicked.connect(self.open_program_food_window)
        self.ui.pushButton_trainingRes.clicked.connect(self.open_training_results_window)
        self.ui.pushButton_weather.clicked.connect(self.open_weather_window)
        self.ui.pushButton_achievements.clicked.connect(self.open_achievements_window)
        self.ui.pushButton_changeInfo.clicked.connect(self.open_change_info_window)
        self.ui.pushButton_changeUser.clicked.connect(self.change_user)
        self.ui.pushButton_aboutProg.clicked.connect(self.open_about_window)
        self.ui.pushButton_closeProgram.clicked.connect(close_program)

    def open_program_food_window(self):
        self.close()
        self.program_food_UI = ProgramFoodWindow()
        self.program_food_UI.show()

    def open_training_results_window(self):
        self.close()
        self.training_results_UI = TrainingInfoWindow()
        self.training_results_UI.show()

    def open_weather_window(self):
        self.close()
        self.weather_UI = WeatherWindow()
        self.weather_UI.show()

    def open_achievements_window(self):
        self.message = MessageBoxWindow('Внимание!',
                                        'Ожидайте реализацию функциональной возможности в следующей версии программы.',
                                        'Information')

    def open_change_info_window(self):
        self.close()
        self.change_info_UI = ChangeInfoWindow()
        self.change_info_UI.show()

    def change_user(self):
        self.close()
        self.authorization_UI = AuthorizationWindow()
        self.authorization_UI.show()

    def open_about_window(self):
        self.close()
        self.about_UI = AboutInfoWindow()
        self.about_UI.show()


class ProgramFoodWindow(QtWidgets.QDialog):
    def __init__(self):
        super(ProgramFoodWindow, self).__init__()
        self.ui = Ui_ProgramFood()
        self.ui.setupUi(self)
        self.setFixedSize(1300, 890)
        self.ui.lineEdit_outputAge.setText()
        self.ui.lineEdit_outputCalcKcal.setText('00')
        self.ui.lineEdit_outputCalcProts.setText('00')
        self.ui.lineEdit_outputCalcFats.setText('00')
        self.ui.lineEdit_outputCalcCarbs.setText('00')
        self.ui.lineEdit_outputPlanKcal.setText('00')
        self.ui.lineEdit_outputPlanProts.setText('00')
        self.ui.lineEdit_outputPlanFats.setText('00')
        self.ui.lineEdit_outputPlanCarbs.setText('00')
        self.onlyInt = QtGui.QIntValidator()
        self.onlyInt.setRange(0, 300)
        self.ui.lineEdit_inputHeight.setValidator(self.onlyInt)
        self.ui.lineEdit_inputWeight.setValidator(self.onlyInt)
        self.ui.pushButton_openFoodBase.clicked.connect(self.open_foodbase_window)
        self.ui.pushButton_rowChange.clicked.connect(self.open_rowchange_window)
        self.ui.pushButton_closeWindow.clicked.connect(self.open_mainwindow)
        if True:
            self.ui.radioButton_man.setChecked(True)
        else:
            self.ui.radioButton_woman.setChecked(True)

    def open_foodbase_window(self):
        self.food_base_UI = FoodBaseWindow()
        self.food_base_UI.show()

    def open_rowchange_window(self):
        self.row_change_UI = RowChangeWindow()
        self.row_change_UI.show()

    def open_mainwindow(self):
        self.close()
        self.mainwindow_UI = MainWindow()
        self.mainwindow_UI.show()


class FoodBaseWindow(QtWidgets.QDialog):
    def __init__(self):
        super(FoodBaseWindow, self).__init__()
        self.ui = Ui_FoodBase()
        self.ui.setupUi(self)
        self.setFixedSize(1100, 560)
        self.onlyInt = QtGui.QIntValidator()
        self.onlyInt.setRange(0, 1000)
        self.ui.lineEdit_inputWeightProduct.setValidator(self.onlyInt)
        self.ui.pushButton_replenishFoodBase.clicked.connect(self.open_addfood_window)
        self.ui.pushButton_closeWindow.clicked.connect(self.close_window)

    def open_addfood_window(self):
        self.add_new_food_UI = AddNewFoodWindow()
        self.add_new_food_UI.show()

    def close_window(self):
        self.close()

class RowChangeWindow(QtWidgets.QDialog):
    def __init__(self):
        super(RowChangeWindow, self).__init__()
        self.ui = Ui_RowChange()
        self.ui.setupUi(self)
        self.setFixedSize(270, 290)
        self.onlyInt = QtGui.QIntValidator()
        self.onlyInt.setRange(0, 1000)
        self.ui.lineEdit_inputWeightProduct.setValidator(self.onlyInt)
        self.ui.pushButton_closeWindow.clicked.connect(self.close_window)

    def close_window(self):
        self.close()

class AddNewFoodWindow(QtWidgets.QDialog):
    def __init__(self):
        super(AddNewFoodWindow, self).__init__()
        self.ui = Ui_AddNewFood()
        self.ui.setupUi(self)
        self.setFixedSize(340, 580)
        self.ui.pushButton_closeWindow.clicked.connect(self.close)

    def close_window(self):
        self.close()

class TrainingInfoWindow(QtWidgets.QDialog):
    def __init__(self):
        super(TrainingInfoWindow, self).__init__()
        self.ui = Ui_TrainingInfo()
        self.ui.setupUi(self)
        self.setFixedSize(1300, 630)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout = self.ui.layoutforgraph
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)
        self.data = [0, 1, 2, 3, 4, 20.2]
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)
        self.ax.plot(self.data, "*-")
        self.ax.set_xlabel('Номер тренировки')
        self.ax.set_ylabel('Результат')
        self.canvas.draw()
        self.ui.pushButton_addResult.clicked.connect(self.open_addresult_window)
        self.ui.pushButton_resultChange.clicked.connect(self.open_resultchange_window)
        self.ui.pushButton_exerciseBase.clicked.connect(self.open_exercisebase_window)
        self.ui.pushButton_closeWindow.clicked.connect(self.close_window)

    def open_addresult_window(self):
        self.add_result_UI = AddResultWindow()
        self.add_result_UI.show()

    def open_resultchange_window(self):
        self.result_change_UI = ResultChangeWindow()
        self.result_change_UI.show()

    def open_exercisebase_window(self):
        self.exercise_base_UI = ExerciseBaseWindow()
        self.exercise_base_UI.show()

    def close_window(self):
        self.close()
        self.mainwindow_UI = MainWindow()
        self.mainwindow_UI.show()


class AddResultWindow(QtWidgets.QDialog):
    def __init__(self):
        super(AddResultWindow, self).__init__()
        self.ui = Ui_AddResult()
        self.ui.setupUi(self)
        self.setFixedSize(270, 295)
        self.ui.pushButton_closeWindow.clicked.connect(self.close_window)

    def close_window(self):
        self.close()

class ResultChangeWindow(QtWidgets.QDialog):
    def __init__(self):
        super(ResultChangeWindow, self).__init__()
        self.ui = Ui_ResultChange()
        self.ui.setupUi(self)
        self.setFixedSize(270, 360)
        self.ui.pushButton_closeWindow.clicked.connect(self.close_window)

    def close_window(self):
        self.close()

class ExerciseBaseWindow(QtWidgets.QDialog):
    def __init__(self):
        super(ExerciseBaseWindow, self).__init__()
        self.ui = Ui_ExerciseBase()
        self.ui.setupUi(self)
        self.setFixedSize(270, 370)
        self.ui.pushButton_closeWindow.clicked.connect(self.close_window)

    def close_window(self):
        self.close()

class WeatherWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(WeatherWindow, self).__init__()
        self.ui = Ui_Weather()
        self.ui.setupUi(self)
        self.setFixedSize(860, 600)
        curs = mycon.cursor()
        query = 'SELECT ID FROM user_authorization WHERE login = %s'
        curs.execute(query, (user_login,))
        user_ID = list(*curs)[0]
        query = 'SELECT country, city FROM user_info WHERE ID = %s'
        curs.execute(query, (user_ID,))
        user_country, user_city = list(*curs)
        self.search = user_country + ' ' + user_city
        self.webview = QtWebEngineWidgets.QWebEngineView()
        self.webview.load(QtCore.QUrl(f'https://www.google.ru/search?q=погода+{self.search}'))
        self.ui.verticalLayout.addWidget(self.webview)
        self.ui.pushButton_closeWindow.clicked.connect(self.open_mainwindow)
        self.ui.pushButton_optInfo.clicked.connect(self.open_optinfo_window)

    def open_mainwindow(self):
        self.close()
        self.mainwindow_UI = MainWindow()
        self.mainwindow_UI.show()

    def open_optinfo_window(self):
        self.message = MessageBoxWindow('Внимание!',
                                        'Ожидайте реализацию функциональной возможности в следующей версии программы.',
                                        'Information')


class OptionalInfoWindow(QtWidgets.QDialog):
    pass


class AchievementsWindow(QtWidgets.QDialog):
    pass


class ChangeInfoWindow(QtWidgets.QDialog):
    def __init__(self):
        super(ChangeInfoWindow, self).__init__()
        self.ui = Ui_ChangeInfo()
        self.ui.setupUi(self)
        self.setFixedSize(320, 810)
        curs = mycon.cursor()
        query = 'SELECT ID FROM user_authorization WHERE login = %s'
        curs.execute(query, (user_login,))
        user_ID = list(*curs)[0]
        query = 'SELECT * FROM user_info WHERE ID = %s'
        curs.execute(query, (user_ID,))
        user_info = list(*curs)
        self.ui.lineEdit_inputLogin.setText(user_login)
        self.ui.lineEdit_inputFIO.setText('Pass')
        self.ui.lineEdit_inputBirthdate.setText(user_info[5])
        self.ui.lineEdit_inputCountry.setText(user_info[6])
        self.ui.lineEdit_inputCity.setText(user_info[7])
        self.ui.pushButton_closeWindow.clicked.connect(self.open_mainwindow)
        if True:
            self.ui.radioButton_man.setChecked(True)
        else:
            self.ui.radioButton_woman.setChecked(True)

    def open_mainwindow(self):
        self.close()
        self.mainwindow_UI = MainWindow()
        self.mainwindow_UI.show()

class AboutInfoWindow(QtWidgets.QDialog):
    def __init__(self):
        super(AboutInfoWindow, self).__init__()
        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self)
        self.setFixedSize(575, 675)
        self.ui.pushButton_closeWindow.clicked.connect(self.open_mainwindow)

    def open_mainwindow(self):
        self.close()
        self.mainwindow_UI = MainWindow()
        self.mainwindow_UI.show()


mycon = mysql.connector.connect(host='127.0.0.1',
                                database='sport_app',
                                user='root',
                                password='Qwerty123')

app = QtWidgets.QApplication(sys.argv)
intro_UI = IntroWindow()
intro_UI.show()
sys.exit(app.exec_())