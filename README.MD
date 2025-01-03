# README

This is a simple take on the [cloudresumechallenge.dev]

# How it works

- We have the infrastructure defined here
- We use terraform to provision
  - S3 to host the frontend
  - API Gateway
  - Lambda to act as our backend
  - DynamoDB on demand for the data store

# Prepare

- On IAM create a user group `cloudresumechallenge`

```bash
# Create IAM group
aws iam create-group --group-name cloudresumechallenge

# Attach policies to the group
aws iam attach-group-policy --group-name cloudresumechallenge --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess
aws iam attach-group-policy --group-name cloudresumechallenge --policy-arn arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess
aws iam attach-group-policy --group-name cloudresumechallenge --policy-arn arn:aws:iam::aws:policy/AWSLambda_FullAccess
aws iam attach-group-policy --group-name cloudresumechallenge --policy-arn arn:aws:iam::aws:policy/AmazonAPIGatewayAdministrator
aws iam attach-group-policy --group-name cloudresumechallenge --policy-arn arn:aws:iam::aws:policy/IAMFullAccess

# Create IAM user
aws iam create-user --user-name cloudresumechallenge-user

# Add user to the group
aws iam add-user-to-group --user-name cloudresumechallenge-user --group-name cloudresumechallenge

# Create access keys for the user
aws iam create-access-key --user-name cloudresumechallenge-user
```
