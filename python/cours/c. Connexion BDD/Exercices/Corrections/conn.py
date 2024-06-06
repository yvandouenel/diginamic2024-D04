###########
# IMPORTS #
###########

import mysql.connector

########################
# Établir la connexion #
########################

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
    # database="librairie"
)

cursor = conn.cursor()

#########################
# creation bdd et table #
#########################

cursor.execute("CREATE DATABASE IF NOT EXISTS ma_base_de_donnees")
cursor.execute("USE ma_base_de_donnees")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS ma_table (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nom VARCHAR(255),
        age INT
    )
""")
conn.commit()

########
# CRUD #
########

# # Insérer des données dans la table
cursor.execute("INSERT INTO ma_table (nom, age) VALUES ('John Doe', 25)")
cursor.execute("INSERT INTO ma_table (nom, age) VALUES ('Robin Hotton', 23)")
# conn.commit()

cursor.execute("UPDATE ma_table SET age = 42 WHERE nom = 'John Doe'")
cursor.execute("DELETE FROM ma_table WHERE nom = 'Robin Hotton'")
conn.commit()


cursor.execute("SELECT * FROM ma_table")
resultat = cursor.fetchall()
for row in resultat:
    print(row)

#############
# Fermeture #
#############

cursor.close()
conn.close()