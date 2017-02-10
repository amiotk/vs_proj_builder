from bs4 import BeautifulSoup as Soup

# Import an xml structure from a file and return it back as an xml soup.
def Open(filename):
	handler = open(filename).read()
	soup = Soup(handler, "xml")

	return soup

# Scans through the xml soup structure and remove existing source and 
# header files.
def Purge(file):
	# Remove source files tags
	tags = ["ClCompile", "ClInclude", "None", "Text"]
	for tag in tags:
		for t in file.findAll(tag):
			if(t.get("Include")):
				print "Removing " + t["Include"]
				t.decompose()

	# Removing empty groups
	for t in file.findAll("ItemGroup"):
		if not t.childs and not tag.attrs:
			print "Removing an empty ItemGroup"
			t.decompose()

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
