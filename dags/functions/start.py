import os
import subprocess
from functions import utils

def migratedb():

    conf = utils.get_destination_database_config()
    gomigrate_uri = utils.gomigrate_create_uri(conf)+"?sslmode=disable"
    parent_dirname = os.path.dirname(__file__)
    migration_dirname = os.path.join(parent_dirname, "/opt/airflow/dags/migrations")

    try:
        output = subprocess.check_output(
            f'/opt/airflow/dags/functions/migrate -path {migration_dirname} -database {gomigrate_uri} up',
            stderr=subprocess.STDOUT,
            shell=True,
            timeout=120,
            universal_newlines=True
        )
    except subprocess.CalledProcessError as exc:
        print("Status: FAIL", "\n", exc.returncode, "\n", exc.output)

        raise Exception("migration FAIL") from None
    else:
        print("Output: \n{}\n".format(output))
    