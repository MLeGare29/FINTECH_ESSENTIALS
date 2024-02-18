# FROM SCRIPTING TO SOFTWARE DEVELOPMENT
# In this lesson, you'll learn how people create software applications in the FinTech industry.
# Th


# IDENTIFYING BUSINESS NEEDS AND BUSINESS REQUIREMENTS
# Say your manager wants you to create a new piece of software that converts Bitcoin to Dollars
# In order to do this you'll need to step back and consider questions that will arise with this task
# This involves considerations known as the following:
# BUSINESS REQUIREMENTS or SOFTWARE APPLICATION REQUIREMENTS
# These requirements specify how to build a program to meet the business need-which is the reason the company is paying you to build software

# First, you must understand the purpose that this app is intended to serve users
# Second, you must understand how it should function properly to meet that need

# KEY QUESTIONS:
# 1. What kinds of dollars do I need to consider?
# 2. Do I need to get that current dollar-to-Bitcoin conversion or the conversion rate for the last 10 days?
# 3. What exhcange will be my reference?
# 4. Do I need to offer users the option to buy Bitcoin after computing the conversion rate?

# THE USER STORY
# "As a [subject], I want to [pursue an action], so that [a desired outcome results]."
# As a Finance Manager, I want to convert USD to BTC so that I can know the current value in BTC of the dollars in my wallet

# REAL LIFE USER STORY EXAMPLE:
# As a Culture Curator, I want to target and neutralize bot accounts so that I can get accurate metrics of my reach and weed out the clutter for a more enjoyable experience.

# ACCEPTANCE CRITERIA:
# Consists of conditions that are needed to satisfy a user need
# "Given [some context], when [some action is taken], then [a particaular set of observable outcomes]"
# "Given that I want to convert USD to BTC, when I set a negative amount of USD to convert, then the application should raise an error and ask the user to introduce a positive amount of USD."

# CONVERT THE USER STORY INTO CODE
# "As a lender, I want to filter the bank list by comparing 
# the maximum loan size of the bank so that I know which banks
# offer the loan amount that the customer requested."
# The first function will signify the max loan the banks can offer
# This will be filter_max_loan_size
# The next function will determine which banks offer the amount the customer requested
# This will be loan_size_approval_list

def filter_max_loan_size(loan_amount, bank_list):
    loan_size_approval_list = []

    for bank in bank_list:
        if loan_amount <= int(bank[1]):
            loan_size_approval_list.append(bank)
    return loan_size_approval_list