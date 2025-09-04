# Power BI Template Utility

Duplicate a `.pbit` (Power BI template) file into new template files with different names.

## Usage

```bash
# Example: duplicate report_template.pbit into SalesReport.pbit and FinanceReport.pbit
python powerbi/duplicate_pbit.py ./report_template.pbit SalesReport FinanceReport -o ./output
```

This will create:

```
output/
  SalesReport.pbit
  FinanceReport.pbit
```
