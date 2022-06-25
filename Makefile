
AIRFLOW_UID=50000

set-user:
	@sudo useradd -u 50000 -g root airflow
	@sudo usermod -a -G root airflow
	
set-perms:
	@chown -R airflow:airflow dags

run:
	@docker-compose up --build