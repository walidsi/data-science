######################################################
# Load a data set of hacked passwords
# Passwords data was obtained from: https://www.leakedsource.com
######################################################
setwd("/resources/data")

LinkedIn_Password_Data <- read.csv("/resources/data/LinkedIn_Password_Data.csv")
Passwords <- LinkedIn_Password_Data
head(Passwords, n=5L)


################################################################################
# Finding patterns in data
################################################################################
#Let's look at the hacked passwords
Passwords

#How many of them had the pattern "123" in them?
grep(pattern = "123", x = Passwords$Passwords, value = T)
NROW(grep(pattern = "123", x = Passwords$Passwords, value = T))

#Select all the passwords in the password file with some variation of the pattern "pass". 
#We are using the short form "pass" to fish out terms relating to the word 'Password'
grep(pattern = "pass", x = Passwords$Passwords, value = T)
NROW(grep(pattern = "pass", x = Passwords$Passwords, value = T))


#How do we create a file with different number or letter patterns?
#We will use the patterns we create to see how many hacked passwords we can predict
number_pattern <- substring("123456789",1,1:9)
number_pattern
#How many rows are in this variable?
NROW(number_pattern)


letter_pattern <- substring("abcdefghijklmnopqrstuvwxyz",1,1:26)
letter_pattern
#How many rows are in this variable?
NROW(letter_pattern)

#Let's make some number and letter combinations
numbers_letters <- merge(number_pattern, letter_pattern)
numbers_letters
numbers_letters_merged <- paste0(numbers_letters$x,numbers_letters$y)
numbers_letters_merged
#How many rows are in this variable?
NROW(numbers_letters_merged)

#Let's make some letter and number combinations
letters_numbers <- merge(letter_pattern, number_pattern)
letters_numbers
letters_numbers_merged <- paste0(letters_numbers$x, letters_numbers$y)
letters_numbers_merged
#How many rows are in this variable?
NROW(letters_numbers_merged)

#It is a common practice for people to use their names or names of their children in passwords
#Databases of names are freely available on the internet, let's explore one in R
Database_of_First_Names <- read.csv("/resources/data/Database_of_First_Names.csv", sep="")
Database_of_First_Names


#With a large data set, we can just look at the first 5 lines
head(Database_of_First_Names, n=5L)
#How many names are in this particular list of names?
NROW(Database_of_First_Names)

#Let's create combinations with names and numbers and, numbers and names

#Let's add first names from the Database_of_First_Names file to the number patterns
names_numbers <- paste0(Database_of_First_Names$firstname,number_pattern)
head(names_numbers, 100L)
tail(names_numbers, 100L)
#How many rows are in this variable?
NROW(names_numbers)


#Let's put the numbers before the name
numbers_names <- paste0(number_pattern,Database_of_First_Names$firstname)
head(numbers_names, 10L)
tail(numbers_names, 10L)
#How many rows are in this variable?
NROW(numbers_names)

#We create a variable called 'firstnames' with the same information, but we convert the names to characters
firstnames <- as.character(Database_of_First_Names$firstname)
head(firstnames)

#Make one long list of numbers, letters and, numbers and letters combined
possible_passwords <- c(as.character(firstnames), as.character(letter_pattern), as.character(number_pattern), as.character(numbers_letters_merged), as.character(letters_numbers_merged), as.character(names_numbers), as.character(numbers_names))
NROW(possible_passwords)                                                
head(possible_passwords, 10L)
tail(possible_passwords, 10L)

#Let's change the possible_passwords variable from rows to columns 
#so we can compare it to the hacked passwords
possible_passwords <- data.frame(possible_passwords)
head(possible_passwords)
tail(possible_passwords)


######################################################
# Let's see how many passwords we can predict 
# with the possible_passwords file we just created
######################################################
matched_passwords <- unique(rbind(merge(Passwords, possible_passwords, by.x = "Passwords", by.y = "possible_passwords", all.x = FALSE)))

#Let's look at the matched passwords
matched_passwords

#How many passwords did we successfully predict?
NROW(matched_passwords)

#How many passwords were there in total?
NROW(Passwords)

#What percentage of passwords were we able to predict?
round(NROW(matched_passwords)/NROW(Passwords), 2)

#Sum the frequencies to get the number of times these passwords were used
#How many accounts would have been compromised with this exercise?
sum(matched_passwords$Frequency)
#1,362,855 that's 1.3million accounts.

#What is the percentage of accounts that would have been compromised with this exercise?
round(sum(matched_passwords$Frequency) / sum(Passwords$Frequency), 2)
#62%

#If any of your passwords look like the ones in this exercise, consider changing them.

#Thanks for your time, follow us @fireside_info

