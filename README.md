# Tax Bracket Calculator

This calculator computes the amount of taxes that needs to be paid, based on the given amount of money.\
The bracket will be determined by a JSON file containing multiple arrays, representing a tax bracket. \
The structure of one bracket is: [begin, end, percent]. begin and end are inclusive, pecent is in decimal form\

USAGE: python TaxBracketCalculator.py [amount of money] [path to tax bracket json]\
RETURNS: The amount of taxes for [user inputted money] is [calculated tax]
