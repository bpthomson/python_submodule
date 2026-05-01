import json
import os
import shutil


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


ls = os.listdir
cd = os.chdir
md = os.mkdir
cp = shutil.copyfile
exist = os.path.exists
pwd = os.getcwd
# cd('..')
root = pwd()


def road(i, j):
    if type(i) == "list":
        ans = root
        for j in i:
            ans = ans + "/" + j
        return ans
    ans = root
    if i:
        ans = ans + "/" + i
    if j:
        ans = ans + "/" + j
    return ans


def getfilename(x: str):
    return x.split("/")[::-1][0]


def mkdir(x: str):
    try:
        md(x)
    except:
        warning(f"While making dir {x}")
        return False
    return True


def zt(x, n):
    x = str(x)
    while len(x) < n:
        x = "0" + x
    return x


def _format_args(args, pretty):
    if not pretty:
        return args
    formatted = []
    for item in args:
        try:
            formatted_item = json.dumps(item, indent=2, ensure_ascii=False, default=str)
            formatted.append("\n" + formatted_item)
        except Exception:
            formatted.append(item)
    return formatted


def warning(*x, txt="WARN", sep=" ", pre=None, end="\n", pretty=False):
    p = ""
    if pre:
        if isinstance(pre, list):
            p = "[" + "] [".join(pre) + "] "
        else:
            p = f"[{pre}]"

    x = _format_args(x, pretty)
    print(
        f"{bcolors.BOLD}{bcolors.WARNING}{txt}{bcolors.ENDC} {p}", *x, sep=sep, end=end
    )


def error(*x, txt="ERROR", sep=" ", pre=None, end="\n", pretty=False):
    p = ""
    if pre:
        if isinstance(pre, list):
            p = "[" + "] [".join(pre) + "] "
        else:
            p = f"[{pre}]"

    x = _format_args(x, pretty)
    print(f"{bcolors.BOLD}{bcolors.FAIL}{txt}{bcolors.ENDC} {p}", *x, sep=sep, end=end)


def info(*x, txt="INFO", sep=" ", pre=None, end="\n", pretty=False):
    p = ""
    if pre:
        if isinstance(pre, list):
            p = "[" + "] [".join(pre) + "] "
        else:
            p = f"[{pre}]"

    x = _format_args(x, pretty)
    print(
        f"{bcolors.BOLD}{bcolors.OKCYAN}{txt}{bcolors.ENDC}  {p}", *x, sep=sep, end=end
    )


def debug(*x, txt="DEBUG", sep=" ", pre=None, end="\n", pretty=False):
    p = ""
    if pre:
        if isinstance(pre, list):
            p = "[" + "] [".join(pre) + "] "
        else:
            p = f"[{pre}]"

    x = _format_args(x, pretty)
    print(
        f"{bcolors.BOLD}{bcolors.OKGREEN}{txt}{bcolors.ENDC} {p}", *x, sep=sep, end=end
    )


def read_from_file(name: str) -> str:
    f = open(name, "r", encoding="UTF-8")
    ans = f.read()
    f.close()
    return ans


def write_to_file(name: str, x):
    with open(name, "w", encoding="UTF-8") as f:
        f.write(str(x))
    f.close()
    return


def append_to_file(name: str, x):
    with open(name, "a", encoding="UTF-8") as f:
        f.write(str(x))
    return
