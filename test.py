# Classroom Test Score Analysis Project
# Generates dataset, graphs, and PDF report

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Preformatted
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4

# ----------------------
# 1. Create Sample Dataset
# ----------------------

np.random.seed(10)

data = pd.DataFrame({
    "Math_Score": np.random.normal(70, 10, 100),
    "Science_Score": np.random.normal(68, 12, 100),
    "English_Score": np.random.normal(72, 8, 100),
    "Study_Hours": np.random.uniform(1, 5, 100)
})

csv_path = "/mnt/data/classroom_test_scores_dataset.csv"
data.to_csv(csv_path, index=False)

# ----------------------
# 2. Generate Graphs (Separate plots, no custom colors)
# ----------------------

# Line Plot - Math Score Trend
plt.figure()
plt.plot(data["Math_Score"])
plt.title("Math Score Trend")
plt.xlabel("Student Index")
plt.ylabel("Math Score")
line_path = "/mnt/data/math_score_trend.png"
plt.savefig(line_path)
plt.close()

# Histogram - Science Scores
plt.figure()
plt.hist(data["Science_Score"], bins=10)
plt.title("Science Score Distribution")
plt.xlabel("Science Score")
plt.ylabel("Frequency")
hist_path = "/mnt/data/science_score_histogram.png"
plt.savefig(hist_path)
plt.close()

# Scatter Plot - Study Hours vs English Score
plt.figure()
plt.scatter(data["Study_Hours"], data["English_Score"])
plt.title("Study Hours vs English Score")
plt.xlabel("Study Hours")
plt.ylabel("English Score")
scatter_path = "/mnt/data/study_vs_english.png"
plt.savefig(scatter_path)
plt.close()

# Bar Chart - Average Scores
plt.figure()
avg_scores = data[["Math_Score", "Science_Score", "English_Score"]].mean()
plt.bar(avg_scores.index, avg_scores.values)
plt.title("Average Subject Scores")
plt.xticks(rotation=45)
bar_path = "/mnt/data/average_scores.png"
plt.savefig(bar_path)
plt.close()

# ----------------------
# 3. Create PDF Report
# ----------------------

pdf_path = "/mnt/data/Classroom_Test_Score_Analysis_Report.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4)
elements = []

styles = getSampleStyleSheet()

elements.append(Paragraph("<b>Classroom Test Score Analysis Report</b>", styles['Title']))
elements.append(Spacer(1, 0.3 * inch))

elements.append(Paragraph("Project Objective:", styles['Heading2']))
elements.append(Paragraph(
    "To analyze student performance across subjects and understand the "
    "relationship between study hours and academic achievement using "
    "statistical and graphical techniques.",
    styles['Normal']))
elements.append(PageBreak())

elements.append(Paragraph("<b>Python Code Used:</b>", styles['Heading2']))

code_text = """
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10)
data = pd.DataFrame({
    "Math_Score": np.random.normal(70, 10, 100),
    "Science_Score": np.random.normal(68, 12, 100),
    "English_Score": np.random.normal(72, 8, 100),
    "Study_Hours": np.random.uniform(1, 5, 100)
})

plt.plot(data["Math_Score"])
plt.hist(data["Science_Score"], bins=10)
plt.scatter(data["Study_Hours"], data["English_Score"])
plt.bar(data[["Math_Score","Science_Score","English_Score"]].mean().index,
        data[["Math_Score","Science_Score","English_Score"]].mean().values)
"""
elements.append(Preformatted(code_text, styles['Code']))
elements.append(PageBreak())

elements.append(Paragraph("Math Score Trend:", styles['Heading2']))
elements.append(Image(line_path, width=5*inch, height=3*inch))
elements.append(PageBreak())

elements.append(Paragraph("Science Score Histogram:", styles['Heading2']))
elements.append(Image(hist_path, width=5*inch, height=3*inch))
elements.append(PageBreak())

elements.append(Paragraph("Study Hours vs English Score:", styles['Heading2']))
elements.append(Image(scatter_path, width=5*inch, height=3*inch))
elements.append(PageBreak())

elements.append(Paragraph("Average Subject Scores:", styles['Heading2']))
elements.append(Image(bar_path, width=5*inch, height=3*inch))

doc.build(elements)

pdf_path
