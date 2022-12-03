# Jenkins with ansible

- This example has 3 services
  - `Jenkins` server with ansible installed
  - `Ubuntu` OSRemote host machine with mysql cli and aws cli installed
  - `MySQL server`

## Credentials

- `jenkins`
  - user: admin
  - password: 123
- `ubuntu`
  - user: ubuntu
  - password: 123
- `mysql`
  - user: root
  - password: 123

## Ansible Inventory

- Create a folder `ansible` in the jenkins_home folder
- Copy the `ubuntu-key` to the jenkins_home

- Inventory is the file in which is defined all the `hosts` and how to connect to them
- <https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html>
- Groups are defined with squared brackets []

```txt
[all:vars]

ansible_connection = ssh

[test]
myremotehost ansible_host=ubuntu ansible_user=ubuntu ansible_private_key_file=/var/jenkins_home/ansible/ubuntu-key
```

- Copy the `hosts` file into the jenkins_home/ansible folder
- Connect with the jenkins-ansible container!

```shell
ansible -i "hosts-file" -m "command" "host-alias"
ansible -i "./hosts" -m "ping" "myremotehost"
```

## Ansible Playbook

- `Playbook` is a script that defines all the things that ansible must do
- <https://docs.ansible.com/ansible/latest/user_guide/playbooks.html>

```yaml
- hosts: myremotehost #  host to execute the task
  tasks:
    - shell: echo Hello World > /tmp/hello.txt # task as a shell script
```

- Run playbook

```shell
ansible-playbook -i "hosts-file" "playbook-file"
ansible-playbook -i "./hosts" "./playbook.yaml"
```

## Ansible plugin for Jenkins

- Manage Jenkins -> Manage Plugins
  - `Ansible plugin`
- New Item -> Build -> `Invoke Ansible Playbook`
  - Insert playbook and hosts paths
  - Add extra variables - key (variable for ansible), value (variable from jenkins parameter $MYVAR)
- Colored output in jenkins
  - `AnsiColor plugin`
  - `Color ANSI Console Output` in Build Environment and `Colorized stdout` in Build

## Copy the script to copy txt into database into db-host container

```shell
docker cp ./people.txt db-host:/tmp
docker cp ./put.sh db-host:/tmp
```

## Playbook jenkins->db

```txt
[all:vars]
ansible_connection = ssh

[test]
test1 ansible_host=remote-host ansible_user=ubuntu ansible_private_key_file=/var/jenkins_home/ansible/ubuntu-key
web1 ansible_host=web ansible_user=ubuntu ansible_private_key_file=/var/jenkins_home/ansible/ubuntu-key
```

```shell
# Test connection
ansible -m ping -i hosts web1
ansible -m ping -i hosts all
```

```yaml
# This playbook update the table in the mysql container

- hosts: web1
  tasks:
    - name: Transfer template to web server
      template:
        src: table.j2
        dest: /var/www/html/index.php
```

```shell
# Run playbook
ansible-playbook -i hosts people.yml -e "PEOPLE_AGE=25" # -e specify parameters
```
