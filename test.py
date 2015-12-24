# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 19:07:05 2015

@author: aduba_000
"""

from reportlab.pdfgen import canvas
from reportlab.lib.units import cm, mm, inch, pica
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, cm
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import Paragraph, Table, TableStyle

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib import colors

from Poll import Poll

poll = Poll("Bloomberg Politics", "Iowa Caucus - Republican", 400, 15, {});
poll.addCandidate("Jeb Bush")
candidates = poll.pollNumbers.keys();



title = poll.companyName;
pdf = canvas.Canvas('test2.pdf')
pdf.setFont('Helvetica', 12)
pdf.setStrokeColorRGB(1, 0, 0)
pdf.drawString(1 * inch, 11*inch, title)

#Fix the constants

pdf.drawString(1 * inch, 11*inch - 5*mm, "SELZER & COMPANY")
pdf.drawString(1 * inch, 11*inch - 10*mm, "400 Republican likely voters")
pdf.drawString(1 * inch, 11*inch - 15*mm, "Margin of error: ± 4.9 percentage points for Republicans")
pdf.drawString(1 * inch, 11*inch - 20*mm, "")
pdf.drawString(1 * inch, 11*inch - 25*mm, "Study #2130")
pdf.drawString(1 * inch, 11*inch - 30*mm, "December 7-10, 2015")
pdf.drawString(1 * inch, 11*inch - 35*mm, "2,635 contacts weighted by age, sex, and district to conform to the active voter profile.")
pdf.setFont("Helvetica-Bold", 12)
pdf.drawString(3.5 * inch, 11*inch - 45*mm, "Poll Questions")
pdf.drawString(1.7 * inch, 11*inch - 50*mm, "PERCENTAGES MAY NOT ADD TO 100% DUE TO ROUNDING.")
pdf.setFont("Helvetica", 11)
pdf.drawString(1 * inch, 11*inch - 60*mm, "Which one of the following Republicans would be your first choice for president?  (Read list and rotate.)")
pdf.drawString(1 * inch, 11*inch - 65*mm, "And who would your second choice be? ")
pdf.setFont("Helvetica-Bold", 10)
pdf.drawString(1 * inch, 11*inch - 70*mm, "If Uncommitted or Not sure in first choice question, code second choice as No first choice and do not ask. ")
pdf.drawString(1 * inch, 11*inch - 75*mm, "(Read list only if necessary)")
pdf.drawString(1 * inch, 11*inch - 80*mm, "")


height = 11*inch - 80*mm

pdf.setFont("Helvetica", 11)
#Write candidates
#candidates = ["Jeb Bush","Ben Carson","Chris Christie", "Ted Cruz", "Carly Fiorina", "Jim Gilmore", "Mike Huckabee", "John Kasich","George Pataki", "Rand Paul","Marco Rubio","Rick Santorum","Donald Trump","Uncommitted","Not sure", "No first choice"]
#candidates2 = ["Jeb Bush","Ben Carson","Chris Christie", "Ted Cruz"]


    
#Set styles 
styles = getSampleStyleSheet()
styleN = styles["BodyText"]
styleN.alignment = TA_LEFT
styleBH = styles["Normal"]
styleBH.alignment = TA_CENTER


# Headers
candidate = Paragraph('''<b>Candidate</b>''', styleBH)
firstChoice = Paragraph('''<b>1st Choice</b>''', styleBH)
secondChoice = Paragraph('''<b>2nd Choice</b>''', styleBH)
combinedFirstAndSecond = Paragraph('''<b>Combined</b>''', styleBH)


#Set Header
header = [candidate, firstChoice,secondChoice, combinedFirstAndSecond]   
data= []
data.append(header)



for i in range(len(candidates)):
    number = []
    name = Paragraph(candidates[i], styleBH);
    number.append(name)
    choiceList = poll.pollNumbers[candidates[i]]
    numberOneChoice = choiceList[0]
    numberTwoChoice = choiceList[1]
    combined = choiceList[2]
    number.append(Paragraph(str(numberOneChoice), styleBH))
    number.append(Paragraph(str(numberTwoChoice), styleBH))
    number.append(Paragraph(str(combined), styleBH))
    data.append(number)
    

table = Table(data, colWidths=[5 * cm, 5 * cm, 5 * cm,
                               5* cm, 5 * cm])
#table.setStyle(TableStyle([
                       #('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       #('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       #]))

table.wrapOn(pdf, 50,100)
#hardcoded in height
table.drawOn(pdf, 50,(height-10) - len(candidates)*20)
print height
pdf.showPage()
pdf.save()