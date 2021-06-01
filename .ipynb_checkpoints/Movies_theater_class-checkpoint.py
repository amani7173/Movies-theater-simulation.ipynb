
from numpy import random
import numpy as np
from collections import Counter
from itertools import chain
from numpy import random
import numpy as np
from collections import Counter
from itertools import chain


class Movies_theater:
    
    def __init__(self, seats=30 , screens =5):
        self.seats=seats
        self.screens=screens
        
        
        
    def revenue(self , seats=30, screens =5):
        
        '''
        Return the total revenue in the week for each day, snack revenue and total revenue for each day.
        The cost for tickets: 75 SAR for adults, 50 SAR for children and 60 SAR for senior citizens.
        Tha snacks are Popcorn, Cheetos and Nachos, and the drinks are Mojito, Cola and Water.
        The defult number of seats and screens are 30 and 5, you can input different numbers.
        The movies are Father, The Barkers, Soul, NomadLand and Tom Jerry.
        '''
        
        ticket_cost = 75
        ticket_cost_child = 50 
        ticket_senior_citizens= 60
        movies = ['Father', 'The Barkers', 'Soul', 'NomadLand', 'Tom Jerry']
        snack_name = ['Popcorn', 'Cheetos','Nachos','Mojito', 'Cola', 'Water']
        # for calculate the revenue of snack
        snack_with_price = Counter({'Popcorn':30,'Cheetos':25,'Nachos':20,'Mojito':10,'Cola':15,'Water':8}) 
        week_days =[]
        for day in range(1,8,1):
            #print(len(week_days))
            # Keep track of total revenue for the day
            total_revenue_day =0
            disc=0
            for screen in range (1,5,1):
                for each_screen in range (seats+1):
                    visitors_adults = random.choice(seats)
                    visitors_children= random.choice(seats-visitors_adults)
                    visitors_senior_citizens= random.choice(seats-(visitors_adults+visitors_children))

                    
                    
                    if visitors_adults > 0 and visitors_children > 0 and visitors_senior_citizens > 0:
                        snack_visitors_adults = np.random.choice(snack_name,visitors_adults)
                        snack_visitors_children = np.random.choice(snack_name,size=visitors_children)
                        snack_visitors_senior_citizens = np.random.choice(snack_name,size=visitors_senior_citizens)
                        pass
                    
                    elif visitors_adults > 0:
                            snack_visitors_adults = np.random.choice(snack_name,visitors_adults)

                            continue

                    elif visitors_children > 0:
                        snack_visitors_children = np.random.choice(snack_name,size=visitors_children)

                        continue
                        
                    else:
                        snack_visitors_senior_citizens = np.random.choice(snack_name,size=visitors_senior_citizens)

                        continue
                    
                    
                    total_snack = list(chain(snack_visitors_adults,snack_visitors_children,snack_visitors_senior_citizens))


                    # Calculate the revenue of snacks and sum the total:
                    # Count the snacks.
                    total_snack_count = Counter(total_snack)
                    # Multiplay the snacks count by the snacks price.
                    prud_total_snack_count = dict(Counter({k:snack_with_price[k]*total_snack_count[k] for k in snack_with_price}))
                    # For loop for insirt the revenue into list, then sum the values.
                    for k,v in prud_total_snack_count.items():
                        revenue_snack =  list(prud_total_snack_count.values())
                    revenue_snack = sum(revenue_snack) 


                        # Calculate revenue, and add to running total for the day For theater.
                    revenue_adults = visitors_adults * ticket_cost
                    revenue_children = visitors_children * ticket_cost_child

                        # 10% discount on senior citizen ticket costs on friday only.
                    if (day==6):
                        disc=ticket_senior_citizens*0.9
                        revenue_senior_citizens = disc * visitors_senior_citizens
                    else:
                        revenue_senior_citizens = visitors_senior_citizens * ticket_senior_citizens



                        # Sum all revenus for each screen.
                    revenue_screen = (revenue_adults + revenue_children + revenue_senior_citizens + revenue_snack) 


                        # Save total to the corresponding day for theater
            total_revenue_day = total_revenue_day + revenue_screen
            week_days.append(total_revenue_day)

                   

        
        return {'week_days': week_days, 'revenue_snack':revenue_snack, 'total_revenue_day':total_revenue_day} 
        
    
    def total_revenue(self):
        '''
        Return the total revenue in a week. 
        '''
        week_days = self.revenue()['week_days']
        return (f"The total revenue in a week is {week_days} SAR.")
    
    def max_day(self):
        '''
        Return the day with highest revenue in the week.
        '''
        week_days = self.revenue()['week_days'] # to take the result from revenue()
        max_d = max(week_days)
        count=1
            #should edti
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        for i in week_days:
            if ( i == max_d):
                count = count+1
        return (f"{days[count]} is the highest revenue day in the week with a total of {max_d} SAR.")
        
         
        
        
    def total_ticket(self):
        '''
        Return the total revenue of tickets in a week.
        '''
        revenue_snack = self.revenue()['revenue_snack'] # to take the result from revenue()
        total_revenue_day = self.revenue()['total_revenue_day'] # to take the result from revenue()
        
        # to subtract the total revenue day from snack revenue.
        sup_total_ticket = total_revenue_day - revenue_snack 
        return (f"The tickets revenue for the week is {sup_total_ticket} SAR.")   
    
    def total_snack(self):
        '''
        Return the total revenue of snacks in a week.
        '''
        revenue_snack = self.revenue()['revenue_snack']
        return (f"The snack revenue for the week is {revenue_snack} SAR.")
    
    def __repr__(self):
        return f"The number of seats and screens are {self.seats}, {self.screens}."