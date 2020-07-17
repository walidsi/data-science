#Digital Analytics and Regression with Google Trends Data


###########################################################################
#                    Some notes before we start coding
###########################################################################

# 1. The '#' precedes comments or notes, it tells R that this is not a command.
# 2 .Notes here are to assist you in the exercise.
# 3. R is case sensitive!!
# 4. You will enter instructions in this quadrant (top left), and you will see them and their output in the bottom left quadrant.
# 5. Ctrl+Enter runs a line of script. You will hit 'Ctrl+Enter' along each of the lines in this script to follow the lesson.
# 6. Feel free to experiment, change some of the script and see what happens. 
# 7. You can always go back to the original file.
# 8. In the toolbar above, the page icon with a green circle and a white cross in it will open a new 'sheet' for you.
# 8.b. You can copy paste code from this R file into a new sheet, a new .R file. Remember to save changes if you wish to access that new file again.
# 9. If you need help in R at any time, type in, "?" + "the thing you need help with", as a command then Ctrl+Enter to 'run' it as an instruction to R
# 9.a. Try using 'help' in R with the 'head' command below. The results will appear in the bottom right hand quadrant. 
?head
# 10. The bottom left quadrant can get very busy, if you want to clear it, type Ctrl+L. Your session will still be active.
# 11. Plots appear in the bottom right hand quadrant. Make sure you are in the 'Plots' tab to see your charts.
# 12. Lastly, "data is" or "data are", focus, we have work to!

###########################################################################
#                    Exercise
###########################################################################
#Access Google Trends through R
#Compare different search terms
#Visualize the data
#Conduct basic statistical analyses

#More notes:
#The "<-" sign means that the item on the left 'gets' the item on the right
#This way we can create many objects in R and refer to them in different contexts
#As an example you can try something simple like assigning the number 1 to the letter a and hte number 2 to the letter b
a <- 1
b <- 2
#You can now refer to a and b as though they were 1 and 2 e.g., a + b. Run it and see the result
a + b
#See the answer in the quadrant below!

###########################################################################
#                    Begin!
###########################################################################

#Set where your files will be uploaded and downloaded from in RStudio within Data Scientist Workbench
#Note that files will now be accessed through Data Scientist Workbench in your browser, not your local c drive
setwd("/resources/data")


###########################################################################
#                    Upload & Transform a Google Analytics .csv file
###########################################################################

case_data <- "report.csv"
open_file  <- file(case_data, open = "r")

linecount <- 0
string_data <- ""
while (length(single_line <- readLines(open_file, n = 1, warn = FALSE)) > 0) {
  linecount <- linecount + 1
  
  if (linecount < 3) {
    case_data <- paste0(case_data,single_line)     
  }
  
#Typical Google Analytics CSV outputs have the column headings in row 5
  if (linecount == 5) column_headings = strsplit(single_line, ",")[[1]]
  
#We do not need the first 5 lines in the CSV
  if (linecount > 5) {

#Typical Google Analytics CSV outputs have a blank row after the first data set
    if (gsub(pattern=",", x=single_line, replacement="") == "") break
    
    string_data <- paste0(string_data,single_line,"\n")
  }
}
close(open_file)

case_table <- read.table(textConnection(string_data), sep=",", header=FALSE, stringsAsFactors = FALSE)

#Assigning the column headings to our data table
names(case_table) <- column_headings

###########################################################################
#                    Let's look at the data
###########################################################################

head(case_table)
column_headings

#Instead of the complex 'Week' column, let's add an ID column
case_table$WeekID<-seq.int(nrow(case_table))

head(case_table)

#We can also look at the data using
print(case_table)

#Or
case_table

#With big data, you would not want to call all the rows in your data set
#so you can call a specific number of lines
head(case_table, n = 10L)
#Brings back the first 10 lines, n = 10L
#You can also only bring back the summary for one column using the $ sign
head(case_table$WeekID, n = 10L)

#We can now start plotting the different trends!

##############################################################
#                    Plotting Google Trends in R
##############################################################

plot(case_table$WeekID, case_table$analytics, type='l', col='orange')
lines(case_table$WeekID, case_table$`google analytics`, type='l', col='red')


###########################################################################
#   Which search term has the highest search volumes in Google Trends?
###########################################################################

par(mfrow = c(1, 1))
plot(case_table$WeekID, case_table$analytics, 
     main = "Searches for 'Analytics' & 'Data Scientist'",
     ylab = "Search Index (0 to 100)",
     xlab = "Week Index",
     type = 'l',
     col  = 'orange')
lines(case_table$WeekID, case_table$`data scientist`, type = 'l', col = 'red')

#To learn more about 'plot', use the R help function:
?plot

