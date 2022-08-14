"""
The formula for the index of qualitative variation is:
IQV = K(1002 – ΣPct2) / 1002(K – 1)
"""


def get_iqv(series):
    """
    IQV Calculation
    1. Square the percentages for each category.
    2. Sum the squared percentages.
    3. Calculate the IQV using the formula above.
    :param series: List of values (%)
    :return: IQV
    """
    sum_all = []
    for i in range(len(series)):
        sum_all.append(series[i] ** 2)
    return (len(series) * (100**2 - sum(sum_all))) / ((100**2) * (len(series) - 1))
