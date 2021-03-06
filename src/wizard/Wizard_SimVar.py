'''
Created on 2010-05-26

@author:  Mathieu Gagnon
@contact: mathieu.gagnon.10@ulaval.ca
@organization: Universite Laval

@license
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
'''

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Wizard_SimVar.ui'
#
# Created: Wed May 26 12:34:54 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from model.PopModel import PopModelSim
from controller.VarDelegate import VarSimDelegate
from model.baseVarModel import GeneratorBaseModel

class Ui_WizardPage(object):
    '''
    This class was automatically generated using a qtdesigner .ui file and qt's pyuic4 program.
    It is a dialog allowing a user to manage simulation variables of a simulation
    '''
    def setupUi(self, WizardPage):
        WizardPage.setObjectName("WizardPage")
        WizardPage.resize(640, 480)
        self.parent = WizardPage.parent()
        self.tableView = QtGui.QTableView(WizardPage)
        self.tableView.setGeometry(QtCore.QRect(60, 90, 351, 261))
        self.tableView.setObjectName("tableView")
        self.horizontalLayoutWidget = QtGui.QWidget(WizardPage)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 360, 351, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label = QtGui.QLabel(WizardPage)
        self.label.setGeometry(QtCore.QRect(60, 60, 151, 21))
        self.label.setObjectName("label")

        self.retranslateUi(WizardPage)
        QtCore.QMetaObject.connectSlotsByName(WizardPage)
        QtCore.QObject.connect(self.pushButton_2,QtCore.SIGNAL("clicked()"),self.addVariable)
        QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL("clicked()"),self.removeVariable)
        
    def initializePage(self):
        '''
        @summary Reimplemented from QWizardPage.initializePage(self)
        Called automatically when the page is shown
        '''
        rowProfile = self.field("currProfile")
        currProfileName = self.parent.topWObject.popTab.comboBox.itemData(rowProfile.toInt()[0]).toString()
        baseModel = GeneratorBaseModel()
        self.tableView.setModel(PopModelSim(baseModel,str(currProfileName),self))
        self.tableView.setItemDelegate(VarSimDelegate(self.tableView,self.parent.topWObject))
        
    def validatePage(self):
        '''
        @summary Reimplemented from QWizardPage.validatePage(self)
        Called automatically when the page is about to be changed
        Little hack here : we assume that validatePage is only called when the user clicks the next button from this page
        Since Qt won't allow visiting a page that we already visited and that this mechanism is buried on the C++ side
        The only way to go back to the profile page is to call MainWizard.back() until we get back to it(only way Qt allows the visit of an already visited page)
        This is exactly what we're doing here
        '''
        self.wizard().back()
        self.wizard().back()
        self.wizard().back()
        self.wizard().back()
        return True
    
    def retranslateUi(self, WizardPage):
        WizardPage.setWindowTitle(QtGui.QApplication.translate("WizardPage", "WizardPage", None, QtGui.QApplication.UnicodeUTF8))
        WizardPage.setTitle(QtGui.QApplication.translate("WizardPage", "Profile - Step 3", None, QtGui.QApplication.UnicodeUTF8))
        WizardPage.setSubTitle(QtGui.QApplication.translate("WizardPage", "Finally, add simulation variables that weren\'t available at first in the demography file.", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("WizardPage", "Add Variable", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("WizardPage", "Remove Variable", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("WizardPage", "Simulation Variables :", None, QtGui.QApplication.UnicodeUTF8))

    def addVariable(self):
        '''
        @summary Adds a variable to the simulation variables list
        '''
        if self.tableView.model().getBaseModel().howManyProfiles():
            index = self.tableView.currentIndex()
        
            if index.isValid():
                self.tableView.model().insertRow(index.row())
            else:
                self.tableView.model().insertRow(self.tableView.model().rowCount())
            return
        
        QtGui.QMessageBox.information(self, "Add Variable aborted", "Before adding variables, make sure a valid profile is selected!")
        
    def removeVariable(self):
        '''
        @summary Removes a variable from the simulation variables list
        '''
        index = self.tableView.currentIndex()
        if index.isValid():
            self.tableView.model().removeRow(index.row())
            