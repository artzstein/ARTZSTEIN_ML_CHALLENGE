from scipy import stats

mean_delivery_days = 5
std_dev_days = 1.2
# Probability that delivery takes longer than 7 days
prob_long_delivery = 1 - stats.norm.cdf(7, loc = mean_delivery_days, scale = std_dev_days)
print(f"probabilty delvery takes more than 7 days: {prob_long_delivery:.1%}")