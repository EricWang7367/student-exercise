import argparse

import psycopg2


def truncate(database, user, password, host, port):
    try:
        with psycopg2.connect(database=database, user=user, password=password, host=host, port=port) as conn:
            with conn.cursor() as cur:
                cur.execute("TRUNCATE register CASCADE")
                rows_deleted = cur.rowcount
            # commit the changes to the database
            conn.commit()
            print("Complete")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Truncates the local database")
    parser.add_argument("--host", type=str, default="localhost")
    parser.add_argument("--port", type=int, default=5432)
    parser.add_argument("--database_name", type=str, default="db")
    parser.add_argument("-u", "--user", type=str, required=True)
    parser.add_argument("-p", "--password", type=str, required=True)
    args = parser.parse_args()
    truncate(database=args.database_name, user=args.user, password=args.password, host=args.host, port=args.port)
