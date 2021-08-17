weight_value_list = [1, 1000, 0.001, 1000000, 1016046.08, 907184, 28.3495]
weight_list = ["grams", "kilograms", "milligrams", "metric ton", "long ton", "short ton", "ounce"]
temp_list = ["celsius", "fahrenheit", "kelvin"]
length_list = ["metre", "kilometre", "centimetre", "millimetre", "mile", "yard", "foot", "inch"]
lenth_value_list = [1, 1000, 0.01, 0.001, 1609.35, 0.9144, 0.3048, 0.024]

#Function for converting temperature
def convert_temp(temp_list):
    unit_temp = input("What unit would you like to convert from?")
    if unit_temp in temp_list:
        num_temp = float(input("How many degrees {} would you like to convert".format(unit_temp)))
        des_unit_temp = str(input("What unit would you like to convert to?"))
        if des_unit_temp in temp_list:
            if unit_temp == "celsius" and des_unit_temp == "fahrenheit":
                ans_temp = 1.8 * unit_temp + 32
            elif unit_temp == "celsius" and des_unit_temp == "kelvin":
                ans_temp = unit_temp + 273.15
            elif unit_temp == "fahrenheit" and des_unit_temp == "celsius":
                ans_temp = (num_temp - 32) / 1.8
            elif unit_temp == "fahrenheit" and des_unit_temp =="kelvin":
                ans_temp = (num_temp - 32) / 1.8 + 273.15
            elif unit_temp == "kelvin" and des_unit_temp == "celsius":
                ans_temp = num_temp - 273.15
            elif unit_temp == "kelvin" and des_unit_temp == "fahrenheit":
                ans_temp = (num_temp - 273.15) * 1.8 + 32
            else:
                print("Please enter two different valid temperature units")
        else:
            print("Please enter a valid temperature unit")
    else:
        print("Please enter a valid temperature unit")
    return ans_temp

convert_temp(temp_list)




