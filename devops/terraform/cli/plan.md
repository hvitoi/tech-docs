# plan

- See any changes to be applied to the infrastructure (diff)
- The `diff` is compared with the `real state` in the cloud

```shell
# plan
terraform plan

# output plan to a file
terraform plan -out "v1plan.out" # can be later applied using this plan file

# override variables
terraform plan -var "location=eastus"
terraform plan -var-file "terraform.tfvars"
```
