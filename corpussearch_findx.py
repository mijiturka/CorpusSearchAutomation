# Aggregates corpus search results into a single file (result.csv) prefixed by year
# Finds the number of x's and prints out the file it found them in
# Uncomment the lines for Windows

# Filename prefices for a single year or year range should be in one of the following formats:
# YYYYfilename, YYYY_YYYYfilename

import glob, re, operator

#queries_folder = "icepahc-v0.9\\queries\\"		#Windows
queries_folder = "MCVF_parsed/queries/"		
result_file = "result.csv"
token_searched = "x"

read_files = glob.glob(queries_folder + "*.cod.ooo")
read_files.sort()

num_x = 0
counts = {}
total_tokens = {}

print("Occurrences of " + token_searched + ":")

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
	
					#update token counts for this year
					token = line
					if (year_prefix, token) in counts:
						counts[year_prefix, token] += 1
					else:
						counts[year_prefix, token] = 1

					#update total number of tokens for this year
					if year_prefix in total_tokens: 
						total_tokens[year_prefix] += 1
					else:
						total_tokens[year_prefix] = 1

					line = year_prefix + ", " + line
					outfile.write(line+"\n")
print("\n")

print("Total number of occurrences of " + token_searched + ":")
print(num_x)
print("\n")
	
print("Total number of tokens per year:")
print(total_tokens)
print("\n")

print("Year, token, count, as percent of tokens for this year:")
counts_sorted = sorted(counts.items(), key=lambda x: (x[0][1], x[0][0]))
for year_token in counts_sorted:
	token_percent = float(year_token[1])/total_tokens[year_token[0][0]] *100
	print(str(year_token) + ", " + str(token_percent))
	
