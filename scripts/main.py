import requests
from bs4 import BeautifulSoup
import pdfplumber
import io
import pypdfium2 as pdfium

url = "https://icdrilling.investorroom.com/index.php?s=66"

def get_pdf_text(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	links = soup.find_all('a')
	for link in links:
		temp = io.BytesIO()
		if ('.pdf' in link.get('href', [])):
			print("Downloading file: ", link.get('href', []))
			# if else to add 'https' to links that don't have it
			# requests don't pull if no https 
			if link.get('href', [])[0:4] == 'http':
				response = requests.get(link.get('href'))
			else:
				response = requests.get(('https:' + link.get('href')))
			temp.write(response.content)
			with pdfplumber.open(temp) as pdf:
				pdf_text = []
				for pg_number in range(len(pdf.pages)):
					if len(pdf.pages[pg_number].extract_text().splitlines())>0:
						page_text = {'title': pdf.pages[pg_number].extract_text().splitlines()[0],
					##				'body': pdf.pages[pg_number].extract_text().splitlines()[1:len(pdf.pages[pg_number].extract_text().splitlines())],
									'full_text': pdf.pages[pg_number].extract_text()}
						pdf_text.append(page_text)
					else:
						page_text = {'title': 'empty',
					##				'body': pdf.pages[pg_number].extract_text().splitlines()[1:len(pdf.pages[pg_number].extract_text().splitlines())],
									'full_text': 'empty'}
						pdf_text.append(page_text)	
				###### add code to make images from temp file as well #####
	return pdf_text
				

if __name__ == '__main__':
	# below url is placeholder
    url = "https://icdrilling.investorroom.com/index.php?s=66"
    pdf_text = get_pdf_text(url)
 
