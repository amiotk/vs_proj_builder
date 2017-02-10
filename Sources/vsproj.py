from bs4 import BeautifulSoup as Soup

# Import an xml structure from a file and return it back as an xml soup.
def Open(filename):
	handler = open(filename).read()
	soup = Soup(handler, "xml")

	return soup

# Scans through the xml soup structure and remove existing C/C++ source and 
# header files.
def Purge(file):
	# Remove source files paths
	for tag in file.findAll("ClCompile"):
		if(tag.get("Include")):
			print "Removing " + tag["Include"]
			tag.decompose()

	# Remove include files paths
	for tag in file.findAll("ClInclude"):
		if(tag.get("Include")):
			print "Removing " + tag["Include"]
			tag.decompose()

	# Removing empty groups
	for tag in file.findAll("ItemGroup"):
		if not tag.childs and not tag.attrs:
			print "Removing an empty ItemGroup"
			tag.decompose()

# Adds new files paths to the xml structure.
def Append_group(file, filepaths):
	print "TODO: Append_group()"

	# Make a new ItemGroup
	group = file.new_tag("ItemGroup")
	
	source = file.new_tag("ClInclude")
	source["Include"] = "asdq"
	group.append(source)
	file.Project.append(group)

# Saves the xml soup structure to a file.
def Save(file, filename):
	handler = open(filename, "w")
	handler.write(file.prettify())
	handler.close()
