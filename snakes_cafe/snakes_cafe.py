def welcome():
  welcome_message = ''' 
  python snakes_cafe.py
  **************************************
  **    Welcome to the Snakes Cafe!   **
  **    Please see our menu below.    **
  **
  ** To quit at any time, type "quit" **
  **************************************

  Appetizers
  ----------
  Wings
  Cookies
  Spring Rolls

  Entrees
  -------
  Salmon
  Steak
  Meat Tornado
  A Literal Garden

  Desserts
  --------
  Ice Cream
  Cake
  Pie

  Drinks
  ------
  Coffee
  Tea
  Unicorn Tears

  ***********************************
  ** What would you like to order? **
  ***********************************
  '''

  print(f'{welcome_message}')

# menuOptions = ['Wings', 'Cookies', 'Spring Rolls', 'Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden', 'Icea Cream', 'Cake', 'Pie', 'Coffee', 'Tea', 'Unicorn Tears']

if __name__=='__main__':
  welcome()
  ordered_request = input('> ')
  count = 0
  order = []
  # while ordered_request != 'quit':

  
