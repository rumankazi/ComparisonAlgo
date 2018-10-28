# t-test for independent samples
from math import sqrt
from numpy.random import seed
from numpy.random import randn
from numpy import mean
from scipy.stats import sem
from scipy.stats import t

# function for calculating the t-test for two independent samples
def independent_ttest(n1, n2, alpha, mean1, mean2,std1, std2 ):
	# calculate means
	#mean1, mean2 = mean(data1), mean(data2)
	# calculate standard errors
	#n1, n2 = len(data1), len(data2)
	se1, se2 = std1/sqrt(n1), std2/sqrt(n2)
	# standard error on the difference between the samples
	sed = sqrt(se1**2.0 + se2**2.0)
	# calculate the t statistic
	t_stat = (mean1 - mean2) / sed
	# degrees of freedom
	df = n1 + n2 - 2
	# calculate the critical value
	cv = t.ppf(1.0 - alpha, df)
	# calculate the p-value
	p = (1.0 - t.cdf(abs(t_stat), df)) * 2.0
	# return everything
	return t_stat, df, cv, p

n1 = n2 = 22212
mean1 = 65.151
mean2 = 67.37191078963231
std1 = 1.7211006682351526
std2 = 0.6130009249064623
# calculate the t test
alpha = 0.05
t_stat, df, cv, p = independent_ttest(n1, n2, alpha, mean1, mean2,std1, std2)
print('t=%.3f, df=%d, cv=%.3f, p=%.3f' % (t_stat, df, cv, p))




# interpret via critical value
#if abs(t_stat) <= cv:
#	print('Accept null hypothesis that the means are equal.')
#else:
#	print('Reject the null hypothesis that the means are equal.')
# interpret via p-value
#if p > alpha:
#	print('Accept null hypothesis that the means are equal.')
#else:
#	print('Reject the null hypothesis that the means are equal.')
