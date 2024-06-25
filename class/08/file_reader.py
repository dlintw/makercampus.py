import os

class FileNotFoundError(Exception):
    def __init__(self, filename):
        self.filename = filename
        self.message = f"文件未找到：{self.filename}"
        super().__init__(self.message)

def read_file(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(filename)

    try:
        with open(filename, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"讀取文件時發生錯誤：{e}")

def main():
    filename = 'example.txt'
    try:
        content = read_file(filename)
        if content:
            print(content)
    except FileNotFoundError as e:
        print(f"錯誤：{e.message}")

if __name__ == "__main__":
    main()
