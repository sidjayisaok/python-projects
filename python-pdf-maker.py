from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

#path name needs to match system
doc = SimpleDocTemplate("/mnt/c/Users/Test/Downloads/digital-analyst-sid-johnston.pdf")
styles = getSampleStyleSheet()

text = """
Dear Hiring Manager,

Why am I applying for this role?  
Because it lines up almost exactly with the analytics, tracking, and reporting work I’ve been doing across Insider Inc., Sobo & Sobo, and my agency experience. I’ve spent years inside media and marketing environments where clean data, accurate tagging, and fast insights aren’t “nice to have” — they’re the only way anything gets done.

Do I have the 4–6 years of analytics experience you’re looking for?  
Yes. At Insider, I’ve supported subscription marketing with data‑connected email templates, landing pages, QA, and performance tracking. At Sobo & Sobo, I handled SEO/SEM analysis, PPC reporting, Google Ads strategy, SQL‑driven insights, and Excel/VBA automation. Across all roles, analytics has been part of my daily workflow, not a side task.

What about the tools — GA4, campaign tracking, Looker Studio, SQL?  
I’ve worked with Google Analytics for years, including the shift to GA4. I’ve built and validated UTM structures, managed campaign tagging, and supported teams in understanding how their tracking choices affect downstream reporting. SQL and Excel are two of my strongest skills — I’ve written queries, built databases, automated reports, and used data to guide marketing decisions. Looker Studio is a natural extension of the reporting work I already do.

Can I handle the fast‑paced, multi‑workstream environment of an agency?  
Definitely. I’ve worked in agencies, on freelance contracts, and in high‑volume media environments where priorities shift quickly and you’re expected to figure things out before someone asks. At Insider, I regularly collaborate with marketing, engineering, and product teams to troubleshoot issues, validate data, and keep projects moving.

How do I approach insights and communication?  
I like to make data feel usable. Whether I’m explaining why a campaign underperformed, validating tracking issues, or walking someone through a dashboard, I focus on clarity and context. My background in journalism actually helps here — I’m comfortable translating complex information into something people can act on.

What makes me a strong fit overall?  
I bring a mix of analytics, SQL, GA experience, campaign tracking, QA, and cross‑team collaboration — all grounded in real media and marketing environments. I’m proactive, detail‑oriented, and comfortable taking ownership of multiple workstreams. Most importantly, I enjoy the work: digging into data, finding the story, and helping teams make better decisions.

Thank you for your time and consideration. I’d welcome the chance to bring my analytics experience to your team.

Sid Johnston  
sidjay18@gmail.com
201‑927‑6399
linkedin.com/in/sidjay
"""

story = []
for line in text.split("\n"):
    story.append(Paragraph(line, styles["Normal"]))
    story.append(Spacer(1, 10))

#path name needs to match system
path = "/mnt/c/Users/Test/Downloads/digital-analyst-sid-johnston.pdf"
doc.build(story)

path