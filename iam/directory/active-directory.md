# Active Directory

- Active Directory (AD) is a directory service developed by Microsoft
- It is a centralized `database` that stores information about users, groups, computers, and other resources in a Windows domain.
- It's a centralized `identity management` (create accounts, assign permissions, etc)

## Architecture

- `Objects` are organized in `trees`, a group of trees is a `forest`
- Objects
  - Users
  - Accounts
  - Computers
  - Printers
  - File Shares
  - Security Groups

## Login Management

- The `user information` is stored in the `Domain Controller` and it can be used to log in in any machine that is connected to the domain controller

## Integration

- **Kerberos**
- **NTLM**
- **LDAP**
  - Non-Windows systems or applications often integrate with AD using `LDAP` to authenticate users or access directory data.
