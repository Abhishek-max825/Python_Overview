import os
import shutil


def file_ogranizer(file_name):
    file_jpg = [file for file in file_name if file.endswith((".jpg", ".png"))]
    file_pdf = [file for file in file_name if file.endswith(".pdf")]
    print(file_jpg)  # ['1.jpg', '2.jpg', '3.jpg', '4.png']
    print(file_pdf)  # ['merged-pdf.pdf', 'resume.pdf', 'SYNOPSIS_MAX.pdf']

    if not os.path.exists("12. Hands On Python Projects/jpg_files") and not os.path.exists("12. Hands On Python Projects/pdf_files"):
        os.mkdir("12. Hands On Python Projects/jpg_files", exist_ok=True)
        os.mkdir("12. Hands On Python Projects/pdf_files", exist_ok=True)

    folder = os.path.dirname(__file__)


    for i, filename in enumerate(sorted(file_jpg), start=1):
        _, extension = os.path.splitext(filename)
        old_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, f"jpg_files/new_photo{i}{extension}")
        os.rename(old_path, new_path)

    pdf_folder = os.path.join(folder, "pdf_files")
    os.makedirs(pdf_folder, exist_ok=True)

    for filename in file_pdf:
        shutil.move(os.path.join(folder, filename), os.path.join(pdf_folder, filename))


if __name__ == "__main__":
    file = os.listdir(os.path.dirname(__file__))
    file_ogranizer(file)
