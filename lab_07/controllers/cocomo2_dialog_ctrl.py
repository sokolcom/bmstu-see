from PyQt5.QtWidgets import QDialog
import view.cocomo2_dialog as ccd
from cocomo2 import Cocomo2
from application_composition_model import ApplicationCompositionModel
from early_architectural_design_model import EarlyArchitecturalDesignModel


class Cocomo2Dialog(QDialog):
    def __init__(self, parent, kloc):
        super(Cocomo2Dialog, self).__init__(parent)
        self.ui = ccd.Ui_Dialog()
        self.ui.setupUi(self)
        self.__build()
        self.kloc = kloc
        self.ui.comp_pushButton.clicked.connect(self.compose_run)
        self.ui.arch_pushButton.clicked.connect(self.arch_run)

    def __build(self):
        n = len(ApplicationCompositionModel.ExpFactor)
        for i in range(n):
            self.ui.exp_comboBox.addItem(ApplicationCompositionModel.ExpFactor[i].name)

        self.exp_factors = [
            self.ui.prec_comboBox,
            self.ui.flex_comboBox,
            self.ui.resl_comboBox,
            self.ui.team_comboBox,
            self.ui.pmat_comboBox
        ]

        self.early_arch_factors = [
            self.ui.rcpx_comboBox,
            self.ui.ruse_comboBox,
            self.ui.pdif_comboBox,
            self.ui.prex_comboBox,
            self.ui.pers_comboBox,
            self.ui.fcil_comboBox,
            self.ui.sceh_comboBox
        ]

        n = len(self.exp_factors)
        for i in range(n):
            m = len(Cocomo2.Factors[i].drivers)
            for j in range(m):
                text = Cocomo2.Factors[i].drivers[j].name
                self.exp_factors[i].addItem(text)

        n = len(self.early_arch_factors)
        for i in range(n):
            m = len(EarlyArchitecturalDesignModel.Factors[i].drivers)
            for j in range(m):
                text = EarlyArchitecturalDesignModel.Factors[i].drivers[j].name
                self.early_arch_factors[i].addItem(text)

    def __get_exp_idxs(self):
        exp_idxs = []
        n = len(self.exp_factors)
        for i in range(n):
            exp_idxs.append(self.exp_factors[i].currentIndex())
        return exp_idxs

    def compose_run(self):
        ruse = self.ui.ruse_spinBox.value()
        exp_idx = self.ui.exp_comboBox.currentIndex()
        screen_counts = [self.ui.screen_simple_spinBox.value(),
                         self.ui.screen_med_spinBox.value(),
                         self.ui.screen_hard_spinBox.value()]
        report_counts = [self.ui.report_simple_spinBox.value(),
                         self.ui.report_med_spinBox.value(),
                         self.ui.report_hard_spinBox.value()]
        third_gen_land = self.ui.third_gen_lang_spinBox.value()
        factors_idxs = self.__get_exp_idxs()
        p = Cocomo2.get_p(factors_idxs)
        month_cost = self.ui.man_month_cost_spinBox.value()
        labor_costs, time, avg_workers, money = ApplicationCompositionModel.process(ruse, exp_idx, screen_counts, report_counts, third_gen_land, p, month_cost)
        self.__show_comp_res(labor_costs, time, avg_workers, money)

    def __show_comp_res(self, labor_costs, time, avg_workers, money):
        self.ui.comp_work_label.setText(str(labor_costs))
        self.ui.comp_time_label.setText(str(time))
        self.ui.comp_workers_label.setText(str(avg_workers))
        self.ui.comp_money_label.setText(str(money))

    def arch_run(self):
        factors_idxs = self.__get_exp_idxs()
        print(factors_idxs)
        p = Cocomo2.get_p(factors_idxs)
        print(p)
        early_arch_factors_idxs = self.__get_early_factors_idxs()
        month_cost = self.ui.man_month_cost_spinBox.value()
        labor_costs, time, avg_workers, money = EarlyArchitecturalDesignModel.process(p, self.kloc, early_arch_factors_idxs, month_cost)
        self.__show_arch_res(labor_costs, time, avg_workers, money)

    def __show_arch_res(self, labor_costs, time, avg_workers, money):
        self.ui.early_work_label.setText(str(labor_costs))
        self.ui.early_time_label.setText(str(time))
        self.ui.early_workers_label.setText(str(avg_workers))
        self.ui.early_money_label.setText(str(money))

    def __get_early_factors_idxs(self):
        early_arch_factors_idxs = []
        n = len(self.early_arch_factors)
        for i in range(n):
            early_arch_factors_idxs.append(self.early_arch_factors[i].currentIndex())
        return early_arch_factors_idxs
