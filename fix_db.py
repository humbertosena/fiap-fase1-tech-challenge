import sqlite3
conn = sqlite3.connect('mlflow.db')
conn.execute("UPDATE alembic_version SET version_num = 'c3d6457b6d8a'")
conn.commit()
conn.close()
