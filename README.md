# Power BI Template Duplicator (AWS Lambda)

This Lambda function duplicates a `.pbit` file stored in Amazon S3 into multiple new templates with different names.

## 🚀 Deployment

1. Create an S3 bucket and upload your base template (e.g., `templates/base_template.pbit`).
2. Deploy the Lambda function with:
   - Runtime: Python 3.9+
   - Handler: `lambda_function.lambda_handler`
   - IAM Role: Requires `s3:GetObject` and `s3:PutObject` permissions.
3. Configure environment variables:
   - `SOURCE_BUCKET` = name of the bucket containing the base template
   - `SOURCE_KEY` = path to the base `.pbit` (e.g., `templates/base_template.pbit`)
   - `TARGET_BUCKET` (optional) = bucket where duplicates will be stored
4. Update `new_template_names` in `lambda_function.py` with your desired template filenames.
5. (Optional) Add an EventBridge rule to trigger on `s3:ObjectCreated:*` for automation.

## 🛠 Example

- Input: `s3://my-bi-templates/templates/base_template.pbit`
- Output:
  - `s3://my-bi-templates/templates/template_sales.pbit`
  - `s3://my-bi-templates/templates/template_marketing.pbit`
  - `s3://my-bi-templates/templates/template_finance.pbit`