#Is 'data scientist' too narrow? It has very few searches, what about 'data science'?
par(mfrow = c(1, 1))
plot(case_table$WeekID, case_table$analytics, 
     main = "Searches for 'Analytics' & 'Data Science'",
     ylab = "Search Index (0 to 100)",
     xlab = "Week Index",
     type = 'l',
     col  = 'blue')
lines(case_table$WeekID, case_table$`data science`, type = 'l', col = 'darkgreen')
#See the new plot on in the bottom right hand quadrant

#Is there a difference between 'data scientist' and 'data science'?
par(mfrow = c(1, 1))
plot(case_table$WeekID, case_table$`data scientist`, 
     main = "Searches for 'Data Scientist' & 'Data Science'",
     ylab = "Search Index (0 to 100)",
     xlab = "Week Index",
     type = 'l',
     col  = 'red')
lines(case_table$WeekID, case_table$`data science`, type = 'l', col = 'blue')

#All versions of 'data science' are exclipsed by searches for 'analytics'
#The Search Index (0 to 100) only goes up to 4 out of a maximum value of 100 for 'data scientist' and 'data science'

###########################################################################
#                    Let's look at correlation
###########################################################################

#R's default correlation is 'pearson' if none is specified
?cor

#What is the relationship between searches for 'data science' and 'data scientist'?
#Can we quantify that relationship?
cor(case_table$`data science`,case_table$`data scientist`)
#The answer will appear in the bottom left quadrant in the RStudio Console below

#Round off decimal points
round(cor(case_table$`data science`,case_table$`data scientist`), digits = 2)
#The correlation for data scientist and data science terms is 88% so we will conclude that 
#People are using these search terms in a similar way, in a similar pattern, in similar weeks

#What is the correlation between 'analytics' and 'machine learning'
round(cor(case_table$`analytics`,case_table$`machine learning`), digits = 2)
#What is the correlation between 'data science' and 'machine learning'

round(cor(case_table$`data science`,case_table$`machine learning`), digits = 2)
#There is a strong positive correlation between 'data science' and 'machine learning'
#There is a weak correlation between 'analytics' and 'machine learning'

#Let's work with the two variables, 'data science' and 'analytics' 
par(mfrow = c(1, 1))
plot(case_table$WeekID, case_table$analytics, 
     main = "Searches for 'Analytics' & 'Data Science'",
     ylab = "Search Index (0 to 100)",
     xlab = "Week Index",
     type = 'l',
     col  = 'blue')
lines(case_table$WeekID, case_table$`data science`, type = 'l', col = 'red')


#Can we quantify this relationship?
round(cor(case_table$analytics,case_table$`data science`), digits = 2)
#The correlation is only 18%, we can conclude that these two searches are not happening in a similar way
#These may be different people searching or people searching for different content

###########################################################################
#                    Summary statistics
###########################################################################

#Summary statistics for each variable
summary(case_table)

#Let's make it easier to work with the two search terms we are interested in 'analytics' and 'data science'
#We'll shorten how we refer to them by creating new variables
Analytics <- c(case_table$analytics)
DataScience <- c(case_table$`data science`)

#To get more statistical information like skew and kurtosis, we use a package called 'psych'
install.packages("psych")
#This may take a minute
library(psych)

describe(Analytics)
describe(DataScience)

#The search behavior for the two terms is very different. 
#How can we learn more about the individual distributions?

###########################################################################
#                    Box plots
###########################################################################

par(mfrow = c(1, 1))
boxplot(Analytics, DataScience, 
        names = c("Analytics","DataScience"),
        xlab  = "Search Terms",
        ylab  = "Search Index (0 to 100)",
        main  = "Boxplot of search terms",
        col   = "orange")


###########################################################################
#                    Histograms
###########################################################################

par(mfrow = c(2, 1))
hist(Analytics,
     main = "Histogram of Searches for 'Analytics'",
     ylab = "Frequency of searches",
     xlab = "Search Index (0 to 100)",
     col  = "orange")
hist(DataScience,
     main = "Histogram of Searches for 'DataScience'",
     ylab = "Frequency of searches",
     xlab = "Search Index (0 to 100)",
     col  = "blue")
#Search Index Number is between 1 and 100

###########################################################################
#                    Scatter plots
###########################################################################

par(mfrow = c(2, 1))
plot(Analytics,
     main = "Scatter plot of searches for Analytics",
     col  = "maroon")
plot(DataScience,
     main = "Scatter plot of searches for Data Science",
     col  = "darkgreen")
plot(Analytics,DataScience,
     main = "Scatter plot of searches, Analytics vs. DataScience",
     col  = "orange")

#What does that look like? We compare 'data science' and 'machine learning'
plot(DataScience, case_table$`machine learning`,
     main = "Scatter plot of searches, 'DataScience' vs. 'Machine Learning'",
     col  = "darkblue")
