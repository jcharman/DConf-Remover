#Script to list all the home directories present on the system and remove the users dconf preferences
#Written by Jake Charman

#Import the required library
import os

#For every subfolder of /home/
for usr in next(os.walk('/home'))[1]:
	#Set the full path of the file
	hmDir = ("/home/" + usr + "/.config/dconf/user")
	#Print the file path to be deleted
	print("Removing: " + hmDir)
	#Check that the file exists
	if os.path.exists(hmDir):
		#Remove the file
		os.remove(hmDir)
	#Should the file be non existant
	else:
		#Print error, move to the next directory
		print("File does not exist, skipping")
