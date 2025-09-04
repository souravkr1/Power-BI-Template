# Power BI Template Renamer

Utility to duplicate a `.pbit` (Power BI template) file into new template files with different names.

## Usage

```bash
# Make script executable
chmod +x scripts/duplicate_pbit.py

# Example: duplicate report_template.pbit into SalesReport.pbit and FinanceReport.pbit
python scripts/duplicate_pbit.py ./report_template.pbit SalesReport FinanceReport -o ./output
