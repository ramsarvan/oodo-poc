from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    contact_type = fields.Selection([
        ('attendee', 'Attendee'), ('instructor', 'Instructor')],
        string='Contact type',
        help='Condition to identify a contact is an Attendee or Instructor')
    course_id = fields.Many2one(
        'course.detail',
        string='Course'
        )
    instructor_id = fields.Many2one(
        comodel_name='res.partner',
        string='Instructor',
        domain="[('contact_type', '=', 'instructor')]"
        )
    partner_course_ids = fields.One2many('partner.course.detail', 'partner_id', string="Course Details")
    lesson_count = fields.Integer("# of Lessons", compute='_compute_lesson_count', compute_sudo=True)
    lesson_ids = fields.Many2many('course.lesson', string='Lessons')

    @api.depends('lesson_ids')
    def _compute_lesson_count(self):
        """ Compute the Lesson count of the person.
        """
        lesson_line_data = 0
        if self.contact_type == 'attendee':
            lesson_line_data = self.env['course.lesson.line'].search_count([('partner_id', 'in', self.ids)])
        elif self.contact_type == 'instructor':
            lesson_line_data = self.env['course.lesson.line'].search_count([('instructor_id', 'in', self.ids)])
        for contact in self:
            contact.lesson_count = lesson_line_data
        
    def action_get_lesson_view(self):
        """ This function returns an action that display No. of Lessons
        of given Contact
        """
        self.ensure_one()
        res = self.env['ir.actions.act_window']._for_xml_id('courses.lesson_action')
        if self.contact_type == 'attendee':
            res['domain'] = [('lesson_line_ids.partner_id', 'in', self.ids)]
        elif self.contact_type == 'instructor':
            res['domain'] = [('lesson_line_ids.instructor_id', 'in', self.ids)]
        return res


class PartnerCourseDetail(models.Model):
    _name = 'partner.course.detail'
    
    partner_id = fields.Many2one('res.partner', string="Attendee")
    lesson_id = fields.Many2one('course.lesson', string="Lessons")  
    course_id = fields.Many2one('course.detail', string="Course")    
