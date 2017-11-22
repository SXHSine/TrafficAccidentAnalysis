import pandas as pd
import numpy as np
from pandas.tseries.holiday import USFederalHolidayCalendar as calendar


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pandas.tools.plotting import parallel_coordinates

import matplotlib as mpl
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid",{"font.sans-serif":['simhei', 'Arial']})

from scipy import stats
import math

data = pd.read_excel('data_heatMap_17.9.25.xlsx')
#ax = sns.boxplot(x="周几", y="事故损失值", data=data, whis=np.inf)
#ax = sns.stripplot(x="周几", y="事故损失值", data=data,jitter=True, color=".3")

#ax = sns.boxplot(x="时段", y="事故损失值", data=data, whis=np.inf)
ax = sns.stripplot(x="时段", y="事故损失值", data=data,jitter=True, color=".3")
plt.show()