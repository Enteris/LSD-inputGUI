'''
Created on 2010-04-16

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


from PyQt4 import QtCore
from PyQt4.QtGui import QColor

class GeneratorManagerModel(QtCore.QAbstractTableModel):
    '''
    Model handling population generation representation
    '''

    def __init__(self, baseModel, parent=None, mainWindow=None):
        '''
        @summary Constructor
        @param baseModel : base model contains the data
        @param parent : model's view
        '''
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.baseModel = baseModel
        self.topWObject = mainWindow
        
    def getBaseModel(self):
        '''
        @summary Return base model
        '''
        return self.baseModel
    
    def columnCount(self, parent=QtCore.QModelIndex()):
        '''' 
        @summary : Reimplemented from QAbstractTableModel.columnCount(self,parent)
        Column count is fixed to 3(profile,size and time)
        @param parent : not used
        '''
        return 3
    
    def rowCount(self, parent=QtCore.QModelIndex()):
        ''' 
        @summary : Reimplemented from QAbstractTableModel.rowCount(self,parent)
        How many variables do we have
        @param parent : not used
        '''
        return self.baseModel.howManyGeneration()
    
    def data(self, index, role=QtCore.Qt.DisplayRole):
        ''' 
        @summary : Reimplemented from QAbstractTableModel.data(self, index, role=QtCore.Qt.DisplayRole)
        Return data for role at position index in model. Controls what is going to be displayed in the table view.
        @param index : cell's index in model/table
        @param role : Qt item role
        '''
        if not index.isValid():
            return QtCore.QVariant()
        
        colonne = index.column()
        varNode = self.baseModel.getSourceNode().childNodes().item(index.row())
        
        if role == QtCore.Qt.TextColorRole:
            
            return QtCore.QVariant(QColor(0,0, 0))
                
        elif role == QtCore.Qt.CheckStateRole:
            return QtCore.QVariant()                #Discard unwanted checkboxes
        
        elif role == QtCore.Qt.ToolTipRole:
            return QtCore.QVariant()
        
        elif role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
       
        if colonne == 0:
            # Profile Name
            return QtCore.QVariant(varNode.toElement().attribute("profile"))
        elif colonne == 1:
            #Number of individuals to generate
            return QtCore.QVariant(varNode.toElement().attribute("size"))
        elif colonne == 2:
            #Time of generation
            return QtCore.QVariant(varNode.toElement().attribute("time"))

        return QtCore.QVariant(QtCore.QString(""))

    def headerData(self, section, orientation, role):
        ''' 
        @summary : Reimplemented from QAbstractTableModel.headerData(self, section, orientation, role)
        See QAbstractTableModel's documentation for mode details
        @param section : model's column or row
        @param orientation : horizontal or vertical
        @param role : Qt item role
        '''
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        
        if orientation == QtCore.Qt.Horizontal:
           
            if section == 0:
                return QtCore.QVariant("Profile name")
            elif section == 1:
                return QtCore.QVariant("Individuals quantity")
            elif section == 2:
                return QtCore.QVariant("Clock value")
            else:
                return QtCore.QVariant()
        else:
            return QtCore.QVariant(section + 1)  
        
        return QtCore.QVariant()
    
    def flags(self, index):
        ''' 
        @summary : Reimplemented from QAbstractTableModel.flags(self,index)
        See QAbstractTableModel's documentation for mode details
        @param index : cell's index in model/table
        '''
        if not index.isValid():
            return QtCore.Qt.ItemIsEnabled

        return QtCore.Qt.ItemFlags(QtCore.QAbstractTableModel.flags(self, index) | QtCore.Qt.ItemIsEditable)

    def insertRow(self, rowafter, parent=QtCore.QModelIndex()):
        ''' 
        @summary : Reimplemented from QAbstractTableModel.insertRow(self, row, parent=QtCore.QModelIndex())
        See QAbstractTableModel's documentation for mode details
        Inserts a row in the model/table
        @param rowafter : insert row in model/table
        @param parent : parent's index(not really relevant for table views)
        '''
        self.beginInsertRows(parent, rowafter, rowafter)
        newGenNode = self.baseModel.getSourceNode().ownerDocument().createElement("SubPopulation")
        newGenNode.setAttribute("profile","")
        newGenNode.setAttribute("time","0")
        newGenNode.setAttribute("size","0")
        self.baseModel.getSourceNode().appendChild(newGenNode)
        self.endInsertRows()
        self.topWObject.dirty = True
        return
    
    def removeRow(self, row, parent = QtCore.QModelIndex()):
        ''' 
        @summary : Reimplemented from QAbstractTableModel.removeRow(self, row, parent = QtCore.QModelIndex())
        See QAbstractTableModel's documentation for mode details
        Removes a row from the model/table
        @param index : cell's position in model/table
        @param rowToDelete : row of the deleted index
        '''
        self.beginRemoveRows(parent, row, row)
        self.baseModel.getSourceNode().removeChild(self.baseModel.getSourceNode().childNodes().item(row))
        self.endRemoveRows()
        self.topWObject.dirty = True
        return
    
    def specialRemove(self,indexes):
        ''' 
        @summary : Remove function to delete multiple(possibly non-contiguous) elements in list
        Remove rows from the model/table with rows of deleted indexes
        @param rows : rows of  the deleted indexes
        '''
        profilesNode = self.baseModel.getSourceNode().childNodes()
        profileToDelete = [profilesNode.item(index) for index in indexes]
        for deletedProfile in profileToDelete:
            for i in range(0,self.baseModel.getSourceNode().childNodes().count()):
                if deletedProfile == self.baseModel.getSourceNode().childNodes().item(i):
                    break
            self.beginRemoveRows(QtCore.QModelIndex(),i,i)
            self.baseModel.getSourceNode().removeChild(deletedProfile)
            self.endRemoveRows()
        
        self.topWObject.dirty = True

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        ''' 
        @summary : Reimplemented from QAbstractTableModel.setData(self, index, value, role=QtCore.Qt.EditRole)
        Sets data for role at position index in model. Modify model and its underlying data structure
        @param index : cell's position in model/table
        @param value : new Value
        @param role : Qt item role
        '''
        if index.isValid() and role == QtCore.Qt.EditRole:
            column = index.column()
            varNode = self.baseModel.getSourceNode().childNodes().item(index.row())
            if column == 0:
                varNode.toElement().setAttribute("profile",value.toString())
                self.topWObject.dirty = True
                return True
            value, success = value.toLongLong()
            if success:
                if column == 1:
                    varNode.toElement().setAttribute("size",str(value))
                    self.topWObject.dirty = True
                    return True
                elif column == 2:
                    varNode.toElement().setAttribute("time",str(value))
                    self.topWObject.dirty = True
                    return True
        
        print("Warning : In ProfileManagerModel::setData, value cannot be casted to long!")
        return False
