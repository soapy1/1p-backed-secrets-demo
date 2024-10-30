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

Try either:
* Python flavour in ./1p-write-secrets-demo-python
* YAML flavour ./1p-write-secrets-demo-yaml

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

### Try it out with GHA

[`.github/workflows/push-1password-secrets-to-gha`](https://github.com/soapy1/1p-backed-secrets-demo/blob/main/.github/workflows/push-1password-secrets-to-gha.yaml)

This workflow shows how you can use pulumi to pull secrets from 1password and push them to a github repo. In this demo, we are just pushing to this repo. However, you should be able to extend this to push to any repo you have access to (access is determined by the GH token provided to the CI).

Try it out by:
* create and push a branch names with following the pattern "demo-push-secrets-*"
* observe the run in github action that populates a secret in this repo

#### Some notes about setting this up

* in order for pulumi to work in GHA, the action needs a way access the pulumi back end. This can be done (either) by:
  * adding a `PULUMI_ACCESS_TOKEN` as a secret to GH
  * setting up OIDC (eg. https://www.pulumi.com/docs/pulumi-cloud/access-management/oidc/client/github/)

* in order for pulumi to write secrets to GH, it must auth with GH. This can be done (either by):
  * adding a `GITHUB_TOKEN` as a secret to GH
  * pulling the github token from 1password
  * configuring the pulumi github app