# README

This is a simple take on the [cloudresumechallenge.dev]

# How it works

- We have the infrastructure defined here
- We use terraform to provision
  - S3 to host the frontend
  - API Gateway
  - Lambda to act as our backend
  - DynamoDB on demand for the data store
