if __name__ == '__main__':
# opening our url file to access URLs
	file = open("url.txt", "r")

	# iterating over the urls
	for links in file.readlines():
		run_code(links)

print(result)
with open("sample.json", "w") as outfile:
    json.dump(result, outfile)
# print(json_object)

