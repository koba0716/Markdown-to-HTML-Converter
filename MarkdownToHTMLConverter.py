import markdown
import sys
import os

# MarkdownToHTMLConverter.py input_file output_file
# input_fileはmd拡張子であることを確認する。
# 引数の入力が正しいことを確認する。
# output_fileの拡張子はHTMLであること

def validate_file_exists(path):
    if not os.path.isfile(path):
        print(f"❌ ファイルが存在しません: {path}")
        sys.exit(1)

def validate_args_count(expected_count):
    if len(sys.argv) != expected_count:
        print(f"❌ 引数の数が正しくありません（{expected_count - 1} 個必要）")
        sys.exit(1)

def validate_extensions(input_file, output_file):
    if not input_file.endswith(".md"):
        print("❌ 入力ファイルは .md 拡張子である必要があります")
        sys.exit(1)
    if not output_file.endswith(".html"):
        print("❌ 出力ファイルは .html 拡張子である必要があります")
        sys.exit(1)

def convert_html(input_file, output_file):
    with open(input_file, 'r', encoding="utf-8") as f:
        md_text = f.read()

    html = markdown.markdown(md_text)
    
    with open(output_file, 'w', encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    validate_args_count(3)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    validate_file_exists(input_file)
    validate_extensions(input_file, output_file)
    convert_html(input_file, output_file)



