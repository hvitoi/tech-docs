# pulumi new

- Creates a project from a template
- By default this command creates the `state of each stacks` at `~/.pulumi/stacks`
- Make sure to `pulumi login` first
- Cached templates are stored at `~/.pulumi/templates`

```shell
# Show available templates
pulumi new

# Based on a template
pulumi new "aws-go" # built-in minimal AWS go pulumi program
pulumi new "aws-go" --name "foo" # project name (prompt if not specified)
pulumi new "aws-go" --description "foo" # project description (prompt if not specified)
pulumi new "aws-go" --dir "/path/to/dir" # path at which the files will be created
pulumi new "aws-go" --generate-only # generate the project only (do not create stack, save config or install deps)
pulumi new "aws-go" --force # force creating the files when the directory is not empty

# Use a remote template
pulumi new git@github.com:foo/pulumi-templates.git/aws-go

# with config
pulumi new "aws-go" --config="aws:region=us-west-2"
```
