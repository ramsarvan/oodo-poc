# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "Courses",
    'summary': "Allows to create Course detail",
    'description': """Allows to link forum on a course""",
    'version': '1.0',
    'depends': ['base', 'contacts'],

    'data': [
        'security/ir.model.access.csv',
        'views/room_view.xml',
        'views/course_view.xml',
        'views/lesson_view.xml',
        'views/attendee_view.xml',
        'views/instructor_view.xml',
        'views/contact_view.xml',
        'report/course_report.xml',
        'report/course_report_templates.xml',
    ],
    
    'installable': True,
    'application': True
}
