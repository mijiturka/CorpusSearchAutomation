# Aggregates corpus search results into a single file (result.csv) prefixed by year
# Finds the number of x's and prints out the file it found them in
# Uncomment the lines for Windows

import glob

#read_files = glob.glob("icepahc-v0.9\\queries\\*.cod.ooo")		#Windows
read_files = glob.glob("icepahc-v0.9/queries/*.cod.ooo")
read_files.sort()
num_x = 0
with open("result.csv", "wb") as outfile:
	for file in read_files:
		#filename = file.split("\\")[-1]		#Windows
		filename = file.split("/")[-1]
		year = filename[0:4]
		if year.isdigit():
			with open(file, "rb") as infile:
				inf = infile.readlines()
				for line in inf:
					line = year + ", " + line
					if line.find("x") > -1:
						num_x = num_x+1
						print(filename + "-" + line)
					outfile.write(line)
print(num_x)

