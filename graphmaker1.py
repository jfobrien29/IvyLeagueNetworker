# graphMaker1.py

import csv

athletesFile = 'all_athletes_final.csv'
# Athletes Stored as:
# [0] = name
# [1] = school
# [2] = sport
# [3] = HS
# [4] = Town
# [5] = State

# Main storage of athletes
# Each athlete has a set of edges
athleteDict = {}
athleteDuplicates = {}

# Edges
teamDict = {}
schoolDict = {}

with open(athletesFile, 'rU') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	for row in csvreader:

		name = row[0] + " (" + row[1] + ")"
		# Add athletes to dictionary
		athleteDict[name] = []

		# Add all teams to the teamDict
		if (row[1] + "_" + row[2]) not in teamDict:
			teamDict[(row[1] + "_" + row[2])] = [name]
		else:
			teamDict[(row[1] + "_" + row[2])].append(name)

		# Add all schools to the schoolDict
		if row[3] not in schoolDict:
			schoolDict[row[3]] = [name]
		else:
			schoolDict[row[3]].append(name)

# First connect teams
for team, teamList in teamDict.items():
	for i in range(0, len(teamList)):
		for j in range(0, len(teamList)):
			if i is not j:
				athleteDict[teamList[i]].append([teamList[j],team,"T"])

# Now connect Highschools
for hs, hsList in schoolDict.items():
	for i in range(0, len(hsList)):
		for j in range(0, len(hsList)):
			if i is not j:
				athleteDict[hsList[i]].append([hsList[j],hs,"HS"])

def bfs_path(start, end):
	finish = False

	# Keep track of previous connection
	lastConnection = {}
	lastConnection[start] = "None"

	# Keep track of visited
	visited = []

	# Keep track of queue
	queue = [start]

	# Final Path
	path = []

	while len(queue) > 0:

		# Pop vertex off queue
		vertex = queue.pop(0)
		visited.append(vertex)

		# Find all connections
		for n in athleteDict[vertex]:
			next = n[0]

			if next not in visited:
				if next not in lastConnection:
					lastConnection[next] = vertex

				if next == end:

					value = end
					while value is not 'None':
						path.append(value)
						value = lastConnection[value]
					return path

				elif next not in queue:
					queue.append(next)
	return "No Path"

# User Input loop
while True:
	print "Input this information to see your connection!"
	response = raw_input("Please enter first athlete: ").strip()
	school  = raw_input("Please enter in school: ").lower()
	response = response + " (" + school + ")"
	while response not in athleteDict:
		response = raw_input("Did not exist, enter another athlete: ").strip()
		school  = raw_input("Please enter in school: ").lower()
		response = response + " (" + school + ")"

	response2 = raw_input("Please enter second athlete: ").strip()
	school  = raw_input("Please enter in school: ").lower()
	response2 = response2 + " (" + school + ")"
	while response2 not in athleteDict:
		response2 = raw_input("Did not exist, enter another athlete: ").strip()
		school  = raw_input("Please enter in school: ").lower()
		response2 = response2 + " (" + school + ")"

	print
	print "Searching..."

	path = bfs_path(response, response2)
	if path == "No Path":
		print "No Path"

	else:
		path.reverse()
		print
		print "Here is your connection!"
		print "------------------------"
		print

		print response,
		for i in range(1,len(path)):
			for a in athleteDict[path[i-1]]:
				if a[0] == path[i]:
					if a[2] == "T":
						print "plays %s with %s " % (a[1], a[0])
					else:
						print "went to %s with %s " % (a[1], a[0])

			if i is not len(path) - 1:
				print "Who",

		print
		print "Isn't that interesting!"
		print













