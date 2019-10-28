# Migrate Zagster CSV data into a SQLite database table.
# By the CS 160 Mob, October 2018
import sqlite3
import csv
db = sqlite3.connect("zagster.sqlite3.db")
with open('all.csv', 'r') as sample_csv:
lines = csv.reader(sample_csv, delimiter=',')
 for row in lines:
 user_id = row[0]
 rental_id = row[1]
 start_lat = row[2]
 if start_lat == "":
 start_lat = "NULL"
 start_lon = row[3]
 if start_lon == "":
 start_lon = "NULL"
 end_lat = row[4]
 if end_lat == "":
 end_lat = "NULL"
 end_lon = row[5]
 if end_lon == "":
 end_lon = "NULL"
 start_time = row[6]
 end_time = row[7]
 membership_name = row[8]
 sql_insert = f"""
 INSERT INTO rides(user_id, rental_id, start_lat, start_lon,
 end_lat, end_lon, start_time, end_time,
 membership_name)
 VALUES ("{user_id}", "{rental_id}", {start_lat}, {start_lon},
 {end_lat}, {end_lon}, "{start_time}", "{end_time}",
 "{membership_name}");
 """
 db.execute(sql_insert)
 db.commit()
db.close()