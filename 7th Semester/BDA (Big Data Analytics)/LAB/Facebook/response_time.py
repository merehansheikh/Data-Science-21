import mysql.connector
import time
import matplotlib.pyplot as plt


def establish_connection():
    return mysql.connector.connect(
        host="localhost", 
        user="root",  
        password="####",
        database="facebook"  
    )

# Fetch member's articles with limit n
def fetch_member_articles(member_id, n):
    db_conn = establish_connection()
    db_cursor = db_conn.cursor()

    start_time = time.time()
    db_cursor.execute('''
    SELECT article_id, body, created_at
    FROM Articles
    WHERE author_id = %s
    LIMIT %s
    ''', (member_id, n))
    articles = db_cursor.fetchall()
    end_time = time.time()

    db_conn.close()
    return end_time - start_time  

# Fetch feedback with limit n
def fetch_article_feedback(article_id, n):
    db_conn = establish_connection()
    db_cursor = db_conn.cursor()

    start_time = time.time()
    db_cursor.execute('''
    SELECT Feedback.comment, Members.full_name, Feedback.commented_at
    FROM Feedback
    JOIN Members ON Feedback.commenter_id = Members.member_id
    WHERE Feedback.article_id = %s
    LIMIT %s
    ''', (article_id, n))
    feedbacks = db_cursor.fetchall()
    end_time = time.time()

    db_conn.close()
    return end_time - start_time  

# Fetch reactions with limit n
def fetch_article_reactions(article_id, n):
    db_conn = establish_connection()
    db_cursor = db_conn.cursor()

    start_time = time.time()
    db_cursor.execute('''
    SELECT Members.full_name, Reactions.reacted_at
    FROM Reactions
    JOIN Members ON Reactions.reactor_id = Members.member_id
    WHERE Reactions.article_id = %s
    LIMIT %s
    ''', (article_id, n))
    reactions = db_cursor.fetchall()
    end_time = time.time()

    db_conn.close()
    return end_time - start_time  

# Fetch member feed with limit n
def fetch_member_feed(member_id, n):
    db_conn = establish_connection()
    db_cursor = db_conn.cursor()

    start_time = time.time()
    db_cursor.execute('''
    SELECT Articles.article_id, Articles.body, Articles.created_at, Members.full_name
    FROM Articles
    JOIN Members ON Articles.author_id = Members.member_id
    WHERE Articles.author_id != %s
    ORDER BY Articles.created_at DESC
    LIMIT %s
    ''', (member_id, n))
    feed = db_cursor.fetchall()
    end_time = time.time()

    db_conn.close()
    return end_time - start_time  

# Step 3: Measure and Plot Query Times

def measure_query_performance():
    n_values = [1000, 10000, 500000  ]  
    member_id = 1
    article_id = 1

    # Measure time for each query with different n values
    article_times = [fetch_member_articles(member_id, n) for n in n_values]
    feedback_times = [fetch_article_feedback(article_id, n) for n in n_values]
    reaction_times = [fetch_article_reactions(article_id, n) for n in n_values]
    feed_times = [fetch_member_feed(member_id, n) for n in n_values]

    # Plotting the results using matplotlib
    plt.figure(figsize=(10, 6))
    
    plt.plot(n_values, article_times, label='Articles Query Time', marker='o')
    plt.plot(n_values, feedback_times, label='Feedback Query Time', marker='o')
    plt.plot(n_values, reaction_times, label='Reactions Query Time', marker='o')
    plt.plot(n_values, feed_times, label='Feed Query Time', marker='o')
    
    plt.xlabel('Number of Records (n)')
    plt.ylabel('Query Time (seconds)')
    plt.title('Query Performance for Varying n Values')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    measure_query_performance()
