import sys

# https://vidigest.com/2018/12/02/generating-an-html-table-from-file-data-using-python-3/
def write_ul(mylist):
    fileout = open("result.html", "w")
    result = "<h1>Search results</h1>\n"
    result += "<ol>\n"
    for row in mylist:
        result += "    <li><a href = '{0}'>{0}</a></li>\n".format(row[0].strip())
    result += "</ol>\n"
    fileout.writelines(result)
    fileout.close()
