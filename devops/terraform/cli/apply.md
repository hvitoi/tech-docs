# apply

- Apply diff to the infrastructure
- When applying a diff, the `terraform.tfstate` file is updated
- Terraform state file is locked while the changes are being applied

```sh
# plan and apply
terraform apply

# apply from a plan file
terraform apply "v1plan.out"

# override variables
terraform apply -var "location=eastus"
terraform apply -var-file "terraform.tfvars"
```
