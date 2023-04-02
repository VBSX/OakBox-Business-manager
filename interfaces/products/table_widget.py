from PySide6 import QtCore
from PySide6.QtCore import Qt

class TableWidget(QtCore.QAbstractTableModel):
    def __init__(self,data, parent = None):
        super(TableWidget, self).__init__(parent = parent)
        self._data = data
    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])
    