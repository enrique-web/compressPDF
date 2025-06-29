from pypdf import PdfWriter

def compress_pdf(input_pdf_path: str, output_pdf_path: str, remove_images=False, reduce_image_quality=False, image_quality=80, compression_level=9):
    """
    Compress a PDF file using pypdf library.

    Parameters:
    - input_pdf_path: str, path to the input PDF file.
    - output_pdf_path: str, path to save the compressed PDF file.
    - remove_images: bool, if True, removes all images from the PDF.
    - reduce_image_quality: bool, if True, reduces the quality of images to the specified image_quality (0-100).
    - image_quality: int, quality level for image compression (only used if reduce_image_quality=True).
    - compression_level: int, level of lossless compression (0-9), higher means more compression.
    """
    writer = PdfWriter(clone_from=input_pdf_path)

    if remove_images:
        writer.remove_images()

    if reduce_image_quality:
        for page in writer.pages:
            for img in page.images:
                img.replace(img.image, quality=image_quality)

    # Apply lossless compression to content streams
    for page in writer.pages:
        page.compress_content_streams(level=compression_level)

    with open(output_pdf_path, "wb") as f_out:
        writer.write(f_out)

    print(f"Compressed PDF saved to {output_pdf_path}")

# Example usage
if __name__ == "__main__":
    input_pdf = "example.pdf"
    output_pdf = "compressed_output.pdf"
    compress_pdf(input_pdf, output_pdf, remove_images=False, reduce_image_quality=True, image_quality=80, compression_level=9)
