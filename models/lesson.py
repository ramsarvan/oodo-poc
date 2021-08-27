from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class CourseLesson(models.Model):
    _name = 'course.lesson'
    
    name = fields.Char(required=True)
    course_id = fields.Many2one(
        'course.detail',
        string='Course',
        required=True
        )
    course_description = fields.Text(string='Course Description',
                               related='course_id.description', required=True)
    room_id = fields.Many2one(
        'course.room',
        string='Room',
        required=True
        )
    lesson_line_ids = fields.One2many('course.lesson.line', 'lesson_id', string="Lessons Line")
    
    def write(self, vals):
        """ Checks that the No. of Attendees can not exceed Room Capacity.
        """
        lesson = super(CourseLesson, self).write(vals)
        all_lesson = self.env['course.lesson'].search([('room_id', '=', self.room_id.id)])
        all_lesson_line_count = self.env['course.lesson.line'].search_count([('lesson_id', 'in', all_lesson.ids)])
        room_capacity = self.room_id.capacity
        attendees_count = all_lesson_line_count
        if(attendees_count > room_capacity):
            raise ValidationError(_('No more available seats'))
        return lesson
    
    @api.model
    def create(self, vals):
        """ Checks that the No. of Attendees can not exceed Room Capacity.
        """
        lesson = super(CourseLesson, self).create(vals)
        all_lesson = self.env['course.lesson'].search([('room_id', '=', vals['room_id'])])
        all_lesson_line_count = self.env['course.lesson.line'].search_count([('lesson_id', 'in', all_lesson.ids)])
        room_capacity = lesson.room_id.capacity
        attendees_count = all_lesson_line_count
        if(attendees_count > room_capacity):
            raise ValidationError(_('No. of Attendees can not exceed Room Capacity.'))
        return lesson
    
class CourseLessonLine(models.Model):
    _name = 'course.lesson.line'
    
    partner_id = fields.Many2one('res.partner', string="Attendee", domain="[('contact_type', '=', 'attendee')]")
    instructor_id = fields.Many2one('res.partner', string="Instructor", domain="[('contact_type', '=', 'instructor')]")
    lesson_id = fields.Many2one('course.lesson', string="Lessons", ondelete="cascade")
