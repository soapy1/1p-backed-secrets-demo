# 1Password backed secrets demo

This repo has some experiments for using 1Password as a secrets database for github actions.

Included in this repo:

## A GH action that reads from 1Password 

[`.github/workflows/use-1password-secrets`](https://github.com/soapy1/1p-backed-secrets-demo/blob/main/.github/workflows/use-1password-secrets.yaml)

This outlines how you can connect a GH action to 1Password to read things like tokens. So, repo owners just need to maintain one GH secret (1Password service account access token) in order to access all other available secrets.

1Password docs: https://developer.1password.com/docs/ci-cd/github-actions/

### Setup steps

* create a 1Password service account (this account should have scoped down permissions, so this repo only has access to the appropriate set of secrets)
* add a GH secret `OP_SERVICE_ACCOUNT_TOKEN`
* add a demo secret to 1Password

### Try it out

* create and push a branch names with following the pattern "demo-read-secrets-*"
* observe the run github action that loads the secret, and outputs a log. Note, the secret is automatically censored when it is output in the logs 

## Use Pulumi to populate GHA with secrets

This outlines how to use Pulumi to read from 1Password and push them to other CI services like GHA.

### Running locally

* Install the 1password cli
* Export environment variables:
  * `GITHUB_TOKEN` (this GH token should have read/write access to this repo's secrets)
  * `OP_SERVICE_ACCOUNT_TOKEN` (token for 1password service account)
*  Setup pulumi (only needs to be run once)
```
$ pulumi install
$ pulumi plugin install resource onepassword --server github://api.github.com/1Password/pulumi-onepassword
```
* Apply changes
```
$ pulumi up
```
