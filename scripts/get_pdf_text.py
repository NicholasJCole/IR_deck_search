import pdfplumber

def get_text(pdf_file):
	with pdfplumber.open(pdf_file) as pdf:
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
		print(pdf_text)
	return pdf_text
			

if __name__ == '__main__':
	pdf_file = "data/pdfs/pdf1.pdf"
	pdf_text = get_text(pdf_file)
