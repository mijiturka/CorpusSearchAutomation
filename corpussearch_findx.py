# Aggregates corpus search results into a single file (result.csv) prefixed by year
# Finds the number of x's and prints out the file it found them in
# Uncomment the lines for Windows

# Filename prefices for a single year or year range should be in one of the following formats:
# YYYYfilename, YYYY_YYYYfilename

import glob, re

#queries_folder = "icepahc-v0.9\\queries\\"		#Windows
queries_folder = "icepahc-v0.9/queries/"		
result_file = "result.csv"

read_files = glob.glob(queries_folder + "*.cod.ooo")
read_files.sort()

num_x = 0

with open(result_file, "wb") as outfile:
	for file in read_files:
		#filename = file.split("\\")[-1]		#Windows
		filename = file.split("/")[-1]
		file_isdata = False

		years = re.match(r"([0-9][0-9][0-9][0-9])_([0-9][0-9][0-9][0-9])", filename)
		if (years):
			year1 = years.group(1)
			year2 = years.group(2)
			year_prefix = year1 + ", " + year2
			file_isdata = True
		else:
			year_prefix = filename[0:4]
			if (year_prefix.isdigit()):
				file_isdata = True

		if file_isdata:
			with open(file, "rb") as infile:
				inf = infile.readlines()
				for line in inf:
					line = line.strip()
					
					#line contains x
					#if line.find("x") > -1:

					#line matches x
					if line == "x":
						num_x = num_x+1
						print(year_prefix + ", " + line + ", " + filename)

					line = year_prefix + ", " + line
					outfile.write(line+"\n")
print(num_x)

