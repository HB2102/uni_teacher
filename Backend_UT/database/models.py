from database.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Float, CheckConstraint


# ID Class ==============================================================================================
class ID:
    __abstract__ = True
    id = Column(Integer, unique=True, index=True, primary_key=True)


# USER Class ================================================================================================
class User(Base, ID):
    __tablename__ = 'user'
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String, nullable=False)
    phone_number = Column(String(20), unique=True)
    email = Column(String, unique=True)
    is_admin = Column(Boolean, default=False)
    is_super_admin = Column(Boolean, default=False)
    is_banned = Column(Boolean, default=False)


# TEACHER Class =============================================================================================
class Teacher(Base, ID):
    __tablename__ = 'teacher'
    full_name = Column(String)
    total_average_score = Column(Float, default=None)
    average_teaching_score = Column(Float, default=None)
    average_behaviour_score = Column(Float, default=None)
    average_grading_score = Column(Float, default=None)
    number_of_comments = Column(Integer, default=0)
    teacher_pic = Column(String, nullable=True)
    pic_name = Column(String, nullable=True)


# UNIVERSITY Class ==========================================================================================
class University(Base, ID):
    __tablename__ = 'university'
    name = Column(String, unique=True, nullable=False)


# SUBJECT Class =============================================================================================
class Subject(Base, ID):
    __tablename__ = 'subject'
    name = Column(String, unique=True, nullable=False)


# COMMENT Class =============================================================================================
class Comment(Base, ID):
    __tablename__ = 'comment'
    user_id = Column(Integer, ForeignKey('user.id'))
    username = Column(String, ForeignKey('user.username'), nullable=False)
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    subject_id = Column(Integer, ForeignKey('subject.id'), nullable=True, default=None)
    text = Column(String, nullable=False)
    date_added = Column(DateTime, nullable=False)
    number_of_likes = Column(Integer, default=0)
    number_of_dislikes = Column(Integer, default=0)
    is_approved = Column(Boolean, default=False)


# TEACHER_UNI Class =========================================================================================
class TeacherUni(Base, ID):
    __tablename__ = 'teacher_uni'
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    university_id = Column(Integer, ForeignKey('university.id'))


# TEACHER_SUBJECT Class =====================================================================================
class TeacherSubject(Base, ID):
    __tablename__ = 'teacher_subject'
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    subject_id = Column(Integer, ForeignKey('subject.id'))


# COMMENT_ACTION Class ======================================================================================
class CommentAction(Base, ID):
    __tablename__ = 'comment_action'
    user_id = Column(Integer, ForeignKey('user.id'))
    comment_id = Column(Integer, ForeignKey('comment.id'))
    action = Column(Boolean)  # True means comment has been liked by user and False means it has been disliked


# RATING Class ==============================================================================================
class Rating(Base, ID):
    __tablename__ = 'rating'
    user_id = Column(Integer, ForeignKey('user.id'))
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    total_point = Column(Integer, CheckConstraint('total_point > 0 AND total_point < 6'), nullable=False)
    teaching_point = Column(Integer, CheckConstraint('total_point > 0 AND total_point < 6'), nullable=False)
    behaviour_point = Column(Integer, CheckConstraint('total_point > 0 AND total_point < 6'), nullable=False)
    grading_point = Column(Integer, CheckConstraint('total_point > 0 AND total_point < 6'), nullable=False)


# REQUEST Class =============================================================================================
class Request(Base, ID):
    __tablename__ = 'request'
    text = Column(String, nullable=False)
    phone_number = Column(String, nullable=True, default=None)
    date_added = Column(DateTime, nullable=False)
    is_reviewed = Column(Boolean, default=False)


# DELETED PICTURES Class ===================================================================================
class DeletedPics(Base, ID):
    __tablename__ = 'deleted_pics'
    name = Column(String, nullable=False)
    is_reviewed = Column(Boolean, default=False)


# REPORT COMMENTS Class ====================================================================================
class CommentReport(Base, ID):
    __tablename__ = 'comment_report'
    comment_id = Column(Integer, ForeignKey('comment.id'))
    reason = Column(String, nullable=True, default=None)
    date_added = Column(DateTime, nullable=False)
    is_reviewed = Column(Boolean, default=False)


# ADD TEACHER REQUEST Class ================================================================================
class AddTeacherRequest(Base, ID):
    __tablename__ = 'add_teacher_request'
    teacher_name = Column(String, nullable=False)
    phone_number = Column(String, nullable=True, default=None)
    uni_text = Column(String, nullable=True, default=None)
    subject_text = Column(String, nullable=True, default=None)
    description = Column(String, nullable=True, default=None)
    date_added = Column(DateTime, nullable=False)
    is_reviewed = Column(Boolean, default=False)


# ADD UNIVERSITY REQUEST Class =============================================================================
class AddUniRequest(Base, ID):
    __tablename__ = 'add_uni_request'
    university_names = Column(String, nullable=False)
    phone_number = Column(String, nullable=True, default=None)
    description = Column(String, nullable=True, default=None)
    date_added = Column(DateTime, nullable=False)
    is_reviewed = Column(Boolean, default=False)


# ADD SUBJECT REQUEST Class ================================================================================
class AddSubjectRequest(Base, ID):
    __tablename__ = 'add_subject_request'
    subject_names = Column(String, nullable=False)
    phone_number = Column(String, nullable=True, default=None)
    description = Column(String, nullable=True, default=None)
    date_added = Column(DateTime, nullable=False)
    is_reviewed = Column(Boolean, default=False)
