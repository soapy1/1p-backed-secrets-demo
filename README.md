# 1Password backed secrets demo

This repo has some experiments for using 1Password as a secrets database for github actions.

Included in this repo:

## A GH action that reads from 1Password 

[`.github/workflows/use-1password-secrets`](https://github.com/soapy1/1p-backed-secrets-demo/blob/main/.github/workflows/use-1password-secrets.yaml)

This outlines how you can connect a GH action to 1Password to read things like tokens.

1Password docs: https://developer.1password.com/docs/ci-cd/github-actions/

### Setup steps

* create a 1Password service account
* add a GH secret `OP_SERVICE_ACCOUNT_TOKEN`
* add a demo secret to 1Password

### Try it out

* create and push a branch names with following the pattern "demo-read-secrets-*"
* observe the run github action that loads the secret, and outputs a log. Note, the secret is automatically censored when it is output in the logs 

