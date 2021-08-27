from odoo import fields, models


class CourseDetail(models.Model):
    _name = 'course.detail'
    
    name = fields.Char(required=True)

    instructor_id = fields.Many2one(
        comodel_name='res.partner',
        string='Instructor',
        domain="[('contact_type', '=', 'instructor')]",
        required=True
        )
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Instructor',
        
        required=True
        )
    description = fields.Text(string='Description')
    lesson_ids = fields.One2many('course.lesson', 'course_id', string="Lessons")
    attendee_ids = fields.One2many('res.partner', 'course_id', string="Attendees")
    course_line_ids = fields.One2many('course.line', 'course_id', string="Attendees")

    
class CourseLine(models.Model):
    _name = 'course.line'
    
    course_id = fields.Many2one('course.detail', string="Course")
    lesson_id = fields.Many2one('course.lesson', string="Lessons")
