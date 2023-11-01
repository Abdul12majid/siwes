#db function

import psycopg2

def create_database_function(function_name, function_code):
  """Creates a database function in PostgreSQL.

  Args:
    function_name: The name of the function to create.
    function_code: The code for the function.
  """

  conn = psycopg2.connect("dbname=my_database user=my_user password=my_password")
  cur = conn.cursor()

  cur.execute("CREATE OR REPLACE FUNCTION {} AS {}".format(function_name, function_code))

  conn.commit()
  cur.close()
  conn.close()


def add_user_to_group(user_id, group_id):
  """Adds a user to a group in PostgreSQL.

  Args:
    user_id: The ID of the user to add to the group.
    group_id: The ID of the group to add the user to.
  """

  create_database_function("add_user_to_group", """
CREATE OR REPLACE FUNCTION add_user_to_group(user_id INT, group_id INT)
RETURNS VOID AS $$
BEGIN
  INSERT INTO group_members (user_id, group_id)
  VALUES ($1, $2);
END;
$$ LANGUAGE plpgsql;
""")

  cur = psycopg2.connect("dbname=my_database user=my_user password=my_password").cursor()
  cur.execute("SELECT add_user_to_group({}, {})".format(user_id, group_id))
  cur.close()


if __name__ == "__main__":
  add_user_to_group(1, 2)
