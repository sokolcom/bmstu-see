from PyQt5.QtWidgets import QMainWindow
import view.mainwindow as mwd
from function_point import FunctionPointMethod
from controllers.cocomo2_dialog_ctrl import Cocomo2Dialog
from math import floor


class Cocomo2Mainwindow(QMainWindow):
    def __init__(self):
        super(Cocomo2Mainwindow, self).__init__()
        self.ui = mwd.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.run)
        self.__build()
        self.__set_coefs()

    def run(self):
        quantity = self.__get_quantity()
        sys_params = self.__get_sys_params()
        total = FunctionPointMethod.count_function_points(quantity)
        self.__set_total(total)
        fp = total[len(total) - 1]
        corrected_fp = FunctionPointMethod.corrected_function_points(fp, sys_params)
        lang_idx = self.__get_lang_idxs()
        lang_perc = self.__get_lang_perc()
        loc = FunctionPointMethod.cfp_to_loc(corrected_fp, lang_idx, lang_perc)
        print(f"fp = {fp}, corrected fp = {corrected_fp}, loc = {loc}")

        kloc = self.__loc_to_kloc(loc)
        cocomo2_dialog = Cocomo2Dialog(self, kloc)
        cocomo2_dialog.show()

    def __get_lang_perc(self):
        lang_perc = []
        n = len(self.lang_perc_spins)
        for i in range(n):
            lang_perc.append(self.lang_perc_spins[i].value())
        return lang_perc

    def __get_lang_idxs(self):
        lang_idxs = []
        n = len(self.lang_combos)
        for i in range(n):
            lang_idxs.append(self.lang_combos[i].currentIndex())
        return lang_idxs

    def __loc_to_kloc(self, loc):
        kloc = floor(loc / 1000)
        return kloc

    def __set_total(self, total):
        n = len(self.complexity_matrix_total)
        for i in range(n):
            self.complexity_matrix_total[i].setText(str(total[i]))

    def __get_sys_params(self) -> []:
        sys_params = []
        n = len(self.sys_params_input)
        for i in range(n):
            val = self.sys_params_input[i].value()
            sys_params.append(val)
        return sys_params

    def __get_quantity(self) -> []:
        quantity = []
        n = len(self.complexity_matrix_quantity)
        m = len(self.complexity_matrix_quantity[0])
        for i in range(n):
            quantity.append([])
            for j in range(m):
                val = self.complexity_matrix_quantity[i][j].value()
                quantity[i].append(val)
        return quantity

    def __set_coefs(self):
        n = len(FunctionPointMethod.Coefficients)
        m = len(FunctionPointMethod.Coefficients[0])
        for i in range(n):
            for j in range(m):
                self.complexity_matrix_koef[i][j].setText(str(FunctionPointMethod.Coefficients[i][j]))

    def __build(self):
        self.lang_combos = [self.ui.first_lang_comboBox,
                            self.ui.second_lang_comboBox,
                            self.ui.third_lang_comboBox]

        self.lang_perc_spins = [self.ui.first_lang_perc_spinBox,
                                self.ui.second_lang_perc_spinBox,
                                self.ui.third_lang_perc_spinBox]

        n = len(FunctionPointMethod.Languages)
        m = len(self.lang_combos)
        for i in range(m):
            for j in range(n):
                self.lang_combos[i].addItem(FunctionPointMethod.Languages[j].name)

        self.complexity_matrix_quantity = [
            [self.ui.simple_ei_spinBox,
             self.ui.med_ei_spinBox,
             self.ui.hard_ei_spinBox],
            [self.ui.simple_eo_spinBox,
             self.ui.med_eo_spinBox,
             self.ui.hard_eo_spinBox],
            [self.ui.simple_eq_spinBox,
             self.ui.med_eq_spinBox,
             self.ui.hard_eq_spinBox],
            [self.ui.simple_ilf_spinBox,
             self.ui.med_ilf_spinBox,
             self.ui.hard_ilf_spinBox],
            [self.ui.simple_eif_spinBox,
             self.ui.med_eif_spinBox,
             self.ui.hard_eif_spinBox]
        ]
        self.complexity_matrix_koef = [
            [self.ui.simple_ei_label,
             self.ui.med_ei_label,
             self.ui.hard_ei_label],
            [self.ui.simple_eo_label,
             self.ui.med_eo_label,
             self.ui.hard_eo_label],
            [self.ui.simple_eq_label,
             self.ui.med_eq_label,
             self.ui.hard_eq_label],
            [self.ui.simple_ilf_label,
             self.ui.med_ilf_label,
             self.ui.hard_ilf_label],
            [self.ui.simple_eif_label,
             self.ui.med_eif_label,
             self.ui.hard_eif_label]
        ]
        self.complexity_matrix_total = [
            self.ui.total_ei_label,
            self.ui.total_eo_label,
            self.ui.total_eq_label,
            self.ui.total_ilf_label,
            self.ui.total_eif_label,
            self.ui.total_label
        ]

        self.sys_params_input = [
            self.ui.sys_1_spinBox,
            self.ui.sys_2_spinBox,
            self.ui.sys_3_spinBox,
            self.ui.sys_4_spinBox,
            self.ui.sys_5_spinBox,
            self.ui.sys_6_spinBox,
            self.ui.sys_7_spinBox,
            self.ui.sys_8_spinBox,
            self.ui.sys_9_spinBox,
            self.ui.sys_10_spinBox,
            self.ui.sys_11_spinBox,
            self.ui.sys_12_spinBox,
            self.ui.sys_13_spinBox,
            self.ui.sys_14_spinBox,
        ]

