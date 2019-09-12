# S002 Bolling Bandit 布林带策略

Bolling Bandit 策略是基于 Bolling Bandit 布林带衍生而来, 标准的Bolling Bandit有三根线: 上下两条是价格的阻力线和支撑线, 中间一条为价格均线

布林带策略是基于移动平均线的基础上加减n个标准差来确定通道的上下轨, 其中n由置信水平确定, 当价格突破轨道线的时候进行开平仓操作


