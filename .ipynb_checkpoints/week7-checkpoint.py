from numpy import random
import numpy as np

def movie_th(seats=30):
    ticket_cost = 75
    ticket_cost_child = 50 
    ticket_senior_citizens= 60
    movies = ['Father', 'The Barkers', 'Soul', 'NomadLand', 'Tom Jerry']
    screens = 5
    week_days =[]
    for day in range(1,8,1):
            #print(len(week_days))
            # Keep track of total revenue for the day
            total_revenue_day =0
            disc=0
            for screen in range (1,5,1):
                for each_screen in range (seats):
                    visitors_adults = random.choice(seats+1)
                    visitors_children= random.choice(seats+1)
                    visitors_senior_citizens= random.choice(seats+1)


                    # Calculate revenue, and add to running total for the day For theater
                    revenue_adults = visitors_adults * ticket_cost
                    revenue_children = visitors_children * ticket_cost_child

                    # 10% discount on senior citizen ticket costs
                    if (day==6):
                        disc=ticket_senior_citizens*0.9
                        revenue_senior_citizens = disc * visitors_senior_citizens
                    else:
                        revenue_senior_citizens = visitors_senior_citizens * ticket_senior_citizens



                    revenue_screen = revenue_adults + revenue_children


                    # Save total to the corresponding day for theater
            total_revenue_day = total_revenue_day + revenue_screen
            week_days.append(total_revenue_day)
                   # week_days[day] = total_revenue_day[day]
    return(week_days)





def max_day():
    max_d = max(week_days)
    count=1
        #should edti
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    for i in week_days:
        if ( i == max_d):
            print(f"{days[count]} is the highest revenue day in the week with a total of {max_d}")

        count = count+1
    