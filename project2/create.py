import sys
#http://jsfiddle.net/7dg6uajL/9/light/

json_filename = 'all_cities_in_the_world.json'
json_file = open(json_filename, 'w')

current_country = ''
current_region = ''

def start(name):
	json_file.write('{"name":"' + name + '","children":[')
def end():
	json_file.write(']}')

start('Earth')

with open('all_cities_in_the_world.csv') as data_file:
	firstline = True
	for line in data_file:
		if line.count(',') != 2:
			continue
		country, region, city = line.split(',')
		if firstline:
			start(country)
			start(region)
			current_country = country
			current_region = region
			firstline = False
		else:
			if country == current_country and region == current_region:
				continue
			if country != current_country:
				end()
				end()
				json_file.write(',')
				start(country)
				current_country = country
				start(region)
			elif region != current_region:
				end()
				json_file.write(',')
				start(region)
				current_region = region

end()
end()
end()