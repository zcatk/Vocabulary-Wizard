import unirest

def get_definitions():
	"""Print definitions received from API call"""
	for u_def in response.body['results']:
		try:
			print("- " + u_def['definition'].capitalize())
		except:
			continue

def get_synonyms():
	"""Print synonyms received from API call"""
	for u_syn in response.body['results']:
		try:
			for p_syn in u_syn['synonyms']:
				print("- " + p_syn.title())
		except:
			continue

def get_antonyms():
	"""Print antonyms received from API call""" 
	for u_ant in response.body['results']:
		try:
			for p_ant in u_ant['antonyms']:
				print("- " + p_ant.title())
		except:
			continue

def get_examples():
	"""Print examples received from API call"""
	for u_example in response.body['results']:
		try:
			for p_example in u_example['examples']:
				print("- " + p_example.capitalize())
		except:
			continue

# Initialize loop and provide graceful quit option
while True:

	uword = raw_input("\nPlease enter a word or 'q' to quit: ")

	if uword == 'q':
		break
	else:
# API Call
		response = unirest.get("https://wordsapiv1.p.rapidapi.com/words/" + uword,
  headers={
# API Key 
    "X-RapidAPI-Key": "ENTER KEY FROM RAPIDAPI HERE"
  }
)

# Output from user input
		print("\n\t" + uword.title())
		print("\nDefinitions: ")
		get_definitions()
		print("\nSynonyms: ")
		get_synonyms()
		print("\nAntonyms: ")
		get_antonyms()
		print("\nExamples: ")
		get_examples()