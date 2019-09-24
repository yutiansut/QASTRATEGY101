#
import QUANTAXIS as QA
import pandas as pd


def strategy001(data, N=40, mu=1):
    MP = QA.MA((data.high+data.low+data.close)/3, N)
    TR = pd.concat([abs(data.high - data.low), abs(data.high - data.close.shift(1)),
                    abs(data.low - data.close.shift(1))], axis=1).max(axis=1)
    upBand = MP + mu*QA.MA(TR, N)
    dnBand = MP - mu*QA.MA(TR, N)
    FP = MP

    return pd.DataFrame({'MP': MP, 'MPDIFF': MP.diff(), 'TR': TR, 'upBand': upBand, 'dnBand': dnBand, 'FP': FP})
