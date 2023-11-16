-- Creating a Stored Procedure
/*Connect to the PostgreSQL database
psql -h pg.pg4e.com -p 5432 -U pg4e_73285570e1 pg4e_73285570e1 
*/
-- Create the table keyvalue

CREATE TABLE keyvalue ( 
  id SERIAL,
  key VARCHAR(128) UNIQUE,
  value VARCHAR(128) UNIQUE,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  PRIMARY KEY(id)
);

-- Add a stored procedure so that every time a record is updated, the updated_at variable is automatically set to the current time

-- Create the trigger function
CREATE OR REPLACE FUNCTION trigger_set_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create the trigger that fires the trigger function on UPDATE

CREATE TRIGGER set_updated_at
BEFORE UPDATE ON keyvalue
FOR EACH ROW
EXECUTE FUNCTION trigger_set_updated_at();

/* Check the details of the stored procedure

\df trigger_set_updated_at

List of functions
 Schema |          Name          | Result data type | Argument data types | Type 
--------+------------------------+------------------+---------------------+------
 public | trigger_set_updated_at | trigger          |                     | func
(1 row)

*/

