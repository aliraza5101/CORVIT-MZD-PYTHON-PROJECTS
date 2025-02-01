import os
from reportlab.lib.pagesizes import legal
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
import tkinter as tk
from tkinter import messagebox

class Family_Member():
    def __init__(self, name, age, qualification, eye_color, emotions, cast, language, city):
        self.name = name
        self.age = age
        self.qualification = qualification
        self.eye_color = eye_color
        self.emotions = emotions
        self.cast = cast
        self.language = language
        self.city = city

father = Family_Member("Nusrat Fateh Ali Khan", 45, "PHD English", "Brown", "Angry", "Mughal", "English", "Muzaffarabad")
mother = Family_Member("Abida Parveen", 42, "PHD Computer Sciences", "Pink", "Happy", "Mughal", "English", "Muzaffarabad")
elder_brother = Family_Member("Chahat Fateh Ali Khan", 25, "PHD Mathematics", "Black", "Blessed", "Mughal", "English", "Muzaffarabad")
brother_1 = Family_Member("Noora Ali", 20, "PHD Botany", "Green", "Obsessed", "Mughal", "English", "Muzaffarabad")
brother_2 = Family_Member("Rock Ali Khan Azam", 18, "PHD Islamiat", "Yellow", "Celebrated", "Mughal", "English", "Muzaffarabad")

# Create the main window
root = tk.Tk()
root.title("Family Tree by Ali Raza")
root.geometry("700x400")  # Reduced window size
root.configure(bg="#1A242F")  # Dark background color

selected_details = ""

def show_details(member):
    global selected_details
    selected_details = f"Name: {member.name}\nAge: {member.age}\nQualification: {member.qualification}\nEye Color: {member.eye_color}\nEmotions: {member.emotions}\nCast: {member.cast}\nLanguage: {member.language}\nCity: {member.city}"
    details_text.delete(1.0, tk.END)
    details_text.insert(tk.END, selected_details)

def show_family_members_names():
    family_names = [
        father.name,
        mother.name,
        elder_brother.name,
        brother_1.name,
        brother_2.name
    ]
    details_text.delete(1.0, tk.END)
    details_text.insert(tk.END, "\n".join(family_names))

def print_all_family_members_to_pdf():
    # PDF file setup
    pdf_filename = "all_family_members_details.pdf"
    pdf_path = os.path.join(os.getcwd(), pdf_filename)

    # Create the PDF document with Legal page size
    page_width, page_height = legal  # page dimensions in points
    c = canvas.Canvas(pdf_path, pagesize=legal)

    # Set margins
    margin = 25
    available_width = page_width - 2 * margin

    # --- Header Section with Logo ---
    logo_path = "corvit.png"  # Logo file name as provided
    logo_width = 80
    logo_height = 80
    try:
        # Draw logo at left margin
        c.drawImage(logo_path, margin, 930, width=logo_width, height=logo_height, preserveAspectRatio=True)
    except Exception as e:
        # Agar logo load na ho, error print ho jayega
        print(f"Logo load failed: {e}")

    # Header text (centered)
    header_text = "Family Registration Details"
    subheader_text = "Complete Information of All Members"
    
    # Calculate text widths to center them
    header_font = "Helvetica-Bold"
    header_font_size = 18
    subheader_font = "Helvetica-Oblique"
    subheader_font_size = 12
    
    header_text_width = c.stringWidth(header_text, header_font, header_font_size)
    subheader_text_width = c.stringWidth(subheader_text, subheader_font, subheader_font_size)
    
    header_x = (page_width - header_text_width) / 2
    subheader_x = (page_width - subheader_text_width) / 2

    c.setFont(header_font, header_font_size)
    c.setFillColor(colors.HexColor("#0A3871"))
    c.drawString(header_x, 950, header_text)
    
    c.setFont(subheader_font, subheader_font_size)
    c.setFillColor(colors.black)
    c.drawString(subheader_x, 930, subheader_text)
    
    # Draw a line below the header spanning within margins
    c.line(margin, 920, page_width - margin, 920)

    # --- Table Data Preparation ---
    styles = getSampleStyleSheet()
    para_style = styles["BodyText"]
    para_style.fontName = "Helvetica"
    para_style.fontSize = 8    # Compact font size
    para_style.leading = 10

    # Prepare table data with headers; wrap long texts in Paragraph for "Name" and "Qualification"
    table_data = [[
        "Name", "Age", "Qualification", "Eye Color", "Emotions", "Cast", "Language", "City"
    ]]
    family_members = [father, mother, elder_brother, brother_1, brother_2]
    for member in family_members:
        table_data.append([
            Paragraph(member.name, para_style),
            member.age,
            Paragraph(member.qualification, para_style),
            member.eye_color,
            member.emotions,
            member.cast,
            member.language,
            member.city,
        ])

    # Set column widths (percentage distribution)
    col_widths = [
        available_width * 0.20,  # Name
        available_width * 0.08,  # Age
        available_width * 0.22,  # Qualification
        available_width * 0.08,  # Eye Color
        available_width * 0.12,  # Emotions
        available_width * 0.10,  # Cast
        available_width * 0.10,  # Language
        available_width * 0.10   # City
    ]

    # Create and style the table
    table = Table(table_data, colWidths=col_widths)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#0A3871")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
    ]))
    table.hAlign = 'CENTER'

    # Wrap and draw the table
    table_width, table_height = table.wrapOn(c, available_width, page_height)
    x_position = (page_width - table_width) / 2
    y_position = 880  # Starting y-position for the table
    table.drawOn(c, x_position, y_position - table_height)

    # --- Footer Section ---
    c.setFont("Helvetica-Oblique", 10)
    c.setFillColor(colors.HexColor("#999999"))
    c.drawString(margin, 30, "Generated by Family Tree App - Ali Raza")
    c.drawString(page_width - margin - 50, 30, "Page 1")

    c.save()
    messagebox.showinfo("Success", f"All family members' details saved to {pdf_filename}")

