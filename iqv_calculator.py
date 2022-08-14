"""
The formula for the index of qualitative variation is:
IQV = K(1002 – ΣPct2) / 1002(K – 1)
"""


def get_iqv(series, percent_ratio: bool = True):
    """
    IQV Calculation
    1. Square the percentages for each category.
    2. Sum the squared percentages.
    3. Calculate the IQV using the formula above.
    :param series: List of values (%)
    :param percent_ratio: True if in ratio or percentage
    :return: IQV
    """

    sum_all = []
    for i in range(len(series)):
        if percent_ratio:
            sum_all.append(series[i] ** 2)
        else:
            sum_all.append((series[i] / sum(series) * 100) ** 2)
    return (len(series) * (100**2 - sum(sum_all))) / ((100**2) * (len(series) - 1))


#%%
