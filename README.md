# Airflow_dags

# SubDAGs
**Overview**

SubDAGs (SubDAGOperators) in Apache Airflow allow you to encapsulate and organize a group of tasks within a DAG. This is particularly useful when you have a set of related tasks that you want to group together, making your DAGs more modular and easier to manage.

# TaskGroups
**Overview**

TaskGroups in Apache Airflow provide another way to organize and visually group related tasks within a DAG. They offer a higher-level abstraction for grouping tasks than SubDAGs and are particularly useful for organizing tasks within a single DAG file.

# XComs
It stands for cross communication and it's nothing more than a little package that allows you to exchange
small amount of data.
You should not share terabytes or gigabytes of data.
