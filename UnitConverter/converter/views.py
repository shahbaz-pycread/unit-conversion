from django.shortcuts import render

# Create your views here.

def convert_length(value, from_unit, to_unit):
	length_units = {
	"meters" : 1,
	"kilometers" : 0.001,
	'miles': 0.000621371,
    'centimeters': 100,
    'inches': 39.3701,
    'feet': 3.28084
}
	return value * length_units[to_unit] / length_units[from_unit]

def convert_weight(value, from_unit, to_unit):
	weight_units = {
	'grams' : 1,
	'kilograms' : 0.001,
	'pounds': 0.00220462,
    'ounces': 0.035274
	}
	return value * weight_units[to_unit] / weight_units[from_unit]

def convert_temperature(value, from_unit, to_unit):
	if from_unit == 'celsius' and to_unit == 'fahrenheit':
		return(value * 9/5) + 32

	if from_unit == 'fahrenheit' and to_unit == 'celsius':
		return (value - 32) * 5/9
	return value


# Main View Function

def unit_converter(request):
	converted_value = None
	to_unit = None
	if request.method == 'POST':
		value = float(request.POST['value'])
		unit_type = request.POST['unit_type']
		from_unit = request.POST['from_unit']
		to_unit = request.POST['to_unit']


		if unit_type == 'length':
			converted_value = convert_length(value, from_unit, to_unit)
		elif unit_type == 'weight':
			converted_value = convert_weight(value, from_unit, to_unit)
		elif unit_type == 'temperature':
			converted_value = convert_temperature(value, from_unit, to_unit)


		

	return render(request, 'converter/unit_converter.html',{'converted_value': converted_value, 'to_unit': to_unit})