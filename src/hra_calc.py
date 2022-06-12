# HRA Calculator 
# Author : Embedded Bro


# MIT License
# 
# Copyright (c) 2022 EmbeddedBro
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Global Variables
annual_hra_received = 0
annual_basic_salary = 0
annual_dearness_allowance = 0
annual_actual_rent_paid = 0
is_it_metro_city = 0
city_type_multiplier = 0

def get_inputs():
    print("Please enter required details :: \n")
    
    global annual_hra_received, annual_basic_salary, annual_dearness_allowance, annual_actual_rent_paid, is_it_metro_city

    annual_hra_received         = input("Enter annual HRA received       :: ")
    annual_basic_salary         = input("Enter annual Basic Salary       :: ")
    annual_dearness_allowance   = input("Enter annual dearness allowance :: ")
    annual_actual_rent_paid     = input("Enter annual actual rent paid   :: ")
    is_it_metro_city            = input("\nDo you live metro cities like \nMumbai, Delhi, Kolkata or Chennai ? \nPlease enter Yes or No :: ")
    check_for_valid_response()
    

def check_for_valid_response():
    global is_it_metro_city, city_type_multiplier

    while True:
        if is_it_metro_city in ["yes", "Yes", "YES", "Y", "y"]:
            city_type_multiplier = 0.5
            break
        elif is_it_metro_city in ["no", "No", "NO", "N", "n"]:
            city_type_multiplier = 0.4
            break
        else:
            print("\nInvalid response !\n")
            is_it_metro_city = input("\nPlease enter response again, Yes or No :: ")

def hra_calc():
    global annual_basic_salary, annual_dearness_allowance, city_type_multiplier, annual_actual_rent_paid, annual_hra_received

    # Component 1
    final_annual_basic_salary_and_DA_component = (float(annual_basic_salary) + float(annual_dearness_allowance)) * city_type_multiplier        
    # Component 2
    considered_annual_rent_paid = float(annual_actual_rent_paid) - ((float(annual_basic_salary) + float(annual_dearness_allowance)) * 0.1)
    calculated_hra = min(float(annual_hra_received), considered_annual_rent_paid, final_annual_basic_salary_and_DA_component)
    
    return calculated_hra

def main():
    print("\n ********** HRA Calculator ********** \n ")
    get_inputs()    
    calculated_hra = hra_calc()
    print("\nTOTAL EXEMPTED HRA :: %.2f \n" % calculated_hra )   

if __name__== '__main__':
    main()