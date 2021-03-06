'''
Created on 2009-10-15

@author:  Majid Malis
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

# Form implementation generated from reading ui file 'trees.ui'
#
# Created: Thu Oct 15 15:37:50 2009
#      by: PyQt4 UI code generator 4.5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtXml
from PyQt4 import QtGui
from editor.AdvancedTreeEditor import MedTreeView
from editor.mainEditorFrame import MainEditorWindow
from model.baseTreatmentsModel import BaseTreatmentsModel


import os
import zipfile

class Ui_trees(object):
    '''
    This class is an automatically generated python file using the pyuic4 program and .ui file generated by Qt_Designer
    This class is the mainWindow's tab containing the processes information of the simulation
    '''
    def __init__(self, parent):
        '''
        @summary Constructor
        @param parent: application's mainWindow
        '''
        self.parent = parent

    def setupUi(self, trees):
        trees.setObjectName("trees")
        #Creating the splitter
        self.splitter = QtGui.QSplitter(self)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter_2")
        #Creating the widget for the splitter
        self.widgetLeft = QtGui.QWidget(self.splitter)
        self.widgetRight = QtGui.QWidget(self.splitter)
        
        #Creating Layouts for the tab widget
        #Left splitter layout
        self.layoutSplitterLeft = QtGui.QVBoxLayout()
        #Right splitter layout
        self.layoutSplitterRight = QtGui.QVBoxLayout()
        #Layout for the add and Delete Buttons
        self.horizontalLayout = QtGui.QHBoxLayout()
        #Layout for the label "Process Tree" and the load predefined Process Button
        self.horizontalLayoutBottom = QtGui.QHBoxLayout()
        #MainLayout
        self.mainLayout = QtGui.QVBoxLayout()
        
        #Adding child layout to the main Layout
        self.mainLayout.addWidget(self.splitter)
        
        #Populating left splitter layout at first
        #Label
        self.tableLabel = QtGui.QLabel()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.tableLabel.setFont(font)
        self.tableLabel.setObjectName("tableLabel")
        #Adding label to the it's layout
        self.layoutSplitterLeft.addWidget(self.tableLabel)
        
        #Processs List
        self.processesList = ArrowsAwareTableView()
        self.processesList.setObjectName("processesList")
        self.processesList.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.processesList.horizontalHeader().setSortIndicatorShown(True)
        self.processesList.setSortingEnabled(True)
        #My preferences
        self.processesList.setSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        self.processesList.setDragEnabled(True)
        self.processesList.setAcceptDrops(True)
        self.processesList.setDropIndicatorShown(True)
        self.processesList.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.processesList.setDefaultDropAction(QtCore.Qt.DropAction(QtCore.Qt.MoveAction))
        self.processesList.setDragDropOverwriteMode(False)
        #Adding Process List to the layout
        self.layoutSplitterLeft.addWidget(self.processesList)
        #Adding layout of the add and delete buttons
        self.layoutSplitterLeft.addLayout(self.horizontalLayout)
        #Populating the add and delete layout
        self.add = QtGui.QPushButton()
        self.add.setObjectName("add")
        self.add.setFixedSize(QtCore.QSize(77,25))
        self.horizontalLayout.addWidget(self.add)
        self.delete = QtGui.QPushButton()
        self.delete.setObjectName("delete")
        self.delete.setFixedSize(QtCore.QSize(77,25))
        self.horizontalLayout.addWidget(self.delete)        
        self.horizontalLayout.addStretch()
        
        #Finally, for the left splitter, add the openTreeEditorButton
        self.pushButton_treeEditor = QtGui.QPushButton()
        self.pushButton_treeEditor.setText("Open tree editor")
        self.pushButton_treeEditor.setObjectName("pushButton_treeEditor")
        self.pushButton_treeEditor.setFixedSize(QtCore.QSize(200,25))
        #Add the button the the layout
        self.layoutSplitterLeft.addWidget(self.pushButton_treeEditor)
        
        #Populating right splitter
        #Top label
        self.tableLabel_2 = QtGui.QLabel()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        
        self.tableLabel_2.setFont(font)
        self.tableLabel_2.setObjectName("tableLabel_2")
        #Adding it to its layout
        self.layoutSplitterRight.addWidget(self.tableLabel_2)
        
        #Creating process view 
        self.SVGViewScroll = QtGui.QScrollArea()
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background,QtGui.QColor(173,216,250)) 
        self.SVGViewScroll.viewport().setPalette(palette)
        self.SVGViewScroll.setWidgetResizable(True)
        #Adding it to right splitter layout
        self.layoutSplitterRight.addWidget(self.SVGViewScroll)
        self.SVGViewScroll.setSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        #Setting the bottom layout
        #First, set horizontalLAyoutBottom as last Child
        self.layoutSplitterRight.addLayout(self.horizontalLayoutBottom)
        #Load Parameters Label
        self.loadParameters = QtGui.QLabel()
        self.loadParameters.setObjectName("loadParameters")
        self.loadParameters.setFixedSize(QtCore.QSize(170,57))
        #Adding it to its layout
        self.horizontalLayoutBottom.addWidget(self.loadParameters)
        #Set Alignment
        
        #Load ParameterButton
        self.parametersToolButton = QtGui.QToolButton()
        self.parametersToolButton.setObjectName("parametersToolButton")
        self.parametersToolButton.setFixedSize(QtCore.QSize(30,31))
        #Adding it to its layout
        self.horizontalLayoutBottom.addWidget(self.parametersToolButton)
        #Set Alignment and add Stretch
        self.horizontalLayoutBottom.addStretch()
        
        #Setting the widgets of the splitter
        self.widgetLeft.setLayout(self.layoutSplitterLeft)
        self.widgetRight.setLayout(self.layoutSplitterRight)
        
        #Setting the main LAyout and all the spacing
        trees.setLayout(self.mainLayout)
        self.mainLayout.setMargin(50)
        self.horizontalLayout.setSpacing(10)       
        self.horizontalLayoutBottom.setSpacing(10)
        
        #Pyuic4 auto-generated code
        self.retranslateUi(trees)
        QtCore.QMetaObject.connectSlotsByName(trees)
       
        # My preferences
        self.connect(self.processesList, QtCore.SIGNAL("clicked(QModelIndex)"), self.updateView)
        self.connect(self.processesList,QtCore.SIGNAL("openTree()"),self.openTreeEditor)
        self.connect(self.processesList,QtCore.SIGNAL("deleteProcess()"),self.deleteRow)
        self.connect(self.add, QtCore.SIGNAL("clicked()"), self.addRow)
        self.connect(self.delete, QtCore.SIGNAL("clicked()"), self.deleteRow)
        self.connect(self.pushButton_treeEditor, QtCore.SIGNAL("clicked()"),self.openTreeEditor)
        self.connect(self.parametersToolButton,QtCore.SIGNAL("clicked()"),self.openProcess)
        
        
    def retranslateUi(self, trees):
        trees.setWindowTitle(QtGui.QApplication.translate("trees", "Population", None, QtGui.QApplication.UnicodeUTF8))
        self.loadParameters.setText(QtGui.QApplication.translate("trees", "Load predefined process :", None, QtGui.QApplication.UnicodeUTF8))
        self.parametersToolButton.setText(QtGui.QApplication.translate("trees", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.tableLabel.setText(QtGui.QApplication.translate("trees", "Processes list :", None, QtGui.QApplication.UnicodeUTF8))
        self.tableLabel_2.setText(QtGui.QApplication.translate("trees", "Process tree :", None, QtGui.QApplication.UnicodeUTF8))
        self.add.setText(QtGui.QApplication.translate("trees", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.delete.setText(QtGui.QApplication.translate("trees", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        
    def updateView(self, index):
        '''
        @summary Creates a preview of the currently selected process and display it in Scroll Area
        @param index : index of the currently selected process
        '''
        if len(self.processesList.selectedIndexes()) > 1:
            #User Is selecting multiple trees, don't update view
            return
        if (index.isValid):
            #self.SVGViewScroll.setWidgetResizable(False)
            trees = index.model().baseModel.getViewTreatmentsDict()
            tree = index.model().baseModel.getTreatmentsDict()[trees[index.row()]]
            processName = str(self.processesList.model().getTreatmentNameFromIndex(index))
            editor = MedTreeView(tree.toElement().elementsByTagName("PrimitiveTree").item(0).firstChild(),self)
            #Create new widget holding the preview
            newQLabel = QtGui.QLabel()
            newQLabel.setPixmap(QtGui.QPixmap.fromImage(editor.printPreview()))
            #newQLabel.setPixmap(editor.printPreview())
            newQLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.SVGViewScroll.setWidget(newQLabel)
            #Since creating the preview automatically checks for errors in model, get result and update error state of the process
            baseTrModel = BaseTreatmentsModel()
            baseTrModel.updateValidationState(processName, editor.primitive)
            
    def addRow(self):
        '''
        @summary Add new process
        '''
        if self.processesList.state() == QtGui.QAbstractItemView.EditingState:
            #Editing state is on, close editor so we don't raise a Qt editing failed error
            print "Closing"
            self.processesList.closePersistentEditor( self.processesList.currentIndex() )
        if self.processesList.selectedIndexes() and len(self.processesList.selectedIndexes()) == 1:
            indexToEdit = self.processesList.selectedIndexes()[0].row()
            self.processesList.model().insertRow(indexToEdit, self.processesList.rootIndex())
            self.processesList.setCurrentIndex(self.processesList.model().index(indexToEdit+1,0))
            self.processesList.edit(self.processesList.model().index(indexToEdit+1,0))
            return
        indexToEdit = self.processesList.model().rowCount()
        self.processesList.model().insertRow(indexToEdit, self.processesList.rootIndex())
        self.processesList.setCurrentIndex(self.processesList.model().index(indexToEdit,0))
        self.processesList.edit(self.processesList.model().index(indexToEdit,0))

        
    def deleteRow(self):
        '''
        @summary Delete currently selected process(es)
        '''
        if len(self.processesList.selectedIndexes()) > 1:
            self.processesList.model().specialRemove([index.row() for index in self.processesList.selectedIndexes()])
            self.processesList.clearSelection()
            return
        
        elif len(self.processesList.selectedIndexes()):
            index = self.processesList.selectedIndexes()[0]
            self.processesList.model().removeRow(index.row())
            self.processesList.clearSelection()
            
    def openTreeEditor(self):
        '''
        @summary Open tree editor
        Allow multiple open at once
        '''
        if self.processesList.selectedIndexes():
            index = self.processesList.selectedIndexes()[0]
            trees = index.model().baseModel.getViewTreatmentsDict()
            tree = index.model().baseModel.getTreatmentsDict()[trees[index.row()]]
            editor = MainEditorWindow(tree.toElement().elementsByTagName("PrimitiveTree").item(0).firstChild(),self.parent,self.processesList.model().getTreatmentNameFromIndex(index))
            editor.setWindowModality(QtCore.Qt.WindowModal)
            if len(self.processesList.selectedIndexes()) > 1:
                for indexes in self.processesList.selectedIndexes()[1:]:
                    tree = index.model().baseModel.getTreatmentsDict()[trees[indexes.row()]]
                    newTreeView = MedTreeView(tree.toElement().elementsByTagName("PrimitiveTree").item(0).firstChild(),editor)
                    editor.tabWidget_2.addTab(newTreeView,indexes.model().getTreatmentNameFromIndex(indexes))
            editor.exec_()
            if editor.result():
                self.updateView(index)
        
    def openProcess(self):
        '''
        @summary Allow a user to import a process defined in an other simulation
        '''
        processFilePath = QtGui.QFileDialog.getOpenFileName(self, self.tr("Select a simulation file from which you want to use a process"),
                                                            os.getcwd(), self.tr("LSD files (*.lsd);;All files (*);;"))
        if processFilePath.isEmpty():
            return
        if str(processFilePath).rpartition(".")[-1] != "lsd":
            QtGui.QMessageBox.warning(self,"Bad file extension","Make sure you choose a file with a .lsd extension!",QtGui.QMessageBox.Ok)
            return
        
        ZipFile = zipfile.PyZipFile(str(processFilePath),"r")

        filesList = ZipFile.namelist()
        
        processesList = list(file for file in filesList if file.find("/Processes/") != -1 and file.find(".xml") != -1)

        selectionDialog = ProcessSelection(processesList, self)
        if not selectionDialog.exec_():
            return
        
        for processFile in selectionDialog.getSelectedPaths():
            processFileName = str(processFile).rpartition("/")[2]
            tmpCopy = ZipFile.open(processFile, "r")
            
            if processFileName.rpartition(".")[0] in self.processesList.model().baseModel.getViewTreatmentsDict():
                
                # If the process already exist
                acceptChange = QtGui.QMessageBox.question(self, "About to replace process","Replace process named "+(processFileName.rpartition(".")[0])+"?")
                if not acceptChange:
                    continue
                else:   # Delete the previous process in the list
                    self.processesList.model().removeRow(self.processesList.model().baseModel.getViewTreatmentsDict().index(processFileName.rpartition(".")[0]))
                
            tmpDom = QtXml.QDomDocument()
            tmpDom.setContent(tmpCopy.read())
            tmpCopy.close()
            self.processesList.model().insertRowFromDom(self.processesList.model().rowCount()-1,tmpDom.documentElement())
        return     
        
class ProcessSelection(QtGui.QDialog):
    '''
    Dialog showing the suer the available processes contained in a compressed simulation folder
    '''
    def __init__(self, filesList, parent=None):
        '''
        @summary Constructor
        @param fileList : list of processes in the compressed folder
        @param parent : parent widget
        '''
        QtGui.QDialog.__init__(self, None)
        self.setWindowTitle("Select process(es) and then click OK")
        self.resize(520, 510)
        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(10,460, 441, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.editors = []
        self.frames = []
        self.labels = []
        self.checkbox = []

        self.scrollBox = QtGui.QScrollArea(self)
        self.scrollBox.setGeometry(QtCore.QRect(10,10,490,450))

        self.frameContainer = QtGui.QFrame(self.scrollBox)
        self.frameContainer.setGeometry(QtCore.QRect(10,10,450,len(filesList)*35+10))

        self.scrollBox.setWidget(self.frameContainer)
        for file in filesList:
            self.frames.append(QtGui.QFrame(self.frameContainer))
            self.frames[-1].setGeometry(QtCore.QRect(0, 30 * len(self.frames)-1, 471, 25))

            self.checkbox.append(QtGui.QCheckBox(self.frames[-1]))
            self.checkbox[-1].setObjectName(str(file))

            self.labels.append(QtGui.QLabel(self.frames[-1]))
            self.labels[-1].setGeometry(QtCore.QRect(40, 3, 400, 20))
            self.labels[-1].setText((str(file).rpartition("/")[2]).rpartition(".")[0])

        self.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.accept)
        self.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), self.reject)
        return

    def getSelectedPaths(self):
        '''
        @summary Find processes that have been chosen by the user
        '''
        returnList = []
        for i in range(0, len(self.frames)):
            if self.checkbox[i].checkState() == QtCore.Qt.Checked:
                returnList.append(str(self.checkbox[i].objectName()))

        return returnList
    
class ArrowsAwareTableView(QtGui.QTableView):
    '''
    This class slightly modify Qt's QTableView class
    Navigating the TableView with arrows will generate the same signal as if the user was using the mouse buttons
    This way, previews will be generated like the user had clicked in the table view.
    '''
    def __init__(self):
        '''
        @summary Constructor 
        '''
        QtGui.QTableView.__init__(self)
        
    def keyPressEvent(self,event):
        '''
        @summary Reimplementation of QTableView's keyPressEvent function
        @param event : see QTableView's documentation for more information
        '''
        super(ArrowsAwareTableView, self).keyPressEvent(event)
        if event.key() == QtCore.Qt.Key_Up or event.key() == QtCore.Qt.Key_Down:
            self.emit(QtCore.SIGNAL("clicked(QModelIndex)"),self.currentIndex())
        if event.key() == QtCore.Qt.Key_Return and not self.state() == QtGui.QAbstractItemView.EditingState:
            self.emit(QtCore.SIGNAL("openTree()"))
        if event.key() == QtCore.Qt.Key_Delete and not self.state() == QtGui.QAbstractItemView.EditingState:
            self.emit(QtCore.SIGNAL("deleteProcess()"))
            