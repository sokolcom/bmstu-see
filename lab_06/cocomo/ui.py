from matplotlib import pyplot as plt

from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QLineEdit, QComboBox, QHeaderView, QTableWidgetItem

from .config import PARAMETERS, PROJECT_MODES
from .math import PM, TM, EAF


class MainWindow(QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = uic.loadUi('cocomo/layout/window.ui', self)

        self.RELY: QComboBox = self.ui.comboBox_1
        self.DATA: QComboBox = self.ui.comboBox_2
        self.CPLX: QComboBox = self.ui.comboBox_3
        self.TIME: QComboBox = self.ui.comboBox_4
        self.STOR: QComboBox = self.ui.comboBox_5
        self.VIRT: QComboBox = self.ui.comboBox_6
        self.TURN: QComboBox = self.ui.comboBox_7
        self.ACAP: QComboBox = self.ui.comboBox_8
        self.AEXP: QComboBox = self.ui.comboBox_9
        self.PCAP: QComboBox = self.ui.comboBox_10
        self.VEXP: QComboBox = self.ui.comboBox_11
        self.LEXP: QComboBox = self.ui.comboBox_12
        self.MODP: QComboBox = self.ui.comboBox_13
        self.TOOL: QComboBox = self.ui.comboBox_14
        self.SCED: QComboBox = self.ui.comboBox_15

        self.SIZE: QLineEdit = self.ui.sizeEdit

        self.COST: QLineEdit = self.ui.costEdit

        self.project_mode: QComboBox = self.ui.comboBox_16

        self.ui.wbsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.classicTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def EAF(self):
        RELY = PARAMETERS['RELY'][self.RELY.currentIndex()]
        DATA = PARAMETERS['DATA'][self.DATA.currentIndex()]
        CPLX = PARAMETERS['CPLX'][self.CPLX.currentIndex()]
        TIME = PARAMETERS['TIME'][self.TIME.currentIndex()]
        STOR = PARAMETERS['STOR'][self.STOR.currentIndex()]
        VIRT = PARAMETERS['VIRT'][self.VIRT.currentIndex()]
        TURN = PARAMETERS['TURN'][self.TURN.currentIndex()]
        ACAP = PARAMETERS['ACAP'][self.ACAP.currentIndex()]
        AEXP = PARAMETERS['AEXP'][self.AEXP.currentIndex()]
        PCAP = PARAMETERS['PCAP'][self.PCAP.currentIndex()]
        VEXP = PARAMETERS['VEXP'][self.VEXP.currentIndex()]
        LEXP = PARAMETERS['LEXP'][self.LEXP.currentIndex()]
        MODP = PARAMETERS['MODP'][self.MODP.currentIndex()]
        TOOL = PARAMETERS['TOOL'][self.TOOL.currentIndex()]
        SCED = PARAMETERS['SCED'][self.SCED.currentIndex()]
        print(RELY * DATA * CPLX * TIME * STOR * VIRT * TURN * ACAP * AEXP * PCAP * VEXP * LEXP * MODP * TOOL * SCED)
        return RELY * DATA * CPLX * TIME * STOR * VIRT * TURN * ACAP * AEXP * PCAP * VEXP * LEXP * MODP * TOOL * SCED

    def PM(self):
        mode = self.project_mode.currentIndex()
        size = float(self.SIZE.text())
        print(PROJECT_MODES['c1'][mode], self.EAF(), size, size ** PROJECT_MODES['p1'][mode], PROJECT_MODES['c1'][mode] * self.EAF() * (size ** PROJECT_MODES['p1'][mode]))
        return PROJECT_MODES['c1'][mode] * self.EAF() * (size ** PROJECT_MODES['p1'][mode])

    def TM(self):
        mode = self.project_mode.currentIndex()
        return PROJECT_MODES['c2'][mode] * (self.PM() ** PROJECT_MODES['p2'][mode])

    @pyqtSlot(name="on_calculateButton_clicked")
    def calculate_project(self):
        pm_clean = round(self.PM(), 2)
        tm_clean = round(self.TM(), 2)
        pm = round(pm_clean * 1.08, 2)
        tm = round(tm_clean * 1.36, 2)

        self.ui.pmLabel.setText(f'Трудоемкость (PM): {pm_clean}')
        self.ui.tmLabel.setText(f'Время разработки (TM): {tm_clean}')
        print(f"PM: {pm_clean}, TM: {tm_clean}")

        for i in range(8):
            self.ui.wbsTable.setItem(i, 1, QTableWidgetItem(
                str(round(pm * int(self.ui.wbsTable.item(i, 0).text()) / 100.0, 2))))
        self.ui.wbsTable.setItem(8, 1, QTableWidgetItem(str(pm)))

        self.ui.classicTable.setItem(0, 0, QTableWidgetItem(str(round(pm_clean * 0.08, 2))))
        self.ui.classicTable.setItem(1, 0, QTableWidgetItem(str(round(pm_clean * 0.18, 2))))
        self.ui.classicTable.setItem(2, 0, QTableWidgetItem(str(round(pm_clean * 0.25, 2))))
        self.ui.classicTable.setItem(3, 0, QTableWidgetItem(str(round(pm_clean * 0.26, 2))))
        self.ui.classicTable.setItem(4, 0, QTableWidgetItem(str(round(pm_clean * 0.31, 2))))
        self.ui.classicTable.setItem(5, 0, QTableWidgetItem(str(round(pm_clean, 2))))
        self.ui.classicTable.setItem(6, 0, QTableWidgetItem(str(round(pm, 2))))
        self.ui.classicTable.setItem(0, 1, QTableWidgetItem(str(round(tm_clean * 0.36, 2))))
        self.ui.classicTable.setItem(1, 1, QTableWidgetItem(str(round(tm_clean * 0.36, 2))))
        self.ui.classicTable.setItem(2, 1, QTableWidgetItem(str(round(tm_clean * 0.18, 2))))
        self.ui.classicTable.setItem(3, 1, QTableWidgetItem(str(round(tm_clean * 0.18, 2))))
        self.ui.classicTable.setItem(4, 1, QTableWidgetItem(str(round(tm_clean * 0.28, 2))))
        self.ui.classicTable.setItem(5, 1, QTableWidgetItem(str(round(tm_clean, 2))))
        self.ui.classicTable.setItem(6, 1, QTableWidgetItem(str(round(tm, 2))))

        y = []
        for i in range(5):
            t = round(float(self.ui.classicTable.item(i, 1).text()))
            for j in range(t):
                y.append(round(round(float(self.ui.classicTable.item(i, 0).text())) / t))

        x = [i + 1 for i in range(len(y))]

        workers_sum = 0

        plt.bar(x, y)
        for xi in x:
            plt.annotate(str(y[xi - 1]), (xi, y[xi - 1]), ha='center')
            workers_sum += y[xi - 1]
        plt.xlabel("Месяц")
        plt.ylabel("Количество сотрудников")
        plt.show()
        workers_avg = workers_sum // len(x)

        budget = round(float(self.COST.text()) * tm * workers_avg, 2)
        self.ui.costLabel.setText(f'Приблизительный бюджет: {budget}')

    @pyqtSlot(name="on_graphsButton_clicked")
    def create_graphs(self):
        def draw_figure(sced):
            sced_type = { 0: "Очень низкий" , 2: "Номинальный" , 4: "Очень высокий"}
            model_type = { 0: "Обычный" , 1: "Промежуточный" , 2: "Встроенный"}

            fig, ax = plt.subplots(3, 2)
            fig.set_figwidth(12)
            fig.set_figheight(10)
            fig.suptitle(f'PM (трудоемкость) и TM (время разработки проекта)\nдля базового уровня модели COCOMO\nSCED={sced_type[sced]}')

            for t in range(3):  #  Types of model
                y_modp_pm = []
                y_tool_pm = []
                y_modp_tm = []
                y_tool_tm = []

                x = [1, 2, 3, 4, 5]
                for i in range(5):
                    y_modp_pm.append(
                        PM(
                            PROJECT_MODES['c1'][t], PROJECT_MODES['p1'][t],
                            EAF([
                                PARAMETERS['MODP'][i], PARAMETERS['SCED'][sced], 
                            ]),
                            100
                        )
                    )
                    y_modp_tm.append(
                        TM(
                            PROJECT_MODES['c2'][t], PROJECT_MODES['p2'][t], y_modp_pm[-1]
                        )
                    )

                    y_tool_pm.append(
                        PM(
                            PROJECT_MODES['c1'][t], PROJECT_MODES['p1'][t],
                            EAF([
                                PARAMETERS['TOOL'][i], PARAMETERS['SCED'][sced]]
                            ),
                            100
                        )
                    )
                    y_tool_tm.append(
                        TM(
                            PROJECT_MODES['c2'][t], PROJECT_MODES['p2'][t], y_tool_pm[-1]
                        )
                    )
                
                ax[t, 0].set_title(f"Тип модели: {model_type[t]} вариант")
                ax[t, 0].set_xlabel('Уровень драйвера затрат')
                ax[t, 0].set_ylabel('Человеко-месяцы')
                ax[t, 0].plot(x, y_modp_pm, 'g', label='MODP')
                ax[t, 0].plot(x, y_tool_pm, 'b', label='TOOL')
                ax[t, 0].legend()

                ax[t, 1] = plt.subplot2grid((3, 2), (t, 1), colspan=2)
                ax[t, 1].set_title(f"Тип модели: {model_type[t]} вариант")
                ax[t, 1].set_xlabel('Уровень драйвера затрат')
                ax[t, 1].set_ylabel('Месяцы')
                ax[t, 1].plot(x, y_modp_tm, 'g', label='MODP')
                ax[t, 1].plot(x, y_tool_tm, 'b', label='TOOL')
                ax[t, 1].legend()

            plt.subplots_adjust(
                left=0.1,
                bottom=0.1, 
                right=0.9, 
                top=0.9, 
                wspace=0.4, 
                hspace=0.4
            )
            fig.show()
        
        for sced in [0, 2, 4]:  # SCED lvl
            draw_figure(sced)


                # plt.suptitle(f'PM (трудоемкость) и TM (время разработки проекта)\nдля базового уровня модели COCOMO')
                # plt.subplot(1, 2, 1)
                # line1, = plt.plot(x, y_modp_pm, 'g', label='MODP')
                # line2, = plt.plot(x, y_tool_pm, 'b', label='TOOL')
                # plt.legend(handles=[line1, line2])

                # plt.subplot(1, 2, 2)
                # # plt.plot(x, y_modp_tm, 'r', x, y_tool_tm, 'g')
                # line1, = plt.plot(x, y_modp_tm, 'g', label='MODP')
                # line2, = plt.plot(x, y_tool_tm, 'b', label='TOOL')
                # plt.legend(handles=[line1, line2])
                # plt.show()


        # for sced in [0, 2, 4]:  # SCED lvl
        #     for t in range(3):  #  Types of model
        #         y_modp_pm = []
        #         y_tool_pm = []
        #         y_modp_tm = []
        #         y_tool_tm = []

        #         x = [1, 2, 3, 4, 5]
        #         for i in range(5):
        #             y_modp_pm.append(
        #                 PM(
        #                     PROJECT_MODES['c1'][t], PROJECT_MODES['p1'][t],
        #                     EAF([
        #                         PARAMETERS['MODP'][i], PARAMETERS['SCED'][sced], 
        #                     ]),
        #                     100
        #                 )
        #             )
        #             y_modp_tm.append(
        #                 TM(
        #                     PROJECT_MODES['c2'][t], PROJECT_MODES['p2'][t], y_modp_pm[-1]
        #                 )
        #             )

        #             y_tool_pm.append(
        #                 PM(
        #                     PROJECT_MODES['c1'][t], PROJECT_MODES['p1'][t],
        #                     EAF([
        #                         PARAMETERS['TOOL'][i], PARAMETERS['SCED'][sced]]
        #                     ),
        #                     100
        #                 )
        #             )
        #             y_tool_tm.append(
        #                 TM(
        #                     PROJECT_MODES['c2'][t], PROJECT_MODES['p2'][t], y_tool_pm[-1]
        #                 )
        #             )

        #         plt.suptitle(f'PM (трудоемкость) и TM (время разработки проекта)\nдля базового уровня модели COCOMO')
        #         plt.subplot(1, 2, 1)
        #         line1, = plt.plot(x, y_modp_pm, 'g', label='MODP')
        #         line2, = plt.plot(x, y_tool_pm, 'b', label='TOOL')
        #         plt.legend(handles=[line1, line2])

        #         plt.subplot(1, 2, 2)
        #         # plt.plot(x, y_modp_tm, 'r', x, y_tool_tm, 'g')
        #         line1, = plt.plot(x, y_modp_tm, 'g', label='MODP')
        #         line2, = plt.plot(x, y_tool_tm, 'b', label='TOOL')
        #         plt.legend(handles=[line1, line2])
        #         plt.show()
