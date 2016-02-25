# Aggregates corpus search results into a single file (result.csv) prefixed by year.
# Prints out:
# 	number of x's and file it found them in.
# 	total tokens per year
# 	token counts per year, with percentage of all tokens from this year

# Filename prefices for a single year or year range should be in one of the following formats:
# 	YYYYfilename, or YYYY_YYYYfilename
# You can have several files for the same year.

# Will look through any file in this folder with this extension
corpus_folder = "MCVF_parsed"
queries_folder = "queries"
query_file_extension = ".cod.ooo"

result_file = "result.csv"
token_searched = "x"
regression_file = "regression.csv"
do_regression = True


import glob, re, os

num_x = 0
counts = {}
total_tokens = {}

query_files = os.path.join(corpus_folder, queries_folder, '*'+query_file_extension)
read_files = glob.glob(query_files)
read_files.sort()

print("Occurrences of " + token_searched + ":")

with open(result_file, "wb") as outfile:
	for file in read_files:
		filename = os.path.basename(file)

		years = re.match(r"([0-9][0-9][0-9][0-9])_([0-9][0-9][0-9][0-9])", filename)
		if (years):
			year1 = years.group(1)
			year2 = years.group(2)
			year_prefix = year1 + ", " + year2
		else:
			year_prefix = filename[0:4]

		with open(file, "rb") as infile:
			inf = infile.readlines()
			for line in inf:
				line = line.strip()
				
				#line contains x
				#if line.find("x") > -1:

				#line matches x
				if line == token_searched:
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
counts_sorted = sorted(counts.items(), key=lambda i: (i[0][1], i[0][0]))
tokens = []
for ((year, token), count) in counts_sorted:
	tokens.append(token)
	token_percent = float(count)/total_tokens[year] *100
	info = [year, token, count, token_percent]
	info_string = ", ".join(str(i) for i in info)
	print(info_string)
tokens = set(tokens)

if do_regression:
	for curr_token in tokens:
		ext_id = regression_file.find('.csv')
		curr_file = regression_file[:ext_id] + "_" + curr_token + regression_file[ext_id:]
		with open(curr_file, "wb") as outfile:
			outfile.write("year, token, count\n")
			for ((year, token), count) in counts_sorted:
				for i in range (0, count):
					if token == curr_token:
						line = year + ", 1"
					else:
						line = year + ", 0"
					outfile.write(line+"\n")
