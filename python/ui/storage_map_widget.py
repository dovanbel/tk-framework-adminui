# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'storage_map_widget.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from sgtk.platform.qt import QtCore, QtGui

class Ui_StorageMapWidget(object):
    def setupUi(self, StorageMapWidget):
        StorageMapWidget.setObjectName("StorageMapWidget")
        StorageMapWidget.resize(456, 182)
        StorageMapWidget.setAutoFillBackground(True)
        self.gridLayout_2 = QtGui.QGridLayout(StorageMapWidget)
        self.gridLayout_2.setContentsMargins(8, 8, 8, 8)
        self.gridLayout_2.setHorizontalSpacing(12)
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.root_desc_layout = QtGui.QHBoxLayout()
        self.root_desc_layout.setSpacing(0)
        self.root_desc_layout.setObjectName("root_desc_layout")
        spacerItem = QtGui.QSpacerItem(12, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.root_desc_layout.addItem(spacerItem)
        self.stroage_root_desc_area = QtGui.QScrollArea(StorageMapWidget)
        self.stroage_root_desc_area.setFocusPolicy(QtCore.Qt.NoFocus)
        self.stroage_root_desc_area.setFrameShape(QtGui.QFrame.NoFrame)
        self.stroage_root_desc_area.setFrameShadow(QtGui.QFrame.Plain)
        self.stroage_root_desc_area.setWidgetResizable(True)
        self.stroage_root_desc_area.setObjectName("stroage_root_desc_area")
        self.storage_root_desc = QtGui.QWidget()
        self.storage_root_desc.setGeometry(QtCore.QRect(0, 0, 157, 104))
        self.storage_root_desc.setObjectName("storage_root_desc")
        self.verticalLayout = QtGui.QVBoxLayout(self.storage_root_desc)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.root_description = QtGui.QLabel(self.storage_root_desc)
        self.root_description.setStyleSheet("font-size: 10px;\n"
"color: rgb(160, 160, 160);")
        self.root_description.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.root_description.setWordWrap(True)
        self.root_description.setObjectName("root_description")
        self.verticalLayout.addWidget(self.root_description)
        self.stroage_root_desc_area.setWidget(self.storage_root_desc)
        self.root_desc_layout.addWidget(self.stroage_root_desc_area)
        self.root_desc_layout.setStretch(0, 1)
        self.gridLayout_2.addLayout(self.root_desc_layout, 1, 0, 1, 1)
        self.storage_layout = QtGui.QHBoxLayout()
        self.storage_layout.setSpacing(6)
        self.storage_layout.setObjectName("storage_layout")
        self.storage_lbl = QtGui.QLabel(StorageMapWidget)
        self.storage_lbl.setObjectName("storage_lbl")
        self.storage_layout.addWidget(self.storage_lbl)
        self.storage_select_combo = QtGui.QComboBox(StorageMapWidget)
        self.storage_select_combo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.storage_select_combo.setAutoFillBackground(True)
        self.storage_select_combo.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.storage_select_combo.setObjectName("storage_select_combo")
        self.storage_layout.addWidget(self.storage_select_combo)
        self.save_storage_btn = QtGui.QToolButton(StorageMapWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.save_storage_btn.setFont(font)
        self.save_storage_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.save_storage_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.save_storage_btn.setObjectName("save_storage_btn")
        self.storage_layout.addWidget(self.save_storage_btn)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.storage_layout.addItem(spacerItem1)
        self.storage_layout.setStretch(0, 1)
        self.storage_layout.setStretch(1, 1)
        self.storage_layout.setStretch(2, 1)
        self.storage_layout.setStretch(3, 100)
        self.gridLayout_2.addLayout(self.storage_layout, 0, 1, 1, 1)
        self.paths_layout = QtGui.QHBoxLayout()
        self.paths_layout.setSpacing(0)
        self.paths_layout.setObjectName("paths_layout")
        self.path_frame = QtGui.QFrame(StorageMapWidget)
        self.path_frame.setObjectName("path_frame")
        self.gridLayout_3 = QtGui.QGridLayout(self.path_frame)
        self.gridLayout_3.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_3.setSpacing(4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.windows_path_lbl = QtGui.QLabel(self.path_frame)
        self.windows_path_lbl.setStyleSheet("font-size: 10px;\n"
"color: rgb(120, 120, 120);")
        self.windows_path_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.windows_path_lbl.setObjectName("windows_path_lbl")
        self.gridLayout_3.addWidget(self.windows_path_lbl, 2, 0, 1, 1)
        self.windows_path_layout = QtGui.QHBoxLayout()
        self.windows_path_layout.setSpacing(4)
        self.windows_path_layout.setObjectName("windows_path_layout")
        self.windows_path = QtGui.QLineEdit(self.path_frame)
        self.windows_path.setEnabled(False)
        self.windows_path.setFocusPolicy(QtCore.Qt.NoFocus)
        self.windows_path.setObjectName("windows_path")
        self.windows_path_layout.addWidget(self.windows_path)
        self.windows_path_edit = QtGui.QLineEdit(self.path_frame)
        self.windows_path_edit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.windows_path_edit.setObjectName("windows_path_edit")
        self.windows_path_layout.addWidget(self.windows_path_edit)
        self.windows_path_layout.setStretch(0, 1)
        self.windows_path_layout.setStretch(1, 1)
        self.gridLayout_3.addLayout(self.windows_path_layout, 2, 1, 1, 1)
        self.linux_path_layout = QtGui.QHBoxLayout()
        self.linux_path_layout.setSpacing(4)
        self.linux_path_layout.setObjectName("linux_path_layout")
        self.linux_path = QtGui.QLineEdit(self.path_frame)
        self.linux_path.setEnabled(False)
        self.linux_path.setFocusPolicy(QtCore.Qt.NoFocus)
        self.linux_path.setObjectName("linux_path")
        self.linux_path_layout.addWidget(self.linux_path)
        self.linux_path_edit = QtGui.QLineEdit(self.path_frame)
        self.linux_path_edit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.linux_path_edit.setObjectName("linux_path_edit")
        self.linux_path_layout.addWidget(self.linux_path_edit)
        self.linux_path_layout.setStretch(0, 1)
        self.linux_path_layout.setStretch(1, 1)
        self.gridLayout_3.addLayout(self.linux_path_layout, 0, 1, 1, 1)
        self.linux_path_lbl = QtGui.QLabel(self.path_frame)
        self.linux_path_lbl.setStyleSheet("font-size: 10px;\n"
"color: rgb(120, 120, 120);")
        self.linux_path_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.linux_path_lbl.setObjectName("linux_path_lbl")
        self.gridLayout_3.addWidget(self.linux_path_lbl, 0, 0, 1, 1)
        self.mac_path_lbl = QtGui.QLabel(self.path_frame)
        self.mac_path_lbl.setStyleSheet("font-size: 10px;\n"
"color: rgb(120, 120, 120);")
        self.mac_path_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.mac_path_lbl.setObjectName("mac_path_lbl")
        self.gridLayout_3.addWidget(self.mac_path_lbl, 1, 0, 1, 1)
        self.mac_path_layout = QtGui.QHBoxLayout()
        self.mac_path_layout.setSpacing(4)
        self.mac_path_layout.setObjectName("mac_path_layout")
        self.mac_path = QtGui.QLineEdit(self.path_frame)
        self.mac_path.setEnabled(False)
        self.mac_path.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mac_path.setObjectName("mac_path")
        self.mac_path_layout.addWidget(self.mac_path)
        self.mac_path_edit = QtGui.QLineEdit(self.path_frame)
        self.mac_path_edit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.mac_path_edit.setObjectName("mac_path_edit")
        self.mac_path_layout.addWidget(self.mac_path_edit)
        self.mac_path_layout.setStretch(0, 1)
        self.mac_path_layout.setStretch(1, 1)
        self.gridLayout_3.addLayout(self.mac_path_layout, 1, 1, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.linux_path_browse = QtGui.QToolButton(self.path_frame)
        self.linux_path_browse.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/tk-framework-adminui/setup_project/file_browse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.linux_path_browse.setIcon(icon)
        self.linux_path_browse.setObjectName("linux_path_browse")
        self.horizontalLayout_3.addWidget(self.linux_path_browse)
        self.linux_lock = QtGui.QLabel(self.path_frame)
        self.linux_lock.setMinimumSize(QtCore.QSize(8, 11))
        self.linux_lock.setMaximumSize(QtCore.QSize(8, 11))
        self.linux_lock.setText("")
        self.linux_lock.setPixmap(QtGui.QPixmap(":/tk-framework-adminui/setup_project/icon_lock.png"))
        self.linux_lock.setScaledContents(True)
        self.linux_lock.setObjectName("linux_lock")
        self.horizontalLayout_3.addWidget(self.linux_lock)
        spacerItem3 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 2, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.mac_path_browse = QtGui.QToolButton(self.path_frame)
        self.mac_path_browse.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mac_path_browse.setIcon(icon)
        self.mac_path_browse.setObjectName("mac_path_browse")
        self.horizontalLayout_4.addWidget(self.mac_path_browse)
        self.mac_lock = QtGui.QLabel(self.path_frame)
        self.mac_lock.setMinimumSize(QtCore.QSize(8, 11))
        self.mac_lock.setMaximumSize(QtCore.QSize(8, 11))
        self.mac_lock.setText("")
        self.mac_lock.setPixmap(QtGui.QPixmap(":/tk-framework-adminui/setup_project/icon_lock.png"))
        self.mac_lock.setScaledContents(True)
        self.mac_lock.setObjectName("mac_lock")
        self.horizontalLayout_4.addWidget(self.mac_lock)
        spacerItem5 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 1, 2, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem6 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.windows_path_browse = QtGui.QToolButton(self.path_frame)
        self.windows_path_browse.setFocusPolicy(QtCore.Qt.NoFocus)
        self.windows_path_browse.setIcon(icon)
        self.windows_path_browse.setObjectName("windows_path_browse")
        self.horizontalLayout_5.addWidget(self.windows_path_browse)
        self.windows_lock = QtGui.QLabel(self.path_frame)
        self.windows_lock.setMinimumSize(QtCore.QSize(8, 11))
        self.windows_lock.setMaximumSize(QtCore.QSize(8, 11))
        self.windows_lock.setText("")
        self.windows_lock.setPixmap(QtGui.QPixmap(":/tk-framework-adminui/setup_project/icon_lock.png"))
        self.windows_lock.setScaledContents(True)
        self.windows_lock.setObjectName("windows_lock")
        self.horizontalLayout_5.addWidget(self.windows_lock)
        spacerItem7 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 2, 2, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 100)
        self.gridLayout_3.setColumnStretch(2, 1)
        self.paths_layout.addWidget(self.path_frame)
        self.gridLayout_2.addLayout(self.paths_layout, 1, 1, 1, 1)
        self.root_name_layout = QtGui.QHBoxLayout()
        self.root_name_layout.setSpacing(4)
        self.root_name_layout.setObjectName("root_name_layout")
        self.root_name = QtGui.QLabel(StorageMapWidget)
        self.root_name.setObjectName("root_name")
        self.root_name_layout.addWidget(self.root_name)
        spacerItem8 = QtGui.QSpacerItem(40, 4, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.root_name_layout.addItem(spacerItem8)
        self.root_name_layout.setStretch(0, 1)
        self.root_name_layout.setStretch(1, 10)
        self.gridLayout_2.addLayout(self.root_name_layout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.count_lbl = QtGui.QLabel(StorageMapWidget)
        self.count_lbl.setStyleSheet("font-size: 10px;\n"
"color: rgb(120, 120, 120);")
        self.count_lbl.setText("")
        self.count_lbl.setObjectName("count_lbl")
        self.horizontalLayout_2.addWidget(self.count_lbl)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.storage_info = QtGui.QLabel(StorageMapWidget)
        self.storage_info.setStyleSheet("font-size: 10px;\n"
"color: rgb(252, 98, 70);")
        self.storage_info.setText("")
        self.storage_info.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.storage_info.setWordWrap(True)
        self.storage_info.setObjectName("storage_info")
        self.horizontalLayout_2.addWidget(self.storage_info)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 10)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)
        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(1, 3)
        self.gridLayout_2.setRowStretch(0, 1)

        self.retranslateUi(StorageMapWidget)
        QtCore.QMetaObject.connectSlotsByName(StorageMapWidget)

    def retranslateUi(self, StorageMapWidget):
        StorageMapWidget.setWindowTitle(QtGui.QApplication.translate("StorageMapWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.root_description.setText(QtGui.QApplication.translate("StorageMapWidget", "This is a description of the root as defined in the roots.yml file. This can be short or long.", None, QtGui.QApplication.UnicodeUTF8))
        self.storage_lbl.setToolTip(QtGui.QApplication.translate("StorageMapWidget", "<p>These are the storage paths defined by your Shotgun site.</p>", None, QtGui.QApplication.UnicodeUTF8))
        self.storage_lbl.setText(QtGui.QApplication.translate("StorageMapWidget", "Storage:", None, QtGui.QApplication.UnicodeUTF8))
        self.storage_select_combo.setToolTip(QtGui.QApplication.translate("StorageMapWidget", "<p>These are the storage paths defined by your Shotgun site.</p>", None, QtGui.QApplication.UnicodeUTF8))
        self.save_storage_btn.setToolTip(QtGui.QApplication.translate("StorageMapWidget", "<p>Click this to save your changes to the selected Storage paths.</p>", None, QtGui.QApplication.UnicodeUTF8))
        self.save_storage_btn.setText(QtGui.QApplication.translate("StorageMapWidget", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.windows_path_lbl.setText(QtGui.QApplication.translate("StorageMapWidget", "Windows:", None, QtGui.QApplication.UnicodeUTF8))
        self.windows_path_edit.setToolTip(QtGui.QApplication.translate("StorageMapWidget", "<p>Edit the storage path for this operating system.</p>", None, QtGui.QApplication.UnicodeUTF8))
        self.linux_path_edit.setToolTip(QtGui.QApplication.translate("StorageMapWidget", "<p>Edit the storage path for this operating system.</p>", None, QtGui.QApplication.UnicodeUTF8))
        self.linux_path_lbl.setText(QtGui.QApplication.translate("StorageMapWidget", "Linux:", None, QtGui.QApplication.UnicodeUTF8))
        self.mac_path_lbl.setText(QtGui.QApplication.translate("StorageMapWidget", "Mac:", None, QtGui.QApplication.UnicodeUTF8))
        self.mac_path_edit.setToolTip(QtGui.QApplication.translate("StorageMapWidget", "<p>Edit the storage path for this operating system.</p>", None, QtGui.QApplication.UnicodeUTF8))
        self.linux_path_browse.setToolTip(QtGui.QApplication.translate("StorageMapWidget", "<p>Browse a path on the current operating system.</p>", None, QtGui.QApplication.UnicodeUTF8))
        self.linux_path_browse.setText(QtGui.QApplication.translate("StorageMapWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.linux_lock.setToolTip(QtGui.QApplication.translate("StorageMapWidget", "<p>This path is locked since it has been saved to Shotgun. Visit Site Preferences > File Management to modify this path. WARNING: changing this path could break existing projects.</p>", None, QtGui.QApplication.UnicodeUTF8))
        self.mac_path_browse.setToolTip(QtGui.QApplication.translate("StorageMapWidget", "<p>Browse a path on the current operating system.</p>", None, QtGui.QApplication.UnicodeUTF8))
        self.mac_path_browse.setText(QtGui.QApplication.translate("StorageMapWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.mac_lock.setToolTip(QtGui.QApplication.translate("StorageMapWidget", "<p>This path is locked since it has been saved to Shotgun. Visit Site Preferences > File Management to modify this path. WARNING: changing this path could break existing projects.</p>", None, QtGui.QApplication.UnicodeUTF8))
        self.windows_path_browse.setToolTip(QtGui.QApplication.translate("StorageMapWidget", "<p>Browse a path on the current operating system.</p>", None, QtGui.QApplication.UnicodeUTF8))
        self.windows_path_browse.setText(QtGui.QApplication.translate("StorageMapWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.windows_lock.setToolTip(QtGui.QApplication.translate("StorageMapWidget", "<p>This path is locked since it has been saved to Shotgun. Visit Site Preferences > File Management to modify this path. WARNING: changing this path could break existing projects.</p>", None, QtGui.QApplication.UnicodeUTF8))
        self.root_name.setToolTip(QtGui.QApplication.translate("StorageMapWidget", "<p>This is the storage root name as required by the selected configuration.</p>", None, QtGui.QApplication.UnicodeUTF8))
        self.root_name.setText(QtGui.QApplication.translate("StorageMapWidget", "root_name", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
