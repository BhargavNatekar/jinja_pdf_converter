from jinja2 import Environment,FileSystemLoader
import sys
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
app = QtWidgets.QApplication(sys.argv)
loader = QtWebEngineWidgets.QWebEngineView()
loader.setZoomFactor(1)
loader.page().pdfPrintingFinished.connect(
    lambda *args: print('finished:', args))
loader.load(QtCore.QUrl('file:///C:/Users/u625299/OneDrive%20-%20Fortive/Desktop/Jinja/jinja_graph.html'))

env=Environment(loader=FileSystemLoader('templates'))
template=env.get_template('template.html')
html=template.render(place_holder="this is rendered from python")
with open("jinja_graph.html", "w") as f:
    f.write(html)
def emit_pdf(finished):
    loader.show()
    loader.page().printToPdf("test.pdf")


loader.loadFinished.connect(emit_pdf)

app.exec()