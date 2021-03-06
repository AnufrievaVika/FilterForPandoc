from panflute import *
import sys

all_headers = {}


def action(elem, doc):
    if type(elem) == Header:
        if stringify(elem) in all_headers.keys() and all_headers.get(stringify(elem)) == elem.level:
            sys.stderr.write("Repeated headers. Level: " + str(elem.level) + ", text: \"" + stringify(elem) + "\"\n")
        else:
            all_headers[stringify(elem)] = elem.level
        if elem.level <= 3:
            title = [Str(stringify(elem).upper())]
            return Header(*title, level=elem.level)

    if type(elem) == Str and str(elem.text).lower() == "bold":
        title = [Str(elem.text)]
        return Strong(*title)


def main(doc=None):
    return run_filter(action, doc=doc)


if __name__ == "__main__":
    main()