# Left-side frame for buttons
frame_buttons = tk.Frame(root, bg="#1A242F")
frame_buttons.pack(side=tk.LEFT, fill=tk.Y, padx=30, pady=30)
buttons_data = [
    ("Show Father Details", lambda: show_details(father), "#007AFF", father),  # iOS Blue
    ("Show Mother Details", lambda: show_details(mother), "#34C759", mother),  # iOS Green
    ("Show Elder Brother Details", lambda: show_details(elder_brother), "#FF3B30", elder_brother),  # iOS Red
    ("Show Brother 1 Details", lambda: show_details(brother_1), "#8E8E93", brother_1),  # iOS Grey
    ("Show Brother 2 Details", lambda: show_details(brother_2), "#AF52DE", brother_2),  # iOS Purple
    ("Show Family Members Only", show_family_members_names, "#FFCC00", None),  # iOS Yellow
]

# Top Heading
heading_label = tk.Label(root, text="Family Tree by Ali Raza", font=("Helvetica", 16, "bold"), fg="white", bg="#1A242F")
heading_label.pack(side=tk.TOP, pady=18)

# Buttons with compact size
for text, command, color, member in buttons_data:
    if member:
        tk.Button(frame_buttons, text=text, command=lambda member=member: show_details(member), bg=color, width=28, height=2, font=("Helvetica", 9, "bold")).pack(pady=7)
    else:
        tk.Button(frame_buttons, text=text, command=show_family_members_names, bg=color, width=28, height=2, font=("Helvetica", 9, "bold")).pack(pady=7)

# Bottom buttons
frame_bottom_buttons = tk.Frame(root, bg="#1A242F")
frame_bottom_buttons.pack(side=tk.BOTTOM, pady=15)

# Now, passing the member to print_to_pdf function
print_button = tk.Button(frame_bottom_buttons, text="Print All to PDF", bg="#1050A2", fg="white", font=("Helvetica", 12, "bold"), width=18, height=2, command=print_all_family_members_to_pdf)
print_button.pack(side=tk.LEFT, padx=10)

close_button = tk.Button(frame_bottom_buttons, text="Close", bg="#C60000", fg="white", font=("Helvetica", 12, "bold"), width=18, height=2, command=root.destroy)
close_button.pack(side=tk.RIGHT, padx=10)

# Right-side text box for details
details_text = tk.Text(root, width=50, height=15, wrap=tk.WORD, font=("Helvetica", 12))
details_text.pack(side=tk.RIGHT, padx=15, pady=15)

# Run the Tkinter event loop
root.mainloop()
