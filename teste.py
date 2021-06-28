

import seaborn as sns
from scipy import stats

x = stats.uniform(0, 1).rvs(10000)
sns.distplot(x, kde=False, norm_hist=True);

norm = stats.distributions.norm()
x_trans = norm.ppf(x)
sns.distplot(x_trans);
