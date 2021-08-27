from odoo import fields, models


class CourseRoom(models.Model):
    _name = 'course.room'
    
    name = fields.Char(required=True)
    capacity = fields.Integer(string='Capacity', required=True)
    
    
