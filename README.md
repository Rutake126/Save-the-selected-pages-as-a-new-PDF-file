

# PDF 特定页数提取脚本

这是一个使用 PyPDF2 库的 Python 脚本，用于从源 PDF 文件中提取指定页数范围并保存为新的 PDF 文件。

## 脚本功能

此脚本可以读取一个 PDF 文件，并从中提取指定页码范围内的页面，然后将提取的页面写入到一个新的 PDF 文件中。

## 使用方法

1. **设置文件路径**：
   - `input_pdf_path`：指定要从中提取页面的源 PDF 文件路径。
   - `output_pdf_path`：指定要保存提取页面的新 PDF 文件路径。

   示例：
   ```python
   input_pdf_path = r'E:\2025\1\test.pdf'
   output_pdf_path = r'E:\2025\1\new.pdf'
   ```

2. **指定页码范围**：
   - `start_page` 和 `end_page` 分别代表你想要提取的起始页码和结束页码（包含起始页和结束页）。

   示例：
   ```python
   start_page = 13
   end_page = 13
   ```

3. **执行操作**：
   - 脚本会使用 PyPDF2 的 PdfReader 类读取源 PDF 文件。
   - 然后创建一个 PdfWriter 实例，并通过循环将指定页码范围内的页面添加至新 PDF 中。
   - 最后，使用 `write()` 方法将新 PDF 文件内容写入到指定路径。

运行脚本后，将会看到如下提示信息：
```shell
Extracted pages {start_page}-{end_page} from {input_pdf_path} and saved to {output_pdf_path}
```
这意味着指定页码范围内的页面已经成功从源文件提取并保存到了新文件中。

## 安装依赖

在运行此脚本之前，请确保已安装 PyPDF2 库：
```shell
pip install PyPDF2
```

## 注意事项
- 请注意，这里的页码是从 0 开始计数的，因此实际提取时需减去 1（例如，提取第 13 页时应使用 `range(12, 13)`）。
- 此脚本仅支持单次连续的页码提取，如需提取多个不连续的页码段，请修改脚本以适应需求。
