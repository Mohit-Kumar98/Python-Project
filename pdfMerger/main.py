import PyPDF2
def merge_pdfs( input_pdfs , output_pdf ):
    merger = PyPDF2.PdfMerger()

    for pdf in input_pdfs:
        merger.append(pdf)

    merger.write(output_pdf)
    merger.close()

if __name__ == "__main__":
    input_pdfs = ["blank.pdf", "sample.pdf"]  # List of input PDF files
    output_pdf = "merged_output.pdf"  # Output PDF file

    merge_pdfs(input_pdfs, output_pdf)
    print(f"PDF files merged into {output_pdf}")
