# compressPDF

A simple Python utility to compress PDF files using the `pypdf` library.

## Description

compressPDF is a lightweight tool to reduce the file size of PDF documents by applying lossless compression techniques. It reads an input PDF, compresses content streams, optionally removes or compresses images, and outputs a smaller PDF file.

## Features

- Lossless compression of PDF content streams
- Optional image compression or removal (depending on implementation)
- Easy to use Python interface
- Minimal dependencies (uses `pypdf`)

## Installation

Install the required library using pip:

```
pip install pypdf
```

Clone the repository:

```
git clone https://github.com/enrique-web/compressPDF.git
cd compressPDF
```

## Usage

Example code to compress a PDF file:

```
from pypdf import PdfReader, PdfWriter

def compress_pdf(input_pdf_path: str, output_pdf_path: str):
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    # Copy pages and compress content streams
    for page in reader.pages:
        page.compress_content_streams()
        writer.add_page(page)

    with open(output_pdf_path, "wb") as f_out:
        writer.write(f_out)

    print(f"Compressed PDF saved to: {output_pdf_path}")

if __name__ == "__main__":
    input_pdf = "input.pdf"
    output_pdf = "compressed_output.pdf"
    compress_pdf(input_pdf, output_pdf)
```

## Notes

- Compression effectiveness depends on the original PDF content.
- For more aggressive compression, consider combining with external tools like Ghostscript.
- This tool focuses on lossless compression and does not degrade image quality by default.

## Contributing

Contributions and suggestions are welcome! Please open issues or submit pull requests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
```
