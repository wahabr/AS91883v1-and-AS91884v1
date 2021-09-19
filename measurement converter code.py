weight_value_list = [1, 1000, 0.001, 1000000, 1016046.08, 907184, 28.3495]
weight_list = ["grams", "kilograms", "milligrams", "metric tons", "long tons", "short tons", "ounces"]
temp_list = ["celsius", "fahrenheit", "kelvin"]
length_list = ["metres", "kilometres", "centimetres", "millimetres", "miles", "yards", "feet", "inches"]
length_value_list = [1, 1000, 0.01, 0.001, 1609.35, 0.9144, 0.3048, 0.0254]


# Function for testing a float
def test_float(num_unit):
    try:
        float(num_unit)
        return True
    except ValueError:
        return False


# Function for converting temperature
def convert_temp(temp_list):
    global unit_temp
    print("These are your options: {}".format(temp_list))
    a = False
    while a is False:
        unit_temp = input("What unit would you like to convert from?").strip().lower()
        if unit_temp in temp_list:
            a = True
        else:
            print("Please enter a valid temperature unit")
    a = False
    while a is False:
        num_temp = input("How many degrees {} would you like to convert?".format(unit_temp))
        a = test_float(num_temp)
        if a is False:
            print("Please enter a valid numerical response")
    print("These are your options: {}".format(temp_list))
    a = False
    while a is False:
        des_unit_temp = (input("What unit would you like to convert to?")).strip().lower()
        if des_unit_temp in temp_list:
            a = True
        else:
            print("Please enter a valid temperature unit")
    if unit_temp == "celsius" and des_unit_temp == "fahrenheit":
        ans_temp = 1.8 * float(num_temp) + 32
        print("Original Measurement Units:{}\nConverted Measurement Units:{}\nOriginal Measurement:{} {}\nConverted Measurement:{} {}".format(unit_temp, des_unit_temp, num_temp, unit_temp, ans_temp, des_unit_temp))
    elif unit_temp == "celsius" and des_unit_temp == "kelvin":
        ans_temp = float(num_temp) + 273.15
        print("Original Measurement Units:{}\nConverted Measurement Units:{}\nOriginal Measurement:{} {}\nConverted Measurement:{} {}".format(unit_temp, des_unit_temp, num_temp, unit_temp, ans_temp, des_unit_temp))
    elif unit_temp == "fahrenheit" and des_unit_temp == "celsius":
        ans_temp = (float(num_temp) - 32) / 1.8
        print("Original Measurement Units:{}\nConverted Measurement Units:{}\nOriginal Measurement:{} {}\nConverted Measurement:{} {}".format(unit_temp, des_unit_temp, num_temp, unit_temp, ans_temp, des_unit_temp))
    elif unit_temp == "fahrenheit" and des_unit_temp == "kelvin":
        ans_temp = (float(num_temp) - 32) / 1.8 + 273.15
        print("Original Measurement Units:{}\nConverted Measurement Units:{}\nOriginal Measurement:{} {}\nConverted Measurement:{} {}".format(unit_temp, des_unit_temp, num_temp, unit_temp, ans_temp, des_unit_temp))
    elif unit_temp == "kelvin" and des_unit_temp == "celsius":
        ans_temp = float(num_temp) - 273.15
        print("Original Measurement Units:{}\nConverted Measurement Units:{}\nOriginal Measurement:{} {}\nConverted Measurement:{} {}".format(unit_temp, des_unit_temp, num_temp, unit_temp, ans_temp, des_unit_temp))
    elif unit_temp == "kelvin" and des_unit_temp == "fahrenheit":
        ans_temp = (float(num_temp) - 273.15) * 1.8 + 32
        print("Original Measurement Units:{}\nConverted Measurement Units:{}\nOriginal Measurement:{} {}\nConverted Measurement:{} {}".format(unit_temp, des_unit_temp, num_temp, unit_temp, ans_temp, des_unit_temp))
    else:
        print("Please enter two different valid temperature units")



# Function for converting weight
def convert_weight(weight_list, weight_value_list):
    print("These are your options: {}".format(weight_list))
    a = False
    while a is False:
        unit_weight = input("What unit would you like to convert from?").strip().lower()
        if unit_weight in weight_list:
            a = True
        else:
            print("Please enter a valid weight unit")
    a = False
    while a is False:
        num_weight = input("How many {} would you like to convert?".format(unit_weight))
        a = test_float(num_weight)
        if a is False:
            print("Please enter a valid numerical response")
    print("These are your options: {}".format(weight_list))
    a = False
    while a is False:
        des_unit_weight = input("What unit would you like to convert to?").strip().lower()
        if des_unit_weight in weight_list:
            a = True
        else:
            print("Please enter a valid weight unit")
    pos_weight = weight_list.index(unit_weight)
    weight_value = weight_value_list[pos_weight]
    value_in_grams = float(num_weight) * weight_value
    pos_des_weight = weight_list.index(des_unit_weight)
    des_weight_value = weight_value_list[pos_des_weight]
    ans_weight = value_in_grams / des_weight_value
    print("Original Measurement Units:{}\nConverted Measurement Units:{}\nOriginal Measurement:{} {}\nConverted Measurement:{} {}".format(unit_weight, des_unit_weight, num_weight, unit_weight, ans_weight, des_unit_weight))



# Function for converting length
def convert_length(length_list, length_value_list):
    print("These are your options: {}".format(length_list))
    a = False
    while a is False:
        unit_length = input("What unit would you like to convert from?").strip().lower()
        if unit_length in length_list:
            a = True
        else:
            print("Please enter a valid length unit")
    a = False
    while a is False:
        num_length = input("How many {} would you like to convert?".format(unit_length))
        a = test_float(num_length)
        if a is False:
            print("Please enter a valid numerical response")
    print("These are your options: {}".format(length_list))
    a = False
    while a is False:
        des_unit_length = input("What unit would you like to convert to?").strip().lower()
        if des_unit_length in length_list:
            a = True
        else:
            print("Please enter a valid length unit")
    pos_length = length_list.index(unit_length)
    length_value = length_value_list[pos_length]
    value_in_metres = float(num_length) * length_value
    pos_des_length = length_list.index(des_unit_length)
    des_length_value = length_value_list[pos_des_length]
    ans_length = value_in_metres / des_length_value
    print("Original Measurement Units:{}\nConverted Measurement Units:{}\nOriginal Measurement:{} {}\nConverted Measurement:{} {}".format(unit_length, des_unit_length, num_length, unit_length, ans_length, des_unit_length))


a = False
while a is False:
    convert = input("Would you like to convert a measurement? ").strip().lower()
    if convert == "yes" or convert == "no":
        a = True
    else:
        print("Please enter yes or no")
if convert == "yes":
    a = False
    while a is False:
        unit = input("Would you like to convert length, weight, or temperature? ").strip().lower()
        if unit == "length" or unit == "temperature" or unit == "weight":
            a = True
        else:
            print("Please enter length, temperature, or weight")
    if unit == "weight":
        convert_weight(weight_list, weight_value_list)
    elif unit == "length":
        convert_length(length_list, length_value_list)
    else:
        convert_temp(temp_list)
else:
    print("Okay. Have a nice day!")
