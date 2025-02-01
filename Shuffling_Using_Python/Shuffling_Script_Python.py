import pandas as pd
import random
from fpdf import FPDF
import os

def read_mcqs(file_path):
    data = pd.read_csv(file_path)
    # Ensure required columns are present
    required_columns = ['S.No.', 'Question', 'Circle A', 'Circle B', 'Circle C', 'Circle D']
    for col in required_columns:
        if col not in data.columns:
            raise ValueError(f"The file must have a column named '{col}'.")
    return data

def generate_shuffled_pdfs(data, num_pdfs, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    mcqs = data.to_dict(orient='records')  # Convert DataFrame rows into a list of dictionaries

    for i in range(1, num_pdfs + 1):
        shuffled_mcqs = mcqs.copy()
        random.shuffle(shuffled_mcqs)

        # Create a PDF
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()

        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt=f"MCQ Set {i}", ln=True, align='C')
        pdf.ln(10)

        for idx, mcq in enumerate(shuffled_mcqs[:20], start=1):  # Only take the first 20 MCQs
            # Print the question
            pdf.multi_cell(0, 10, txt=f"{idx}. {mcq['Question']}")

            # Print the options
            pdf.multi_cell(0, 10, txt=f"A) {mcq['Circle A']}    B) {mcq['Circle B']}    C) {mcq['Circle C']}    D) {mcq['Circle D']}")
            pdf.ln(5)

        # Save the PDF
        pdf_path = os.path.join(output_folder, f"MCQ_Set_{i}.pdf")
        pdf.output(pdf_path)
        print(f"Generated: {pdf_path}")

def main():
    # Input file (update with your actual file path)
    input_file = r"E:\Ali Raza\Corvit Institute Projects Python"  # Replace with your actual file path
    output_folder = "Shuffled_PDFs"
    num_pdfs = 30  # Number of PDFs to generate

    # Load MCQs from file
    data = read_mcqs(input_file)

    # Check if there are enough MCQs
    if len(data) < 20:
        raise ValueError("The file must contain at least 20 MCQs.")

    # Generate shuffled PDFs
    generate_shuffled_pdfs(data, num_pdfs, output_folder)

if __name__ == "__main__":
    main()