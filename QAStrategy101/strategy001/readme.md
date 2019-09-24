# S001 King Keltner

King Keltner 策略是基于移动平均线创立的, 基本思想是 在由最高价, 最低价, 收盘价得出的中心价格基础上计算出市场价格通道线的上下轨, 当价格上穿上轨时做多, 下穿下轨时做空, 由于不是每一次突破都会成功, 因此, 合理的止损设置显得尤为重要, 在kk策略中, 选择中心价格作为出场信号

1. 计算中心价 MP = 最高价, 最低价, 收盘价三者平均后的40周期移动平均价

MP = MA((high+low+close)/3, 40)


2. 计算真实价格区间 TrueRange

TR =  max( abs(high_t - low_t), abs(high_t- close_t-1), abs(low_t - close_t-1))

3. 计算通道上下轨 (upBand, dnBand), 其中mu是一个可变参数, 默认为1

upBand = MP + mu*MA(TR, 40)

dnBand = MP - mu*MA(TR, 40)

4. 计算平仓价格

FP = MP = MA((high+low+close)/3, 40)

5. 开平仓条件

买入开仓 BUY_OPEN : 当前周期MP > 上一个周期的MP  AND 当前价格 > upBand

卖出开仓 SELL_OPEN:  当前周期MP < 上一个周期的MP  AND 当前价格 < dnBand

平仓 : 当前周期价格 下穿  平仓价格FP

平仓 : 当前周期价格 上穿  平仓价格FP

平仓既是止盈 也是止损条件


策略简单描述到此, 下面进入分析和策略代码部分