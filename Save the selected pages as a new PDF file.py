import PyPDF2

#指定文件路径
input_pdf_path = r'E:\2025\1\test.pdf'
output_pdf_path = r'E:\2025\1\new.pdf'

start_page = 13
end_page = 13

#读取
reader = PyPDF2.PdfReader(input_pdf_path)

#创建一个新的PDF，并写入
writer = PyPDF2.PdfWriter()

for page_num in range(start_page - 1, end_page):
    writer.add_page(reader.pages[page_num])

#保存
with open(output_pdf_path, 'wb') as f:
    writer.write(f)

print(f'Extracted pages {start_page}-{end_page} from {input_pdf_path} and saved to {output_pdf_path}')
