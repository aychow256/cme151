import sys
#http://jsfiddle.net/7dg6uajL/9/light/

json_filename = 'all_cities_in_the_world.json'
json_file = open(json_filename, 'w')

current_country = ''
current_region = ''
current_city = ''

def start_new(name):
	json_file.write('{"name":"' + name + '","children":[')
def end():
	json_file.write(']}')

start_new('Earth')

with open('all_cities_in_the_world.csv') as data_file:
	firstline = True
	for line in data_file:
		if line.count(',') != 2:
			continue
		country, region, city = line.split(',')
		if country != 'United States of America':
			continue
		if firstline:
			start_new(country)
			start_new(region)
			#start_new(city)
			firstline = False
		else:
			#if city != current_city:
			#	end()
			#	start_new(city)
			if region == current_region and country == current_country:
				continue
			if region != current_region:
				end()
				json_file.write(',')
				start_new(region)
				current_region = region
			if country != current_country:
				end()
				json_file.write(',')
				start_new(country)
				current_country = country

#end()
end()
end()
end()