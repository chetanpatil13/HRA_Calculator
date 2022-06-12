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


class hra_calculator:
    def __init__(self):
        self.annual_hra_received = 0
        self.annual_basic_salary = 0
        self.annual_dearness_allowance = 0
        self.annual_actual_rent_paid = 0
        self.is_it_metro_city = 0
        self.city_type_multiplier = 0
        
    def get_inputs(self):
        print("Please enter required details :: \n")        
        self.annual_hra_received         = input("Enter annual HRA received       :: ")
        self.annual_basic_salary         = input("Enter annual Basic Salary       :: ")
        self.annual_dearness_allowance   = input("Enter annual dearness allowance :: ")
        self.annual_actual_rent_paid     = input("Enter annual actual rent paid   :: ")
        self.is_it_metro_city            = input("\nDo you live metro cities like \nMumbai, Delhi, Kolkata or Chennai ? \nPlease enter Yes or No :: ")
        self.check_for_valid_response()
    

    def check_for_valid_response(self):
        
        while True:
            if self.is_it_metro_city in ["yes", "Yes", "YES", "Y", "y"]:
                self.city_type_multiplier = 0.5
                break
            elif self.is_it_metro_city in ["no", "No", "NO", "N", "n"]:
                self.city_type_multiplier = 0.4
                break
            else:
                print("\nInvalid response !\n")
                self.is_it_metro_city = input("\nPlease enter response again, Yes or No :: ")

    def hra_calc(self):
        # Component 1
        final_annual_basic_salary_and_DA_component = (float(self.annual_basic_salary) + float(self.annual_dearness_allowance)) * self.city_type_multiplier        
        # Component 2
        considered_annual_rent_paid = float(self.annual_actual_rent_paid) - ((float(self.annual_basic_salary) + float(self.annual_dearness_allowance)) * 0.1)
        calculated_hra = min(float(self.annual_hra_received), considered_annual_rent_paid, final_annual_basic_salary_and_DA_component)
    
        return calculated_hra


def main():
    print("\n ********** HRA Calculator ********** \n ")

    # Object Instantiation
    hra_calc = hra_calculator()
    hra_calc.get_inputs()    
    calculated_hra = hra_calc.hra_calc()
    print("\nTOTAL EXEMPTED HRA :: %.2f \n" % calculated_hra )

if __name__== '__main__':
    main()