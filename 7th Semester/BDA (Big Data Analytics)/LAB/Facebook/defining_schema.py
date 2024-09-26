import mysql.connector

def setup_database():
    # Connect to MySQL database
    connection = mysql.connector.connect(
        host="localhost", 
        user="root",  
        password="####",  
        database="facebook" 
    )
    
    cur = connection.cursor()

    # Members table
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Members (
        member_id INT PRIMARY KEY AUTO_INCREMENT,
        full_name VARCHAR(255) NOT NULL,
        contact_email VARCHAR(255) NOT NULL UNIQUE
    )
    ''')

    # Articles table
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Articles (
        article_id INT PRIMARY KEY AUTO_INCREMENT,
        author_id INT NOT NULL,
        body TEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (author_id) REFERENCES Members(member_id) ON DELETE CASCADE
    )
    ''')

    # Feedback table
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Feedback (
        feedback_id INT PRIMARY KEY AUTO_INCREMENT,
        article_id INT NOT NULL,
        commenter_id INT NOT NULL,
        comment TEXT NOT NULL,
        commented_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (article_id) REFERENCES Articles(article_id) ON DELETE CASCADE,
        FOREIGN KEY (commenter_id) REFERENCES Members(member_id) ON DELETE CASCADE
    )
    ''')

    # Reactions table
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Reactions (
        reaction_id INT PRIMARY KEY AUTO_INCREMENT,
        article_id INT NOT NULL,
        reactor_id INT NOT NULL,
        reacted_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (article_id) REFERENCES Articles(article_id) ON DELETE CASCADE,
        FOREIGN KEY (reactor_id) REFERENCES Members(member_id) ON DELETE CASCADE
    )
    ''')

    connection.commit()
    connection.close()

if __name__ == '__main__':
    setup_database()