#The few data points in the plot look positive correlated, and we know that they are
round(cor(case_table$`data science`,case_table$`machine learning`), digits = 2)
#There is a strong positive correlation between 'data science' and 'machine learning'
# 90%


###########################################################################
#                    Strong positive correlation
###########################################################################

#Of the Google Trends data we pulled, is there anything else in there that is highly correlated to 'analytics'?

#Remember this?
#What data is actually being pulled?
head(case_table)

#Take a closer look at the other columns in the extraction
column_headings

#Let's make it easier to work with the term 'Google Analytics'
#We'll shorten how we refer to it by creating a new variable
GoogleAnalytics <- c(case_table$`google analytics`)

#Let's test whether people searching for 'analytics' are likely searching for 'google analytics' related content
par(mfrow = c(1, 1))
plot(case_table$WeekID, case_table$analytics, 
     main = "Searches for 'Analytics' & 'Google Analytics'",
     ylab = "Search Index (0 to 100)",
     xlab = "Week Index",
     type = 'l',
     col  = 'blue')
lines(case_table$WeekID, GoogleAnalytics, type = 'l', col = 'red')

#Can we quantify this relationship?
round(cor(Analytics,GoogleAnalytics), digits = 3)

#A perfect correlation is 100%, these two terms have a near perfect correlation!
#These searches are consistent with searches more about digital marketing, search engine marketing and general analytics

#Let's see if the distributions for the two terms are similar?
#Recall the package 'Psych'?

describe(Analytics)
describe(GoogleAnalytics)

#The search behavior for the two terms is very similar. 
#How can we learn more about the individual distributions?

###########################################################################
#                    Visualizing the strong positive correlation
###########################################################################

par(mfrow = c(1, 1))
boxplot(Analytics, GoogleAnalytics, 
        names = c("Analytics","Google Analytics"),
        xlab  = "Search Terms",
        ylab  = "Search Index (0 to 100)",
        main  = "Boxplot of search terms",
        col   = "maroon")

#**********Look at histograms**********
par(mfrow = c(2, 1))
hist(Analytics,
     main = "Histogram of Searches for 'Analytics'",
     ylab = "Frequency of searches",
     xlab = "Search Index (0 to 100)",
     col  = "orange")
hist(GoogleAnalytics,
     main = "Histogram of Searches for 'Google Analytics'",
     ylab = "Frequency of searches",
     xlab = "Search Index (0 to 100)",
     col  = "grey")


#**********Look at scatter plots**********
par(mfrow = c(1, 1))
plot(GoogleAnalytics, Analytics,
     main = "Scatter plot of searches, Analytics vs. Google Analytics",
     col  = "orange")
#Note that 'Analytics' is on the 'y' axis, that is known as the 'dependent variable'

#Add a line of best fit
abline(lm(formula = Analytics ~ GoogleAnalytics), main = "Scatter plot of searches, Analytics vs. Google Analytics", col="red") 


###########################################################################
#                    Regression
###########################################################################

#To fit an ordinary linear model, we use the 'lm' function for 'linear model'
#We assign the results to an object called 'Regression'
Regression <- lm(formula = Analytics ~ GoogleAnalytics)
#The first variable is the target variable and the second is the predictor variable or explanatory variable
#We are looking to see if variations in the variable 'Analytics' can be explained by variations in the variable 'GoogleAnalytics'


#Let's look at it in the  console below: 
Regression

#Round output to 2 decimal places
#Round(x,digits = 2)

round(coef(Regression), digits = 2)

#Regression output
summary(Regression)
round(summary(Regression)$coefficients, digits = 3)
round(summary(Regression)$r.squared, digits = 3)

par(mfrow = c(1, 1))
plot(GoogleAnalytics, Analytics,
     main = "Scatter plot of searches, Analytics vs. Google Analytics",
     col  = "orange")

plot(Regression)
#Show all 4 charts in the same view using 'par'
par(mfrow = c(2,2))

#Now for the Regression plots:
plot(Regression)

abline(Regression)

#Note the 'Zoom' button in the 'Plots' tab in the bottom right hand quadrant 
#'Zoom' will open the chart in a new browser window, you may get be asked to allow the 'pop-up'

#We can call out specific values of interest from the 'Regression' output e.g., r squared
round(summary(Regression)$r.squared, digits = 2)
#Note the near perfect R-Squared in the output
#Note the statistically significant P-Value

#What else can you pull out?
names(summary(Regression))

#So what is our model or line of best fit formula?
Regression
#Y = 4.132 + 1.751X

#This formula can be read as: analytics = 4.140 + 1.754googleanalytics 
#What search index number for 'analytics' can we expect when the searche index for 'googleanalytics' is 33?
4.132 + (1.751*33) 

#The answer will appear in the bottom left quadrant in RStudio

#Round it off to one decimal point.
round(4.132 + (1.751*33), digits = 1)

