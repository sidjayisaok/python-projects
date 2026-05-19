from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate("/mnt/c/Users/Test/Downloads/Sid_Johnston_Digital_Marketing_Analyst_Cover_Letter.pdf")
styles = getSampleStyleSheet()

text = """Dear Hiring Manager,

I’m excited about this opportunity because it aligns directly with the analytics, tracking, and cross‑functional work I’ve been doing across Insider Inc., Sobo & Sobo, and my agency experience. Over the past several years, I’ve supported digital marketing teams by implementing tracking strategies, validating data integrity, troubleshooting analytics issues, and translating business questions into measurable, actionable metrics.

A large part of my work has involved partnering with marketing, engineering, and product teams to define analytics requirements and ensure campaigns are tracked accurately. I’ve built and validated UTM structures, managed campaign URL tagging, and supported teams in understanding how their tracking choices affect downstream reporting. I’m fluent in both Universal Analytics and GA4, and I’m comfortable navigating the differences between the two — especially around event modeling, attribution, and custom dimensions.

Quality assurance has been a consistent part of my workflow. I’ve performed tagging audits, validated data across environments, debugged tracking issues, and worked with developers to resolve configuration gaps. Whether identifying cross‑domain tracking issues, validating payloads, or troubleshooting console errors, I focus on ensuring that the data teams rely on is accurate, stable, and trustworthy.

I’ve also created dashboards, ad hoc reports, and performance summaries to help stakeholders understand what’s happening on their sites and campaigns. My background in SQL, Excel, and GA reporting gives me a strong foundation for building Looker Studio dashboards and translating raw data into insights that support decision‑making. I enjoy helping teams understand not just what the numbers say, but why they look the way they do.

Collaboration is one of my strengths. I’ve worked closely with media agencies, analytics vendors, and internal teams to prioritize work, clarify requirements, and keep projects moving. I’m comfortable managing backlogs, coordinating with external partners, and communicating clearly with both technical and non‑technical audiences. I also enjoy creating documentation and training materials that help teams adopt new processes and improve their analytics maturity.

This role feels like a natural extension of the work I’ve been doing — combining analytics, QA, tracking governance, and cross‑team collaboration. I’d welcome the chance to bring my experience to your team and contribute to a more stable, accurate, and actionable analytics environment.

Thank you for your time and consideration.

Sid Johnston  
sidjay18@gmail.com
201‑927‑6399
linkedin.com/in/sidjay
"""

story = []
for line in text.split("\n"):
    story.append(Paragraph(line, styles["Normal"]))
    story.append(Spacer(1, 10))

path = "/mnt/c/Users/Test/Downloads/Sid_Johnston_Digital_Marketing_Analyst_Cover_Letter.pdf"
doc.build(story)

path