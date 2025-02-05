#!/usr/bin/env python3

# Copyright 2023 TIER IV, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from PyQt5 import QtCore
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QWidget


class TimeManagerWidget(QMainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.setObjectName("PerceptionReplayer")
        self.resize(480, 120)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.central_widget = QWidget(self)
        self.central_widget.setObjectName("central_widget")

        self.grid_layout = QGridLayout(self.central_widget)
        self.grid_layout.setContentsMargins(10, 10, 10, 10)
        self.grid_layout.setObjectName("grid_layout")

        self.rate_button = []
        for i, rate in enumerate([0.1, 0.5, 1.0, 2.0, 5.0, 10.0]):
            button = QPushButton(str(rate))
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.rate_button.append(button)
            self.grid_layout.addWidget(self.rate_button[-1], 0, i, 1, 1)

        self.button = QPushButton("pause")
        self.button.setCheckable(True)
        self.button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.grid_layout.addWidget(self.button, 1, 0, 1, -1)
        self.setCentralWidget(self.central_widget)
