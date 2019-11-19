import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    

import pandas as pd
import numpy as np
import sklearn as sk
from sklearn import metrics, datasets
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

import matplotlib.patches as mpatches

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320, 140))    
        self.setWindowTitle("Rainfall Prediction") 

        

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('TempHigh')
        self.line1 = QLineEdit(self)

        self.line1.move(150, 20)
        self.line1.resize(200, 32)
        self.nameLabel.move(20, 20)

        #
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('TempAvgF')
        self.line2 = QLineEdit(self)

        self.line2.move(150, 60)
        self.line2.resize(200, 32)
        self.nameLabel.move(20,60)
        
        ##3
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('TempLowF')
        self.line3 = QLineEdit(self)

        self.line3.move(150, 100)
        self.line3.resize(200, 32)
        self.nameLabel.move(20,100)


         
        ##3
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('DewPointHighF')
        self.line4 = QLineEdit(self)

        self.line4.move(150, 140)
        self.line4.resize(200, 32)
        self.nameLabel.move(20,140)


         
        ##3
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('DewPointAvgF')
        self.line5 = QLineEdit(self)

        self.line5.move(150, 180)
        self.line5.resize(200, 32)
        self.nameLabel.move(20,180)

         
        ##3
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('DewPointLowF')
        self.line6 = QLineEdit(self)

        self.line6.move(150, 220)
        self.line6.resize(200, 32)
        self.nameLabel.move(20,220)


         
        ##3
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('HumidityHighPercent')
        self.line7 = QLineEdit(self)

        self.line7.move(150, 260)
        self.line7.resize(200, 32)
        self.nameLabel.move(20,260)


         
        ##3
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('HumidityAvgPercent')
        self.line8 = QLineEdit(self)

        self.line8.move(150, 300)
        self.line8.resize(200, 32)
        self.nameLabel.move(20,300)


         
        ##3
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('HumidityLowPercent')
        self.line9 = QLineEdit(self)

        self.line9.move(150, 340)
        self.line9.resize(200, 32)
        self.nameLabel.move(20,340)


         
        ##3
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('SeaLevelPressureAvgInches')
        self.line10 = QLineEdit(self)

        self.line10.move(150, 380)
        self.line10.resize(200, 32)
        self.nameLabel.move(20,380)


         
        ##3
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('VisibilityHighMiles')
        self.line11 = QLineEdit(self)

        self.line11.move(150, 420)
        self.line11.resize(200, 32)
        self.nameLabel.move(20,420)

         
        ##3
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('VisibilityAvgMiles')
        self.line12 = QLineEdit(self)

        self.line12.move(150, 460)
        self.line12.resize(200, 32)
        self.nameLabel.move(20,460)

         
        ##3
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('VisibilityLowMiles')
        self.line13 = QLineEdit(self)

        self.line13.move(150, 500)
        self.line13.resize(200, 32)
        self.nameLabel.move(20,500)

         
        ##3
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('WindHighMPH ')
        self.line14 = QLineEdit(self)

        self.line14.move(150, 540)
        self.line14.resize(200, 32)
        self.nameLabel.move(20,540)

         
        ##3
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('WindAvgMPH')
        self.line15 = QLineEdit(self)

        self.line15.move(150, 580)
        self.line15.resize(200, 32)
        self.nameLabel.move(20,580)

         
        ##3
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('WindGustMPH')
        self.line16 = QLineEdit(self)

        self.line16.move(150, 620)
        self.line16.resize(200, 32)
        self.nameLabel.move(20,620)




        
        
        pybutton = QPushButton('OK', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(20, 660)        
    
    
    
   
    
    def clickMethod(self):
        arr=[]

        
        arr.append(self.line1.text())
        arr.append(self.line2.text())
        arr.append(self.line3.text())
        arr.append(self.line4.text())
        arr.append(self.line5.text())
        arr.append(self.line6.text())
        arr.append(self.line7.text())
        arr.append(self.line8.text())
        arr.append(self.line9.text())
        arr.append(self.line10.text())
        arr.append(self.line11.text())
        arr.append(self.line12.text())
        arr.append(self.line13.text())
        arr.append(self.line14.text())
        arr.append(self.line15.text())
        arr.append(self.line16.text())
    
        arrs = []
        while len(arr) > 1:
                pice = arr[:1]
                arrs.append(pice)
                arr= arr[1:]
        arrs.append(arr)
     
        print(arrs)



        ### MAIN CODE HERE

        data = pd.read_csv("austin_final.csv")

        X = data.drop(['PrecipitationSumInches'], axis=1)
        Y_temp = data['PrecipitationSumInches']
        Y_temp = Y_temp.values.reshape(-1, 1)

       
        Y = []

        x1 = pd.DataFrame(columns=X.columns.values)
        x2 = pd.DataFrame(columns=X.columns.values)
        x3 = pd.DataFrame(columns=X.columns.values)
        x4 = pd.DataFrame(columns=X.columns.values)
        for i in range(Y_temp.size):
            if(Y_temp[i]<0.001):
                Y.append(1)
                x1.loc[i] = X.loc[i]
            elif(Y_temp[i]>=0.001 and Y_temp[i]<0.1):
                Y.append(2)
                x2.loc[i] = X.loc[i]
            elif(Y_temp[i]>=0.1 and Y_temp[i]<1.2):
                Y.append(3)
                x3.loc[i] = X.loc[i]
            else:
                Y.append(4)
                x4.loc[i] = X.loc[i]

        Y = np.array(Y).reshape(len(Y), )

        logr = LogisticRegression(multi_class='ovr', solver='liblinear').fit(X, Y)
        print(logr.score(X,Y)*100)
        
        input=np.array(arrs)
        input= input.astype(np.float)

        #input = np.array([[50], [60], [45], [67], [49], [43], [93], [75], [57], [29.68], [10], [7], [2], [20], [4], [31]])
        #input = np.array([[58], [43], [28], [37], [22], [18], [75]])
        input = input.reshape(1, -1)
        classes = ['None', 'No Rain', 'Drizzles', 'Moderate Rains', 'Heavy Rains']
        print(classes[int(logr.predict(input))])

        x1 = x1.filter(['TempAvgF', 'DewPointAvgF', 'HumidityAvgPercent', 'SeaLevelPressureAvgInches', 'VisibilityAvgMiles', 'WindAvgMPH'], axis=1)
        x2 = x2.filter(['TempAvgF', 'DewPointAvgF', 'HumidityAvgPercent', 'SeaLevelPressureAvgInches', 'VisibilityAvgMiles', 'WindAvgMPH'], axis=1)
        x3 = x3.filter(['TempAvgF', 'DewPointAvgF', 'HumidityAvgPercent', 'SeaLevelPressureAvgInches', 'VisibilityAvgMiles', 'WindAvgMPH'], axis=1)
        x4 = x4.filter(['TempAvgF', 'DewPointAvgF', 'HumidityAvgPercent', 'SeaLevelPressureAvgInches', 'VisibilityAvgMiles', 'WindAvgMPH'], axis=1)


        for i in range(6):
            plt.subplot(3,2,i+1)
            plt.scatter(x1.index.values, x1[x1.columns.values[i]], color='b')
            plt.scatter(x2.index.values, x2[x2.columns.values[i]], color='r')
            plt.scatter(x3.index.values, x3[x3.columns.values[i]], color='g')
            plt.scatter(x4.index.values, x4[x4.columns.values[i]], color='y')
            plt.title(x1.columns.values[i])

        blue_patch = mpatches.Patch(color='blue', label='No rains')
        red_patch = mpatches.Patch(color='red', label='Drizzles')
        green_patch = mpatches.Patch(color='green', label='Moderate rains')
        yellow_patch = mpatches.Patch(color='yellow', label='Heavy rains')
        plt.legend(handles=[blue_patch, red_patch, green_patch, yellow_patch], bbox_to_anchor=(1.05, 2), loc=2, borderaxespad=0.)

        plt.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
