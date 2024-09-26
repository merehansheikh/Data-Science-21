import mysql.connector
import random
import datetime

def establish_connection():
    return mysql.connector.connect(
        host="localhost", 
        user="root",  
        password="####",
        database="facebook"  
    )

def generate_members(total_members):
    db_conn = establish_connection()
    db_cursor = db_conn.cursor()

    first_names = ['Lucas', 'Emily', 'Olivia', 'Henry', 'Sophia', 'James', 'Zara', 'Liam', 'Ella', 'David']
    last_names = ['Anderson', 'Johnson', 'Smith', 'Lee', 'Brown', 'Davis', 'Clark', 'Garcia', 'Wilson', 'Walker']
    email_domains = ['myemail.com', 'webmail.net', 'sample.org', 'inbox.com']

    members = []
    for i in range(total_members):
        full_name = f"{random.choice(first_names)} {random.choice(last_names)}"
        email = f"{full_name.replace(' ', '').lower()}{i}@{random.choice(email_domains)}"
        members.append((full_name, email))

    db_cursor.executemany('INSERT INTO Members (full_name, contact_email) VALUES (%s, %s)', members)
    db_conn.commit()
    db_conn.close()

def generate_articles(total_articles):
    db_conn = establish_connection()

    db_cursor = db_conn.cursor()

    db_cursor.execute('SELECT member_id FROM Members')
    member_ids = [record[0] for record in db_cursor.fetchall()]

    post_contents = [
        'Loving this weather!', 'Just started a new project.', 'Can’t believe the news today.', 'Feeling great!',
        'Just finished a marathon!', 'Looking forward to the holidays.', 'What a fantastic day!', 'Life is beautiful.',
        'Had an amazing lunch!', 'Ready for the weekend!'
    ]

    articles = []
    for _ in range(total_articles):
        member_id = random.choice(member_ids)
        content = random.choice(post_contents)
        created_at = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 365))
        articles.append((member_id, content, created_at))

    db_cursor.executemany('INSERT INTO Articles (author_id, body, created_at) VALUES (%s, %s, %s)', articles)
    db_conn.commit()
    db_conn.close()

def generate_feedbacks(total_feedbacks):
    db_conn = establish_connection()

    db_cursor = db_conn.cursor()

    db_cursor.execute('SELECT article_id FROM Articles')
    article_ids = [record[0] for record in db_cursor.fetchall()]

    db_cursor.execute('SELECT member_id FROM Members')
    member_ids = [record[0] for record in db_cursor.fetchall()]

    feedback_contents = [
        'Great post!', 'Totally agree.', 'Couldn’t have said it better.', 'Interesting point of view.', 'Thanks for sharing!',
        'Well said!', 'This is awesome!', 'Couldn’t agree more.', 'Fantastic!', 'Loved it!'
    ]

    feedbacks = []
    for _ in range(total_feedbacks):
        article_id = random.choice(article_ids)
        member_id = random.choice(member_ids)
        feedback_text = random.choice(feedback_contents)
        commented_at = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 365))
        feedbacks.append((article_id, member_id, feedback_text, commented_at))

    db_cursor.executemany('INSERT INTO Feedback (article_id, commenter_id, comment, commented_at) VALUES (%s, %s, %s, %s)', feedbacks)
    db_conn.commit()
    db_conn.close()

def generate_reactions(total_reactions):
    db_conn = establish_connection()

    db_cursor = db_conn.cursor()

    db_cursor.execute('SELECT article_id FROM Articles')
    article_ids = [record[0] for record in db_cursor.fetchall()]

    db_cursor.execute('SELECT member_id FROM Members')
    member_ids = [record[0] for record in db_cursor.fetchall()]

    reactions = []
    for _ in range(total_reactions):
        article_id = random.choice(article_ids)
        member_id = random.choice(member_ids)
        reacted_at = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 365))
        reactions.append((article_id, member_id, reacted_at))

    db_cursor.executemany('INSERT INTO Reactions (article_id, reactor_id, reacted_at) VALUES (%s, %s, %s)', reactions)
    db_conn.commit()
    db_conn.close()

if __name__ == '__main__':
    total_members = 1000  
    total_articles = 10000 
    total_feedbacks = 500000  
    total_reactions = 200000  
    print("Populating Members table...")
    generate_members(total_members)
    print("Populating Articles table...")
    generate_articles(total_articles)
    print("Populating Feedback table...")
    generate_feedbacks(total_feedbacks)
    print("Populating Reactions table...")
    generate_reactions(total_reactions)
    print("Database population complete.")
