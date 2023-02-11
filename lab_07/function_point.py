class Language:
    def __init__(self, name: str, loc_per_fp: int):
        self.name = name
        self.loc_per_fp = loc_per_fp


class FunctionPointMethod:
    EICoefs = [3, 6, 4]
    EOCoefs = [4, 5, 7]
    EQCoefs = [3, 4, 6]
    ILFCoefs = [7, 10, 15]
    EIFCoefs = [5, 7, 10]
    Coefficients = [EICoefs,
                    EOCoefs,
                    EQCoefs,
                    ILFCoefs,
                    EIFCoefs]
    Languages = (
        Language("Ассемблер", 320),
        Language("С", 128),
        Language("Кобол", 106),
        Language("Фортран", 90),
        Language("Паскаль", 53),
        Language("С++", 53),
        Language("Java", 53),
        Language("C#", 53),
        Language("Ada 95", 49),
        Language("Visual Basic 6", 24),
        Language("Visual C++", 34),
        Language("Delphi Pascal", 29),
        Language("Perl", 21),
        Language("Prolog", 54),
        Language("SQL", 46),
        Language("JavaScript", 56),
    )

    @staticmethod
    def count_function_points(quantity):
        fp = []
        n = len(quantity)
        m = len(quantity[0])
        for i in range(n):
            val = 0
            for j in range(m):
                val += quantity[i][j] * FunctionPointMethod.Coefficients[i][j]
            fp.append(val)
        total = sum(fp)
        fp.append(total)
        return fp

    @staticmethod
    def corrected_function_points(fp, sys_params):
        sys_params_sum = sum(sys_params)
        corrected_funct_points = fp * (0.65 + 0.01 * sys_params_sum)
        return corrected_funct_points

    @staticmethod
    def cfp_to_loc(cfp, lang_idx, lang_perc):
        val = 0
        perc_sum = sum(lang_perc)
        n = len(lang_idx)
        for i in range(n):
            loc = cfp * FunctionPointMethod.Languages[lang_idx[i]].loc_per_fp
            val += (loc * lang_perc[i]) / perc_sum
        val = round(val)
        return val
