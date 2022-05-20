# Ambari

- Ambari is a tool to manage and visualize a hadoop cluster
- Ambari can also be used to install the other hadoop components. First installing ambari and then from it the hadoop cluster

- Usernames
  - Reset the admin password with `ambari-admin-password-reset` (via shell root:hadoop)
  - You can also use the default `maria_dev:maria_dev` user

## Dashboard

- Ambari dashboard <http://localhost:8080/>
- Overviews about services and important metrics

## Services

- Allows configuring an individual hadoop component

## Hosts

- Machines that compose the hadoop cluster
- Namenodes and Datanodes

## Alerts

- Email you when something goes wrong
  - E.g., HDFS storage capacity

## Admin

- Check installed services
- Service accounts
- Authentication methods

## Views

<http://localhost:8080/#/main/views>

- **Files View**

  - Interactively explore the HDFS

- **Hive View**

  - Movielens 100k dataset: <https://grouplens.org/datasets/movielens/>
  - Import it using Hive View at `upload table` tab

- **Pig View**

  - Run pig scripts
