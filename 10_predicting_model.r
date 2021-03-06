# Import Google Trends Data
google = read.csv('GoogleTrendsMerc_Weekly.csv');
google$date = as.Date(google$week);	# Column name in the csv file
# Sales Data
dat = read.csv('leftlane_merc_monthly.csv');
dat$month = as.Date(dat$Month)
# Get ready for forecasting
dat = rbind(dat, dat[nrow(dat), ]);
dat[nrow(dat), 'month'] = as.Date('2013-01-01');
dat[nrow(dat), -1] = rep(NA, ncol(dat)-1);
# Define predictors - Time lags
dat$s1 = c(NA, dat$sales[1:(nrow(dat)-1)])
dat$s12 = c(rep(NA, 12), dat$sales[1: (nrow(dat)-12)]);
# Plot sales and Google Trends Data
par(mfrow=c(2,1));
plot(sales ~ month, data = dat, lwd = 2, type = 'l', main = 'Merc Sales', ylab = 'Sales', xlab = 'Time');
plot(sales ~ week, data = google, lwd = 2, type = 'l', main = 'Google Trends: Merc', ylab = 'Percentage Change', xlab = 'Time');
# Merge sales data w/ Google Trends Data
google$month = as.Date(paste(substr(google$week, 1, 7), '01', sep = '-'));
dat = merge(dat, google);
#### Define Predictor - Google Trends
# t.lag defines the time lag between the research and purchase.
# 	t.lag = 0 if you want to include the last week of the previous month and 1st-2nd week of the corresponding month
#	t.lag = 1 if you want to include 1st-3rd week of the corresponding month
t.lag = 1;
id = which(dat$month[-1] != dat$month[-nrow(dat)]);
mdat = dat[id + 1, c('month', 'sales', 's1', 's12')];
mdat$trends1 = dat$trends[id + t.lag];
mdat$trends2 = dat$trends[id + t.lag + 1];
mdat$trends3 = dat$trends[id + t.lag + 2];
# Divide data by two parts - model fitting & prediction
dat1 = mdat[1:(nrow(mdat)-1), ]
dat2 = mdat[nrow(mdat), ]
#### Exploratory Data Analysis
# Testing Autocorrelation & Seasonality
acf(log(dat1$sales));
#Box.test(log(dat1$sales), type = "Ljung-Box");
# Testing Correlation
plot(y = log(dat1$sales), x = dat1$trends1, main = '', pch = 19, ylab = 'log(Sales)', xlab = 'Google Trends - 1st Week');
abline(lm(log(dat1$sales) ~ dat1$trends1), lwd = 2, col = 1)
cor.test(y = log(dat1$sales, x = dat1$trends1));
cor.test(y = log(dat1$sales, x = dat1$trends2));
cor.test(y = log(dat1$sales, x = dat1$trends3));
##### Fit Model;
fit = lm(log(sales) ~ log(s1) + log(s12) + trends1, data=dat1);
summary(fit)
##### Diagnostic Plot
par(mfrow=c(2,2));
plot(fit)
#### Prediction for the next month;
predict.fit = predict(fit, newdata=dat2, se.fit=TRUE);