import sys


json_filename = 'all_cities_in_the_world.json'
json_file = open(json_filename, 'a')

current_country = ''
current_region = ''
current_city = ''

def start_new(name):
	json_file.write('{"name":"' + name + '","children":[')
def end():
	json_file.write(']},')

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
			if region != current_region:
				end()
				start_new(region)
			if country != current_country:
				end()
				start_new(country)
#end()
end()
end()
end()