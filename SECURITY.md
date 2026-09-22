# Coursework security

Do not commit passwords, authentication codes, recovery codes, personal access
tokens, Secure Shell private keys, database credentials, `.env` files, or private
student information.

If a secret is committed, removing it from the latest file is not sufficient
because Git history may still contain it. Immediately revoke or rotate the secret
through the service that issued it, then notify the instructor through the
university's private communication channel. Do not publish the secret in an issue.

Report suspected vulnerabilities in supplied course code privately to the
instructor. Student repositories must remain private unless the course policy
explicitly states otherwise.
