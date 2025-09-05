import boto3
import os

s3 = boto3.client("s3")

def lambda_handler(event, context):
    """
    AWS Lambda handler to duplicate a .pbit file in S3 into multiple
    new templates with different names.
    """

    # Read environment variables (set in Lambda console or SAM/CloudFormation)
    source_bucket = os.environ.get("SOURCE_BUCKET")
    source_key = os.environ.get("SOURCE_KEY")  # e.g., "templates/base_template.pbit"
    target_bucket = os.environ.get("TARGET_BUCKET", source_bucket)

    # List of new template names to create
    new_template_names = [
        "template_sales.pbit",
        "template_marketing.pbit",
        "template_finance.pbit"
    ]

    try:
        for template_name in new_template_names:
            target_key = f"templates/{template_name}"

            # Copy file inside S3
            copy_source = {"Bucket": source_bucket, "Key": source_key}
            s3.copy_object(
                CopySource=copy_source,
                Bucket=target_bucket,
                Key=target_key
            )

            print(f"✅ Duplicated {source_key} -> {target_key}")

        return {
            "statusCode": 200,
            "body": f"Successfully duplicated {source_key} into {len(new_template_names)} templates"
        }

    except Exception as e:
        print(f"❌ Error duplicating template: {str(e)}")
        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}"
        }
