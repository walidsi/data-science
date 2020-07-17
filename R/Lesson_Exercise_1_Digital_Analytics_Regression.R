#Big Data University Lesson Exercise


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

#Or if you're used to spreadsheet formats, this output looks like a table
#NB: The 'table' appears in a different tab in the tool bar so you would need to come back to this tab after viewing your data
View(case_table)

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

#Is there a difference between searches for 'data scientist' and 'data science'?
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

