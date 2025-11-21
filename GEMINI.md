# GEMINI.md

## Directory Overview

This directory contains a collection of SQL scripts designed for learning and practicing database concepts. The project is structured to provide basic examples, exercises (quests), and potentially templates for SQL operations. The scripts are written in standard SQL, with some comments in Korean within the quest files.

## Key Files

*   **`sqls/create_tables.sql`**: Defines the initial `Persons` table, which serves as a basic schema for many of the other SQL scripts.
*   **`sqls/insert_into_values.sql`**: Provides an example of how to insert data into the `Persons` table.
*   **`sqls/seleci_forms.sql`**: (Note the typo in the filename) Demonstrates various `SELECT` statements to query data from the `Persons`table.
*   **`sqls/updates.sql`**: Shows the syntax for updating records in a table.
*   **`sqls/deletes.sql`**: Provides an example of how to delete records from a table.
*   **`quests/10_DMLs/10_DMLs_1.sql`**: A self-contained exercise or "quest" that involves creating a `news_articles` table, inserting data, and then performing `SELECT`, `UPDATE`, and `DELETE` operations. The instructions are commented in Korean.
*   **`sqls/webscrapings_databases.sql`**: Contains `CREATE TABLE` statements for schemas related to storing web scraping results.

## Usage

This directory is intended for educational purposes for someone studying SQL. A typical workflow would be:

1.  **Setup**: Use a SQL client or database command line to connect to a database.
2.  **Schema Creation**: Execute the script in `sqls/create_tables.sql` to create the initial `Persons` table. You can also create the tables from `sqls/webscrapings_databases.sql` if you are working on the web scraping exercises.
3.  **Data Population**: Run the `sqls/insert_into_values.sql` script to add sample data.
4.  **Learning**: Examine the scripts in the `sqls` directory to understand basic SQL commands.
5.  **Practice**: Work through the exercises in the `quests` directory to test your SQL knowledge.
