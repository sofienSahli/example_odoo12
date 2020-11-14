from .... import models, fields


class Student (models.Model):
    _name = "student"
    _description = "student basic information"

    student_name = fields.Char(String="student name", required=True)
    student_age = fields.Integer("Age")
    student_birth_date = fields.Date("Birth_date")
    student_email = fields.Char(String="Email")
    student_image = fields.Binary(String="image")
