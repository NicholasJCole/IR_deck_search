import pypdfium2 as pdfium

def make_images(filepath):
    pdf = pdfium.PdfDocument(filepath)
    page_indices = [i for i in range(len(pdf))]
    renderer = pdf.render_to(
        pdfium.BitmapConv.pil_image,
	    page_indices = page_indices,
    )
    for image, index in zip(renderer, page_indices):
        image.save("output_%02d.jpg" % index)

if __name__ == '__main__':
	filepath = "data/pdfs/pdf1.pdf"
	make_images(filepath)
