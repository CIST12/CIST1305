MARK_UP = 2.5

# The main function
def main():
    another = 'y'
    # process one or more items
    while another == 'y' or another == 'Y':
        # display an item's retail price
    show_retail()

        # do this again?
    another = input('do you have another items? ' + '(enter y for yes): ')

# the show_retail function gets an items wholesale
# cost and displays the item's retail price
def show_retail():
    # get the item's wholesale cost.
    wholesale = float(input("enter the item's wholesale cost: "))
    # validate the wholesale cost
    while wholesale < 0:
        print('error: the cost cannot be negetive.')
        wholesale = float(input('enter the correct wholesale cost: '))

        # calculate the retail price
    retail = wholesale * MARK_UP
        # display the retail price
    print(" the retail price is $", format(retail, '.2f'))


    # call the main function.


main()




