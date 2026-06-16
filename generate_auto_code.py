from jinja2 import Environment, FileSystemLoader
from validate_json import ReadValidateJson
import logging


class GenerateCode(ReadValidateJson):
    def __init__(self):
        super().__init__()
        self.signal_list = self.read_signals_json()

    def write_and_format(self):
        env = Environment(loader=FileSystemLoader("templates"))
        template = env.get_template("src_code.jinja")
        context = {
            "signals": self.signal_list
        }
        output = template.render(context)
        cpp_file_path = "source_code/mappings.cpp"
        with open(cpp_file_path, "w") as fp:
            fp.write(output)
            self.logger.debug(f"{cpp_file_path} written and formatted")


if __name__ == "__main__":
    code_gen = GenerateCode()
    code_gen.write_and_format()