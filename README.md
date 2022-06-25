To run this program, please make sure to have `make` and `docker-compose` installed in your computer

step to run:
- make set-user
- make set-perms
- make run

to load the dataset, I use apache airflow which runs every 1 hour, but you also can trigger the tasks manually

to trigger the tasks, below is the step:
- open airflow web by accessing localhost:5884
- enter username: `airflow` and password `airflow`
- click arrow button on the right side

I think the user of this DWH would be business analyst, so I created 2 presentation tables other than the tables of the dataset, which are:
- monthly total purchase per products
- monthly best seller products (top 10)

to check the data in the db (postgresql):
- username: airflow
- password: airflow
- database name: olist