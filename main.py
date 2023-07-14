from PDF_Highlighter import highlighter
import sys

def main():
    isAll = True
    page = -1
    data = sys.argv[2]
    filename = sys.argv[1]
    # at least the filename and data must be provided
    if (len(sys.argv) < 3):
        print("Error: not enough arguments")
        quit()
    # if a single page is desired
    if "-single_page" in sys.argv:
        isAll = False
        page = sys.argv[-1]
    # if a list is given
    if "-list" in sys.argv:
        # treats the data is a filename and opens it
        listfile = open(data, "r")
        text = listfile.read()
        # turns data into a list of all the words in the text
        data = text.split("#")
    theHighlighter = highlighter(filename)
    theHighlighter.run(isAll, data, page)

main()