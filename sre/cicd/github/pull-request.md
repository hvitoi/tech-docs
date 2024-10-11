# Pull Request

- Pull request is a proposal of potential changes
- Why this name?
  - It's named `pull request` because it's like you are asking the other collaborators to pull your feature and avaliate it, a request to pull your changes from the remote branch and check it out and give feedbacks
  - `Pull request` is also when you want a main repository to `pull` the branch from your fork repository
- Pull request is a `environment for discussion`, after the discussion the feature branch can be merged into master or not
- Existing pull request is automatically updated when new commits are pushed to remote
- Pull requests can only be created in Github/GItlab website!

- **PR naming**: [`branch`]: `Description of the feature`
- **Merge pull request types**
  - `Create a merge commit`: just like a conventional merge (3-way), all the history of commits are preserved and the commit will have 2 parents (from base and feature branches)
  - `Squash and merge`
  - `Rebase and merge`

### Branch protection rules

- `Protected branch` is a branch that has some rules, for example to require PR to have certain `quantity of approves` before merging will be allowed
- It's interesting to make `rules` for the master branch and make it `protected` (Settings/Branches)
- `Rules`
  - Require pull request reviews before merging
  - Require status checks to pass before merging
  - Require signed commits
  - Require linear history
  - Include administrators
  - Allow force pushes
  - Allow deletions
