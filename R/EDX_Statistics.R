bike <- BikeData

# Find the number of students in the dataset
table(bike$student)

# Pull out student data into a new dataframe
student <-bike[bike$student==1,]

# Find how often the students ride, using the new dataframe
table(student$cyc_freq)

# Create a vector for the distance variable
distance <-student$distance

# Find average distance ridden
mean(distance)

males <- bike [bike$gender == 'M',]

male_times <- males$time

mean(male_times)

daily_riders <- bike[bike$cyc_freq == 'Daily', ]

male_daily_riders <- daily_riders[daily_riders$gender=='M',]
female_daily_riders <- daily_riders[daily_riders$gender=='F',]

table(male_daily_riders)
table(female_daily_riders)

table(daily_riders$gender)

mean(daily_riders$age)

mean(female_daily_riders$age)

mean(male_daily_riders$age)

male_daily_riders_thirty <- male_daily_riders[male_daily_riders$age >= 30, ]
table(male_daily_riders_thirty$gender)