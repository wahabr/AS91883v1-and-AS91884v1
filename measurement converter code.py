weight_value_list = [1, 1000, 0.001, 1000000, 1016046.08, 907184, 28.3495]
weight_list = ["grams", "kilograms", "milligrams", "metric tons", "long tons", "short tons", "ounces"]
temp_list = ["celsius", "fahrenheit", "kelvin"]
length_list = ["metres", "kilometres", "centimetres", "millimetres", "miles", "yards", "feet", "inches"]
length_value_list = [1, 1000, 0.01, 0.001, 1609.35, 0.9144, 0.3048, 0.024]

#Function for converting temperature
def convert_temp(temp_list):
    unit_temp = input("What unit would you like to convert from?")
    if unit_temp in temp_list:
        num_temp = float(input("How many degrees {} would you like to convert?".format(unit_temp)))
        des_unit_temp = str(input("What unit would you like to convert to?"))
        if des_unit_temp in temp_list:
            if unit_temp == "celsius" and des_unit_temp == "fahrenheit":
                ans_temp = 1.8 * num_temp + 32
            elif unit_temp == "celsius" and des_unit_temp == "kelvin":
                ans_temp = num_temp + 273.15
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


#Function for converting weight
def convert_weight(weight_list, weight_value_list):
    unit_weight = input("What unit would you like to convert from?")
    if unit_weight in weight_list:
        num_weight = input("How many {} would you like to convert?".format(unit_weight))
        des_unit_weight = input("What unit would you like to convert to?")
        if des_unit_weight in weight_list:
            pos_weight = weight_list.index(unit_weight)
            weight_value = weight_value_list(pos_weight)
            value_in_grams = num_weight * weight_value
            pos_des_weight = weight_list.index(des_unit_weight)
            des_weight_value = weight_value_list(pos_des_weight)
            ans_weight = des_weight_value * num_weight
        else:
            print("Please enter a valid weight unit")
    else:
        print("Please enter a valid weight unit")

#Function for converting length
def convert_length(length_list,length_value_list):
    unit_length = input("What unit would you like to convert from?")
    if unit_length in length_list:
        num_length = input("How many {} would you like to convert?".format(unit_length))
        des_unit_length = input("What unit would you like to convert to?")
        if des_unit_length in weight_list:
            pos_length = length_list.index(unit_length)
            length_value = length_value_list(pos_length)
            value_in_metres = num_length * length_value
            pos_des_length = length_list.index(des_unit_length)
            des_length_value = length_value_list(pos_des_length)
            ans_weight = des_length_value * num_length
        else:
            print("Please enter a valid length unit")
    else:
        print("Please enter a valid length unit")


convert = input("Would you like to convert a measurement")
if convert == "yes":
    unit = input("Would you like to convert length, weight, or temperature?")
    if unit == "weight":
        convert_weight(weight_list,weight_value_list)
    elif unit == "length":
        convert_length(length_list, length_value_list)
    elif unit == "temperature":
        convert_temp(temp_list)
    else:
        print("Please enter length, temperature, or weight")
elif convert == "no":
    print("Okay. Have a nice day!")
else:
    print("Please enter yes or no")
