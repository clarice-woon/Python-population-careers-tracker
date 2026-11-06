# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 11:21:17 2025

@author: woonc
"""
# https://youtu.be/J2pcrBS2IFw
# Scenario: Which industry sectors provide the greatest employment opportunities? Are there preferences among the age-ranges for industries? 
# E.g. User can enter a year and be presented with a table showing the number of people and percentage in each industry for the year. 
# User may pick an occupation and be presented with the trends over the years by age groups or pick an age group and show the trend over the years by occupations.


import csv
    
def emp_each_industry():
    interested_year=int(input("Enter a year: ")) #convert to integer
    with open("out.csv","w",newline="") as f_out: #specify newline as none
        csv_pointer_outw=csv.writer(f_out)
        header=[[f"Chosen year is {interested_year}"],["Industry","Number of Employees Hired by Each Industry","Percentage of Employees in Each Industry/%"]]
        csv_pointer_outw.writerows(header) 
        row=["age_range","industry",2024,2023,2022,2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007]
        year_index=row.index(interested_year) #refers to "row" list and gives index in row where the targetted year is
        #column 1 in out.csv
        industries=[["Manufacturing"],["Construction"],["Services:Wholesale & Retail Trade"],["Services:Transportation & Storage"],["Services:Accommodation & Food Services"],["Services:Information & Communications"],["Services:Financial & Insurance Services"],["Services:Real Estate Services"],["Services:Professional Services"],["Services:Administrative & Support Services"],["Services:Public Administration & Education"],["Services:Health & Social Services"],["Services:Arts, Entertainment & Recreation"],["Services:Other Community, Social & Personal Services"],["Others"]]
        #column 2 in out.csv
        num_of_employees_hired=[[0] for _ in range(len(industries))] #len(outer_list)=num of sublists
        #column 3 in out.csv
        per_of_emp_each_industry=[[0] for _ in range(len(industries))]
        total_employees=0
        for sublist in industries: #iterations in sublist of nested list
            for industry in sublist: #goes manufacturing, then construction and so on and so forth
                with open("C:/Users/woonc/OneDrive/Desktop/NTU/Decision making with programming and analytics/Python wk 8 indiv/A. Employed Residents Aged 15 Years And Over By Industry And Age Group.csv", "r") as A_in:
                    #open file in each loop iteration so pointer can go back to start of the file
                    csv_pointerA_r=csv.reader(A_in)
                    for line in csv_pointerA_r: 
                        if line[1]==industry: #e.g. equals manufacturing
                            a=industries.index(sublist) #so that sublists in three columns are corresponding
                            try:
                                num_of_employees_hired[a][0]+=float(line[year_index]) #num of employees in desired year
                                total_employees+=float(line[year_index])
                            except:
                                pass #when na or - data
        for i,sublist1 in enumerate(num_of_employees_hired):
            for value in sublist1:
                per_of_emp_each_industry[i][0]=(value/total_employees)*100 
        for b in range(len(industries)):
            data=[industries[b][0],num_of_employees_hired[b][0],per_of_emp_each_industry[b][0]] #joins three nested list to form one row in each iteration
            csv_pointer_outw.writerow(data)
    for x,sublist2 in enumerate(per_of_emp_each_industry):
        for value in sublist2:
            if value==max(max(sublist) for sublist in per_of_emp_each_industry): #maximum percentage in the column
                max_industry_index=x #finds index of sublist (industry) with the highest percentage of employees hired
    industry_with_max=industries[max_industry_index][0] 
    print("Data has been output into out.csv file.")
    print(f"The industry that provides the greatest employment opportunities in {interested_year} is {industry_with_max}.\n")
    with open("analytics.txt","a") as f_analytics: # use "a" to append, so file contents will not be cleared when opened again
        print(f"The industry that provides the greatest employment opportunities in {interested_year} is {industry_with_max}.\n",file=f_analytics)
   

def industry_age_pref():
    input_industry=input("Enter an industry:")
    interested_industry=input_industry.replace(" ","").lower()
    with open("out.csv","w",newline="") as f_out:
        csv_pointer_outw=csv.writer(f_out)
        years=[2024,2023,2022,2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007] #to be added in header row
        header=[[f"Chosen industry is {input_industry}",f"Percentage of {input_industry} Employees in this Age Group/%"],["Age Group"]+years]
        csv_pointer_outw.writerows(header)
        # column 1 in out.csv - age_groups
        age_groups=["15 - 19 Years","20 - 24 Years","25 - 29 Years","30 - 34 Years","35 - 39 Years","40 - 44 Years","45 - 49 Years","50 - 54 Years","55 - 59 Years","60 - 64 Years","65 Years & Over"]
        emp_each_age_group=[[] for _ in range(len(age_groups))]
        # column 2 in out.csv - emp_perc_age_group
        emp_perc_age_group=[[0]*len(years) for _ in range(len(age_groups))]
        occupation_total_over_years=[0]*len(years) # to be used for percentage calculation
        with open("C:/Users/woonc/OneDrive/Desktop/NTU/Decision making with programming and analytics/Python wk 8 indiv/A. Employed Residents Aged 15 Years And Over By Industry And Age Group.csv", "r") as A_in:
            csv_pointerA_r=csv.reader(A_in)
            for line in csv_pointerA_r: #pointer reads the file
                row_industry=line[1].replace(" ","").lower()
                if row_industry==interested_industry: #e.g. equals manufacturing   
                    a=age_groups.index(line[0]) #so that row in age_groups column can match corresponding row in emp_each_age_group
                    emp_each_age_group[a]=line[2:20] #num of employees over the years 
                    for i,value in enumerate(line[2:20]):
                        try:
                            occupation_total_over_years[i]+=float(value)
                        except: 
                            pass #when na or - data
            for emp_specific_age_grp,sublist1 in enumerate(emp_each_age_group):
                for emp_year,emp_in_year in enumerate(sublist1):
                    try:
                        emp_perc_age_group[emp_specific_age_grp][emp_year]=(float(emp_in_year)/occupation_total_over_years[emp_year])*100 #float()
                    except: 
                        pass
                        #emp_perc_age_group[emp_specific_age_grp][emp_year]=emp_each_age_group[emp_specific_age_grp][emp_year]
                        # when emp_in_year=="na"/"-"
            for age_grp, sublist2 in enumerate(emp_perc_age_group):
                sublist2.insert(0,age_groups[age_grp])
                csv_pointer_outw.writerow(sublist2)
    print("Data has been output into out.csv file.\n")
    year_findmax=int(input(f"Enter a year to find the age range with most hired by {input_industry}:"))
    year_findmax_index=years.index(year_findmax) 
    for x,sublist3 in enumerate(emp_perc_age_group):
        for value in sublist3:
            if value==max(sublist[year_findmax_index+1] for sublist in emp_perc_age_group): # finds maximum percentage in 2024 among age groups
                age_range_with_max_index=x
    age_range_with_max=age_groups[age_range_with_max_index] #index 0 looks at year selected
    print(f"In {year_findmax}, the {input_industry} hired the most employees from the age range {age_range_with_max}.\n")
    with open("analytics.txt","a") as f_analytics:
        print(f"In {year_findmax}, the {input_industry} hired the most employees from the age range {age_range_with_max}.",file=f_analytics)

def trend_over_age():
    input_occupation=input("Enter the occupation:")
    interested_occupation=input_occupation.replace(" ","").lower() #to remove spaces and standardise format for comparison
    with open("out.csv","w",newline="") as f_out:
        csv_pointer_outw=csv.writer(f_out)
        years=[2024,2023,2022,2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007]
        header=[[f"Chosen Occupation is {input_occupation}",f"Percentage of {input_occupation} Employees in this Age Group/%"],["Age Group"]+years]
        csv_pointer_outw.writerows(header)
        age_groups=["15 - 19 Years","20 - 24 Years","25 - 29 Years","30 - 34 Years","35 - 39 Years","40 - 44 Years","45 - 49 Years","50 - 54 Years","55 - 59 Years","60 - 64 Years","65 Years & Over"]
        emp_each_age_group=[[] for _ in range(len(age_groups))]
        emp_perc_age_group=[[0]*len(years) for _ in range(len(age_groups))]
        occupation_total_over_years=[0]*len(years)
        with open("C:/Users/woonc/OneDrive/Desktop/NTU/Decision making with programming and analytics/Python wk 8 indiv/B. Employed Residents Aged 15 Years And Over By Occupation And Age Group).csv", "r") as B_in:
            csv_pointerB_r=csv.reader(B_in)
            for line in csv_pointerB_r: #pointer reads the file
                row_occupation=line[1].replace(" ","").lower() #e.g. "associateprofessionals&technicians"
                if row_occupation==interested_occupation: 
                    a=age_groups.index(line[0])
                    emp_each_age_group[a]=line[2:20] #num of employees over the years 
                    for i,value in enumerate(line[2:20]):
                        try:
                            occupation_total_over_years[i]+=float(value)
                        except: 
                            pass
            #print(emp_each_age_group)
            for emp_specific_age_grp,sublist1 in enumerate(emp_each_age_group):
                for emp_year,emp_in_year in enumerate(sublist1):
                    try:
                        if emp_in_year=="na":
                            emp_perc_age_group[emp_specific_age_grp][emp_year]="na"
                        else:
                            emp_perc_age_group[emp_specific_age_grp][emp_year]+=(float(emp_in_year)/occupation_total_over_years[emp_year])*100 #float()
                    except: #some age groups have zero employees in certain years in the chosen occupation
                        emp_perc_age_group[emp_specific_age_grp][emp_year]=0
            for age_grp, sublist2 in enumerate(emp_perc_age_group):
                sublist2.insert(0,age_groups[age_grp])
                csv_pointer_outw.writerow(sublist2)
    print("Data has been output into out.csv file\n")  
    
                
def trend_over_occupations():
    input_age_grp=input("Enter an age group: ")
    interested_age_grp=input_age_grp.replace(" ","").lower() #replace and lower to standardise
    with open("out.csv","w",newline="") as f_out: #newline change from default
        csv_pointer_outw=csv.writer(f_out)
        years=[2024,2023,2022,2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007]
        header=[[f"Chosen Age Group is {input_age_grp}",f"Percentage of Employees Aged {interested_age_grp} in this Occupation/%"],["Occupation"]+years]
        csv_pointer_outw.writerows(header)
        occupations=["Associate Professionals & Technicians","Cleaners, Labourers & Related Workers","Clerical Support Workers","Craftsmen & Related Trade Workers","Managers & Administrators (Including Working Proprietors)","Plant & Machine Operators & Assemblers","Professionals","Service & Sales Workers","Others"]
        emp_each_occupation=[[] for _ in range(len(occupations))] #len(outer_list)=num of sublists
        emp_perc_occupation=[[0]*len(years) for _ in range(len(occupations))]
        age_grp_total_over_years=[0]*len(years)
        with open("C:/Users/woonc/OneDrive/Desktop/NTU/Decision making with programming and analytics/Python wk 8 indiv/B. Employed Residents Aged 15 Years And Over By Occupation And Age Group).csv", "r") as B_in:
            csv_pointerB_r=csv.reader(B_in)
            for line in csv_pointerB_r: #pointer reads the file
                row_age_grp=line[0].replace(" ","").lower()
                if row_age_grp==interested_age_grp:
                    a=occupations.index(line[1].strip())
                    emp_each_occupation[a]=line[2:20] #num of employees over the years 
                    for i,value in enumerate(line[2:20]):
                        try:
                            age_grp_total_over_years[i]+=float(value)
                        except: 
                            pass
            for emp_specific_occupation,sublist1 in enumerate(emp_each_occupation):
                for emp_year,emp_in_year in enumerate(sublist1):
                    try:
                        if emp_in_year=="na":
                            emp_perc_occupation[emp_specific_occupation][emp_year]="na"
                        else:
                            emp_perc_occupation[emp_specific_occupation][emp_year]+=(float(emp_in_year)/age_grp_total_over_years[emp_year])*100 #float()
                    except: #some age groups have zero employees in certain years in the chosen occupation
                        emp_perc_occupation[emp_specific_occupation][emp_year]=0
            for occupation, sublist2 in enumerate(emp_perc_occupation):
                sublist2.insert(0,occupations[occupation])
                csv_pointer_outw.writerow(sublist2)
    print("Data has been output into out.csv file.\n")   

    
                
#Program
while True:
    user_input=input("Enter 1 to see employment data across industries.\nEnter 2 to see trends across age groups for an industry over the years.\nEnter 3 to see trends across age groups for an occupation over the years.\nEnter 4 to see trends across occupations for an age group over the years.\nEnter'q' to quit program.\n")
    if user_input=="1":
        emp_each_industry()
    elif user_input=="2":
        industry_age_pref()
    elif user_input=="3":
        trend_over_age()
    elif user_input=="4":
        trend_over_occupations()
    elif user_input=="q":
        print("Exiting program.")
        with open("analytics.txt","r") as f_summary:
            for line in f_summary:
                print(line,end="")
        f_summary=open("analytics.txt","w")
        f_summary.close() #to clear file contents
        break
    else:
        print("\nEnter 1, 2, 3, 4 or'q'\n")
        

        
        
        
        
        