# Ansible Playbook

- `Playbook` is a script that defines all the things that ansible must do
- <https://docs.ansible.com/ansible/latest/user_guide/playbooks.html>

```yaml
- hosts: remotehost #  host to execute the task
  tasks:
    - shell: echo Hello World > /tmp/hello.txt # task as a shell script
    - debug:
        msg: "{{ MSG }}" # Log message out
- hosts: webserver
  tasks:
    - name: Transfer template to web server
      template:
        src: table.j2
        dest: /var/www/html/index.php
```

- Run playbook

```sh
ansible-playbook -i "hosts-file" "playbook-file"
ansible-playbook -i "./hosts" "./playbook.yaml" -e "PEOPLE_AGE=25" # -e for parameters
```
