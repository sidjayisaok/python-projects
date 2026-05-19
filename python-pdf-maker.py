from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

#path name needs to match system
doc = SimpleDocTemplate("/mnt/c/Users/Test/Downloads/[file name].pdf")
styles = getSampleStyleSheet()

text = """
"""

story = []
for line in text.split("\n"):
    story.append(Paragraph(line, styles["Normal"]))
    story.append(Spacer(1, 10))

#path name needs to match system
path = "/mnt/c/Users/Test/Downloads/[file name].pdf"
doc.build(story)

path