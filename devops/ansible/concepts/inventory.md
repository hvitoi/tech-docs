# Ansible Inventory

- Inventory is the file in which is defined all the `hosts` and how to connect to them
- <https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html>
- Groups are defined with squared brackets []
- Inventory file is usually called **hosts**

```txt
[all:vars]
ansible_connection = ssh

[test]
remotehost ansible_host=ubuntu ansible_user=ubuntu ansible_private_key_file=/var/jenkins_home/ansible/ubuntu-key
webserver ansible_host=nginx ansible_user=root ansible_private_key_file=/var/jenkins_home/ansible/nginx-key
```

```sh
ansible -i "hosts-file" -m "command" "host-alias"
ansible -i "./hosts" -m "ping" "remotehost"
```
