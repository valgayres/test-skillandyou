import sqlite3
import random

con = sqlite3.connect("test.db")

con.execute(
    """
        CREATE TABLE IF NOT EXISTS survey_answers(
            id INTEGER PRIMARY KEY,
            student_id INTEGER,
            survey_id INTEGER,
            question_id INTEGER,
            question TEXT,
            answer TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """
)

con.execute(
    """
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY,
            name TEXT,
            course_name TEXT
        )
    """
)

students = [
    ('Alice', 'Python'),
    ('Bob', 'Python'),
    ('Heidi', 'Ruby'),
    ('Ivan', 'Ruby'),
    ('Judy', 'Ruby'),
    ('Oscar', 'JavaScript'),
    ('Peggy', 'JavaScript'),
    ('Eve', 'Python'),
    ('Trent', 'Ruby'),
    ('Victor', 'JavaScript')
]
con.execute("DELETE FROM students")
con.executemany("""
    INSERT INTO students(name, course_name)
    VALUES (?, ?);
""", students)

surveys = [
    {
        "id": 1,
        "questions": [
            {"id": 1, "question": "Did you enjoy the course?"},
            {"id": 2, "question": "Do you think the course was too long?"},
            {"id": 3, "question": "Provide some feedbacks?"},
        ]
    },
    {
        "id": 2,
        "questions": [
            {"id": 1, "question": "Did you get a job after the course?"},
            {"id": 2, "question": "If yes, what is your job title?"},
            {"id": 3, "question": "If no, what are you doing now?"},
        ]
    }
]

feedbacks_sample = [
    "I found the course extremely interesting, and it really helped me understand my future job.",
    "The teachers are competent and were always willing to help the students, which made the learning process enjoyable.",
    "This course is interesting and has provided me with valuable insights into the industry.",
    "I appreciate how the teachers are competent and helping the students throughout the course.",
    "The course is helping me understand my future job, and I feel more prepared now.",
    "Unfortunately, the course is too long and felt dragged out at times.",
    "I think the course is too complex, and some topics were hard to grasp.",
    "The teachers are not helping enough, and I often felt lost during the lessons.",
    "The course is too long and requires more concise material.",
    "It's unfortunate that the teachers are not helping enough; assistance was minimal.",
    "I enjoyed the course because it is interesting and engaging.",
    "The course is helping me understand my future job, making me more confident.",
    "The teachers are competent and always helping the students succeed.",
    "I felt that the course is too complex for beginners like me.",
    "The course is too long, which made it hard to stay focused.",
    "The teachers are not helping enough, leaving many questions unanswered.",
    "I found the course interesting and it kept me engaged throughout.",
    "The teachers are competent and provide excellent guidance to the students.",
    "The course is too complex, and I struggled to keep up with the pace.",
    "The course is interesting and is helping me understand my future job prospects.",
    "I believe the teachers are competent and always helping the students with their queries.",
    "Sadly, the course is too long and I lost interest halfway through.",
    "The teachers are not helping enough, making the course feel even more complex.",
    "The course is helping me understand my future job and the skills required.",
    "I think the course is too complex, and additional resources are needed.",
    "The teachers are competent and helping the students grasp difficult concepts.",
    "The course is interesting and has broadened my understanding of the field.",
    "The course is too long and could be condensed into a shorter timeframe.",
    "I feel that the teachers are not helping enough, which affects the learning experience.",
    "Overall, the course is interesting and is helping me prepare for my future career."
]
other_feedbacks = [
    "The course provided a good balance between theory and practical application.",
    "I appreciated the hands-on projects that allowed us to apply what we learned.",
    "The course schedule was convenient and fit well with my other commitments.",
    "I found the course materials to be well-organized and easy to follow.",
    "The instructors were knowledgeable and presented the material clearly.",
    "I would have liked more opportunities for group discussions and collaboration.",
    "The course exceeded my expectations in terms of content and delivery.",
    "Some topics could benefit from more in-depth exploration.",
    "The online resources and supplementary materials were very helpful.",
    "I think the course could include more real-world examples to enhance understanding.",
    "The learning environment was supportive and encouraged participation.",
    "I felt that the assessments accurately reflected the course content.",
    "The course pacing was appropriate and kept me engaged throughout.",
    "I would recommend this course to others interested in the subject.",
    "I appreciated the timely feedback on assignments from the instructors.",
    "Additional guest lectures from industry professionals would be beneficial.",
    "The course helped me develop new skills and improve my knowledge.",
    "I enjoyed the interactive elements such as quizzes and live coding sessions.",
    "Some technical issues with the online platform hindered the learning experience.",
    "The course met my learning objectives and provided valuable insights.",
    "I believe the course content is up-to-date with current industry trends.",
    "I would have preferred more personalized feedback on my performance.",
    "The overall structure of the course was logical and easy to follow.",
    "I found the study materials accessible and comprehensive.",
    "The course inspired me to pursue further studies in this field.",
    "I appreciated the diversity of topics covered in the course curriculum.",
    "The collaborative projects were a highlight and enhanced my learning.",
    "I think incorporating more multimedia content could improve the course.",
    "The workload was manageable alongside my other responsibilities.",
    "I felt well-prepared for the final assessment due to the course content."
]
all_feedbacks = feedbacks_sample + other_feedbacks

# Generate at least 50 answers
answers = []

# Get student IDs from the database
cursor = con.execute("SELECT id FROM students")
student_ids = [row[0] for row in cursor.fetchall()]

for student_id in student_ids:
    for survey in surveys:
        survey_id = survey["id"]
        got_job = None  # For tracking the answer to "Did you get a job after the course?"
        for question in survey["questions"]:
            question_id = question["id"]
            question_text = question["question"]
            # Generate an answer based on the question
            if question_text == "Did you enjoy the course?":
                answer_text = random.choice(["Yes", "No"])
            elif question_text == "Do you think the course was too long?":
                answer_text = random.choice(["Yes", "No"])
            elif question_text == "Provide some feedbacks?":
                # Provide multiple feedbacks to increase the total number of answers
                feedbacks = random.sample(
                    all_feedbacks, k=2)  # Choose 2 feedbacks
                for feedback in feedbacks:
                    answers.append(
                        (student_id, survey_id, question_id, question_text, feedback))
                continue  # Skip adding the answer below since we've added multiple
            elif question_text == "Did you get a job after the course?":
                got_job = random.choice(["Yes", "No"])
                answer_text = got_job
            elif question_text == "If yes, what is your job title?":
                if got_job == "Yes":
                    answer_text = random.choice(
                        ["Software Engineer", "Data Analyst", "Web Developer"])
                else:
                    continue  # Skip this question if the student didn't get a job
            elif question_text == "If no, what are you doing now?":
                if got_job == "No":
                    answer_text = random.choice(
                        ["Looking for a job", "Continuing education", "Freelancing"])
                else:
                    continue  # Skip this question if the student got a job
            else:
                answer_text = "N/A"
            answers.append((student_id, survey_id, question_id,
                           question_text, answer_text))

con.execute("DELETE FROM survey_answers")
con.executemany("""
    INSERT INTO survey_answers(student_id, survey_id, question_id, question, answer)
    VALUES (?, ?, ?, ?, ?)
""", answers)
con.commit()
