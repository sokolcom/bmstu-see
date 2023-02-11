from cocomo2 import Driver


class RUSE:
    descr = "Сложность продукта"
    drivers = [
        Driver("Низкий", 0.95),
        Driver("Номинальный", 1),
        Driver("Высокий", 1.07),
        Driver("Очень высокий", 1.15),
        Driver("Сверхвысокий", 1.24),
    ]


class RCPX:
    descr = "Необходимость повторного использования"
    drivers = [
        Driver("Очень низкий", 0.60),
        Driver("Низкий", 0.83),
        Driver("Номинальный", 1),
        Driver("Высокий", 1.33),
        Driver("Очень высокий", 1.91),
        Driver("Сверхвысокий", 2.72),
    ]


class PDIF:
    descr = "Сложность платформы"
    drivers = [
        Driver("Низкий", 0.87),
        Driver("Номинальный", 1),
        Driver("Высокий", 1.29),
        Driver("Очень высокий", 1.81),
        Driver("Сверхвысокий", 2.61),
    ]


class PREX:
    descr = "Опытность персонала"
    drivers = [
        Driver("Очень низкий", 1.33),
        Driver("Низкий", 1.22),
        Driver("Номинальный", 1),
        Driver("Высокий", 0.87),
        Driver("Очень высокий", 0.74),
        Driver("Сверхвысокий", 0.62),
    ]


class PERS:
    descr = "Способности персонала"
    drivers = [
        Driver("Очень низкий", 1.62),
        Driver("Низкий", 1.26),
        Driver("Номинальный", 1),
        Driver("Высокий", 0.83),
        Driver("Очень высокий", 0.63),
        Driver("Сверхвысокий", 0.5),
    ]


class FCIL:
    descr = "Возможности среды"
    drivers = [
        Driver("Очень низкий", 1.30),
        Driver("Низкий", 1.10),
        Driver("Номинальный", 1),
        Driver("Высокий", 0.87),
        Driver("Очень высокий", 0.73),
        Driver("Сверхвысокий", 0.62),
    ]


class SCED:
    descr = "Сроки"
    drivers = [
        Driver("Очень низкий", 1.43),
        Driver("Низкий", 1.14),
        Driver("Номинальный", 1),
        Driver("Высокий", 1),
        Driver("Очень высокий", 1),
    ]


class EarlyArchitecturalDesignModel:
    Factors = [
        RCPX,
        RUSE,
        PDIF,
        PREX,
        PERS,
        FCIL,
        SCED
    ]

    @staticmethod
    def process(p: float, size: int, factors_idxs: (), man_month_cost: float):
        labor_costs = EarlyArchitecturalDesignModel.__get_labor_costs(p, size, factors_idxs)
        time = EarlyArchitecturalDesignModel.__get_time(labor_costs, p)
        avg_workers = EarlyArchitecturalDesignModel.__get_avg_workers(time, labor_costs)
        money = EarlyArchitecturalDesignModel.__get_money(time, man_month_cost)
        print(f"Early Arch Design Model: labor = {labor_costs}, time = {time}, avg workers = {avg_workers}, money = {money}")
        return labor_costs, time, avg_workers, money

    @staticmethod
    def __get_time(labor, p):
        degree = 0.33 + 0.2 * (p - 1.01)
        time = 3.0 * pow(labor, degree)
        time = round(time, 3)
        return time

    @staticmethod
    def __get_labor_costs(p: float, size: int, factors_idxs: ()):
        earch = EarlyArchitecturalDesignModel.__get_earch(factors_idxs)
        labor_costs = 2.45 * earch * pow(size, p)
        labor_costs = round(labor_costs, 3)
        return labor_costs

    @staticmethod
    def __get_earch(factors_idxs: ()):
        earch = 1
        n = len(factors_idxs)
        for i in range(n):
            earch *= EarlyArchitecturalDesignModel.Factors[i].drivers[factors_idxs[i]].value
        return earch

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
