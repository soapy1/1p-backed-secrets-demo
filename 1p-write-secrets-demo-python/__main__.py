import pulumi
import pulumi_github as github
import pulumi_onepassword as onepassword

# get pulumi sample secret
example = onepassword.get_item(vault="pulumi",
    uuid="demo-api-cred")

# create secret in GH
example_secret_actions_secret = github.ActionsSecret(
    "exampleSecretActionsSecret",
    repository="1p-backed-secrets-demo",
    secret_name="example_secret_from_1password",
    plaintext_value=example.credential
)
