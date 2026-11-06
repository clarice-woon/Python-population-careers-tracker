# Python-population-careers-tracker
A python programme should also allow users to run these tasks: The user chooses either an occupation or an age group as the subject-matter, and is presented with its career trends over the years.

# User can run the programme until they key in "q" to terminate
My overall program starts with a while true loop, allowing users to loop this program continuously until they enter q to terminate.

When the user terminates, there will be summarised analytics of the queries they've made if they chose to see employment data across industries (option 1), in addition to the output csv file. Otherwise, for options 2 to 4, the output is just the csv file highlighting the trends across years.

	Enter a year: 2022
	Data has been output into out.csv file.
	The industry that provides the greatest employment opportunities in 2022 is Services:Wholesale & Retail Trade.

	Enter 1 to see employment data across industries.
	Enter 2 to see trends across age groups for an industry over the years.
	Enter 3 to see trends across age groups for an occupation over the years.
	Enter 4 to see trends across occupations for an age group over the years.
	Enter'q' to quit program.

	Exiting program.
	In 2022, the construction hired the most employees from the age range 55 - 59 Years.
	The industry that provides the greatest employment opportunities in 2022 is Services:Wholesale & Retail Trade.

When user starts a new query, the summary contents are cleared and user can start afresh.

# Analysis question: Which industry sectors provide the greatest employment opportunities? Are there preferences for age ranges among industries? 
To answer our analysis question, I will run option 1 and give the programme takes a year input. The code then finds the industry sublist with max percentage in this year, then it finds the corresponding age range. In my summary analytics, I am able to see which industry hires most, and specifically which age group they tend to hire, which shows their age preferences for employees.

Other than the summary analytics, by looking at the csv file output, I can gain new insights about the other industries too. From the results in table 1 and 2 (in the slides), it appears that the wholesale and retail trade, as well as the public administration and education industry offer the most opportunities for employment. Factors affecting employment opportunities could include the level of government support and the ease of entering the industry.

And yes, there are age preferences in certain industries like manufacturing. This could be because of the level of expertise and physical strength needed to operate the machinery. Thus, most employees that possess a mix of both would be in the middle-aged range.

Lastly, codes for table 3 and 4 are similar to table 2, except the program will read datasets B and C rather than A and C. These two tables look at the occupations rather than industries.

From the two tables, we can see that 15-19 year olds would find most opportunity in the "others" category, perhaps in gig works. They would have least opportunity to work as a manager and administrator, perhaps because these occupations require years of experience, and as shown in table 3, would actually favour middle-aged employees.
