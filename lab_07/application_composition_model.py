from cocomo2 import Driver


class ApplicationCompositionModel:
    ExpFactor = [
        Driver("Очень низкая", 4),
        Driver("Низкая", 7),
        Driver("Номинальная", 13),
        Driver("Высокая", 25),
        Driver("Очень высокая", 50),
    ]
    ScreenFormsMultiplier = [1, 2, 3]
    ReportMultiplier = [2, 5, 8]
    ThirdGenLangMultiplier = 10

    @staticmethod
    def process(ruse: int, exp_idx: int, screen_counts: (), report_counts: (), third_gen_land: int, p: float,
                man_month_cost: float):
        op = ApplicationCompositionModel.__get_op(screen_counts, report_counts, third_gen_land)
        nop = ApplicationCompositionModel.__get_nop(op, ruse)
        prod = ApplicationCompositionModel.ExpFactor[exp_idx].value
        labor_costs = ApplicationCompositionModel.__get_labor_costs(nop, prod)
        time = ApplicationCompositionModel.__get_time(p, labor_costs)
        avg_workers = ApplicationCompositionModel.__get_avg_workers(time, labor_costs)
        money = ApplicationCompositionModel.__get_money(time, man_month_cost)
        print(f"Application composition model: labor = {labor_costs}, time = {time}, avg workers = {avg_workers}, money = {money}")
        return labor_costs, time, avg_workers, money

    @staticmethod
    def __get_money(time, month_cost):
        money = time * month_cost
        money = round(money, 3)
        return money

    @staticmethod
    def __get_avg_workers(time, work):
        if time == 0:
            return float("inf")
        avg_workers = work / time
        avg_workers = round(avg_workers)
        return avg_workers

    @staticmethod
    def __get_time(p: float, labor: float):
        degree = 0.33 + 0.2 * (p - 1.01)
        time = 3 * pow(labor, degree)
        time = round(time, 3)
        return time

    @staticmethod
    def __get_labor_costs(nop, prod):
        val = nop / prod
        val = round(val, 3)
        return val

    @staticmethod
    def __get_op(screen_counts, report_counts, third_gen_land):
        op = 0
        n = len(screen_counts)
        for i in range(n):
            op += ApplicationCompositionModel.ScreenFormsMultiplier[i] * screen_counts[i]
            op += ApplicationCompositionModel.ReportMultiplier[i] * report_counts[i]
        op += third_gen_land * ApplicationCompositionModel.ThirdGenLangMultiplier
        return op

    @staticmethod
    def __get_nop(op, ruse):
        nop = op * ((100 - ruse) / 100)
        return nop
