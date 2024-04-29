import os.path


class MainDirectories:
    ROOT_DIR = os.path.abspath(os.curdir)
    report_dir = ROOT_DIR + '/reports/'


class BasicActions:
    @staticmethod
    def convert_datetime(input):
        output = str(input).replace(" ", "_").replace("-", "_").replace(":", "_").replace("/", "_").replace("*", "")
        return output