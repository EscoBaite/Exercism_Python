"""Functions for calculating steps in exchaning currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate):
    """Function to estimate value after exchange.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    
    Function that takes the ammount of money you are planning to exchange
    and the unit value of the foreign currency and returns the exchanged value 
    of the foreign currency you will recieve.
    """
    return budget / exchange_rate
    pass


def get_change(budget, exchanging_value):
    """Function to get the remaining money from the budget.

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    
    Function that takes the ammount of money available and the ammount 
    of money you want to exchange now and returns the remainig ammount.
    """
    return budget - exchanging_value
    pass


def get_value_of_bills(denomination, number_of_bills):
    """Function to get the total value of the bills given.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    
    Function that takes the value of a bill and the total number of bills
    and returns the total value of the bills given.
    """
    return int(denomination * number_of_bills)
    pass


def get_number_of_bills(budget, denomination):
    """Function to get the number of currecy bills that you can recieve 
    within the given ammount.

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    
    Function that takes the total starting value of the currency and the value
    of a single bill of the currency and returns the total number of whole bills
    of currency that fit the starting ammount.
    """
    return budget // denomination
    pass


def get_leftover_of_bills(budget, denomination):
    """Function to calculate what is leftover after exchanging into bills.

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    
    Function that takes the total starting value and the denomination of a single bill
    and returns the leftover ammount that cannot be returned from your starting ammount.
    """
    return budget % denomination
    pass


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Function to calculate the exchangable value.

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    
    Function that takes the total budget, the exchange rate, the spread,
    and denomination and returns the total exchangable value.
    """
    
    actual_exchange_rate = exchange_rate + (exchange_rate * (spread / 100))
    total_ammount = exchange_money(budget, actual_exchange_rate)
    total_value = get_number_of_bills(total_ammount, denomination)
    return int(total_value * denomination)
    pass