#Income
    # Rental Income = income

#Expenses
    # Taxes = taxes_are_theft 
    # Insurance = insurance_cost
    # Repairs and CapEx = capex_cost
    # Property Manager = manager_cost
    # Mortgage = mortgage_cost
    # Interest rate = interest_rate 
    # (Mortgage  * interest_rate) = mortgage_interest_cost
    
#Cash Flow
    # (Income - Expenses) = cash_flow

#Cash On Cash ROI
    # down_payment 
    # closing_cost
    # rehab_cost
    # misc_cost

#Total 
    # (cash_flow % total_investment) = cash_on_cash_roi %

#What the program needs 
    # Calculate ROI
    # Driver Code to allow users to choses what do to next 
    # User class 
    # Property class 
    # Property class store multiple expenses and incomes 
    # ROI stored for each Property 
    # Display ROI to user
    # Using regex and API's to get compare rental_income to median rent in Miami 


# OBJECTIVEP

#The premise of this assignment/program is to store multiple users who have 
# multiple properties associated with them.
# Within these properties the program needs to calculate what the ROI (return on investment is).
# In order to calculate the ROI we need the following information from the user.
# Property Expenses 
# Property Income 
# Investment (i.e. purchase price, closing costs)
# We use the above characteristics/variables to calculate ROI with this formula, ROI = (Net Profit / Total Investment) x 100



# CODE 

# So lets break down what we know above to code.
# Since we know we need to store multiple users, we might want to have a User class
# Since we know we need to store multipe properties, we might want to have a Property class


# But what would make up these classes? Lets start with User.
# The only characteristic/property we really NEED to store on our User class is the ability for a 
# user to have multiple properties
# So this we could store in our init()


#class User():

    #def __init__(self):
       # self.properties = []


# The above is really all we need but we could add more like a User's name. Are there any methods we 
# need on this user class? 
# Well we know that we need to store multiple properties for this specific user so maybe we put that 
# in our user class.


#class User():

   # def __init__(self, name):
       # self.properties = []
       # self.name = name

   # def add_properties(self):
        #this is where we could instantiate our Property objects and then add them to our list above! 
      #  pass


# The above is enough to get started with the User but what about our Propert class? 
# Well we know that we need to calculate ROI for our properties, and we have a couple different values that will help us
# do that: Expenses, Income, Investment. Welp if we need these guys to calculate ROI why don't we store them to our properties?


#class Property():

    #def __init__(self):
       # self.expenses = 0
       # self.income = 0
       # self.investments = 0
      #  self.roi = 0

# The above is a good start to what we might need to store on our properties to help us calculate & store our ROI.
# But how to we get there? How do we calculate our ROI. Well a couple methods might help us there or maybe just one method? That is 
# up to you. 


#class Property():

    #def __init__(self):
        #self.expenses = 0
       # self.income = 0
       # self.investments = 0
       # self.roi = 0


   # def calculate_roi(self):
        #this is where we need to gather information from our user in order to calculate our roi. We need to
        #what are expenses, income, investment is. This could either be a total # the user can give us. (i.e. what is the total annual income of your property)
        # Or we can ask them to be more specific(i.e. what type of income is this? rent/laundry/storage, and how much $ do you get from this income?)

        #then we use that information to run our calculation
        #self.roi = your_calculation

        #the above stores the roi on the class because we are using the self keyword. The only thing we need to do now
        #is display that # to the user!

       # pass 


#Well now we have a Property class that we can use to create multiple Property objects on & a User class that we can
#store properties to that User & create multiple different User objects. But how do we use all this code? Well we need a driver class or function.
#This seems like a good place to potentially store all of our users too!




#class ROI():

   # def __init__(self):
        #self.users = []
       # self.current_user = None


#Now we have a list so we can store multiple users and we can also keep track of who the current user is! But we need some
# "driver" code. This might be very similar to what we did with the Theater class. But obviously, ours does not need
# to be that complicated. 



#class ROI():

    #def __init__(self):
        #self.users = []
       # self.current_user = None



   # def run():

        #Here's where can display our options to our users of what they want to do with your program (i.e. add a user, 
        # change a user, add a property, quit etc)
        # itll look something like the below & should look familiar


       # response = input("What do you want to do?")

        #if response == 'add user':
              #well we need to instantiate our User object. And make sure if the init is taking in a paramater we
              #pass in the appropriate argument. We can also add that object to our self.user list & set the current_user
              #to THIS specific user object
              #pass

        #elif response == 'change user':
              # if you want the user to be able to change who is "logged in" what attribute on the User object might be 
              # helpful in identifying that specific user? Once we traverse through the user list & find that specific user 
              # we can then set the current_user to that object
             # pass

       # elif response == 'add property':
              #look at that we have a method in the User class for adding a property. How could we access that method on 
              #the current user that is "logged in"? 
             # pass


       # elif response == 'quit':
             #we know what to do here :) 
            # pass
        
class User:
    def __init__(self, name):
        self.properties = []
        self.name = name

    def add_properties(self, property):
        self.properties.append(property)

class Property:
    def __init__(self):
        self.expenses = 0
        self.income = 0
        self.investments = 0
        self.roi = 0

    def calculate_roi(self):
        if self.investments != 0:
            self.roi = ((self.income - self.expenses) / self.investments) * 100

class ROI:
    def __init__(self):
        self.users = []
        self.current_user = None

    def run(self):
        while True:
            response = input("What do you want to do? ('add user','change user','add property','quit'):")
            if response =='add user':
                name = input("What is user name?")
                user = User(name)
                self.users.append(user)
                self.current_user = user
                print(f"User'{name}'added.")
            elif response == 'change user':
                if self.users:
                    name = input("Enter user name to switch:")
                    for user in self.users:
                        if user.name == name:
                            self.current_user = user
                            print(f"Switched to user '{name}'.")
                            break
                    else:
                        print("User not found.")
                else:
                    print("No users available.")
            elif response == 'add property':
                if self.current_user:
                    property = Property()
                    property.expenses = int(input("Enter expenses: "))
                    property.income = int(input("Enter income: "))
                    property.investments = int(input("Enter investments: "))
                    property.calculate_roi()
                    self.current_user.add_properties(property)
                    print("Property added to your list!.")
                else:
                    print("Please select user!.")
            elif response == 'quit':
                break
            else:
                print("Try again.")
roi = ROI()


