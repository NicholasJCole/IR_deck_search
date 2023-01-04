
import requests
from bs4 import BeautifulSoup


def main(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	links = soup.find_all('a')
	i = 0
	files_saved = []
	for link in links:
		if ('.pdf' in link.get('href', [])):
			i+=1
			print("Downloading file: ", link.get('href', []))
			# if else to add 'https' to links that don't have it
			# requests don't pull if no https 
			if link.get('href', [])[0:4] == 'http':
				response = requests.get(link.get('href'))
			else:
				response = requests.get(('https:' + link.get('href')))
			pdf = open("pdf"+str(i)+".pdf", 'wb')
			pdf.write(response.content)
			pdf.close()
			print("File ", i, " downloaded")		
			files_saved.append(link.get('href', []))
	return files_saved


if __name__ == '__main__':
	# below url is placeholder
    url = "https://investors.jfrog.com/events-and-presentations/presentations/default.aspx"
    main(url)
 
