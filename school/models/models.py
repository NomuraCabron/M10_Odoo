from odoo import models, fields, api
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta

class Student(models.Model):
    _name = 'school.student'
    _description = 'Student'

    name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    dni = fields.Char(string='DNI/NIE', required=True, unique=True)
    birthdate = fields.Date(string='Birthdate', required=True)
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    class_id = fields.Many2one('school.school_class', string='Class')

    @api.constrains('dni')
    def _check_unique_dni(self):
        for record in self:
            if self.search_count([('dni', '=', record.dni)]) > 1:
                raise ValidationError('DNI/NIE must be unique.')

    @api.depends('birthdate')
    def _compute_age(self):
        for record in self:
            if record.birthdate:
                today = fields.Date.today()
                record.age = relativedelta(today, record.birthdate).years

class SchoolClass(models.Model):
    _name = 'school.school_class'
    _description = 'School Class'

    name = fields.Char(string='Class Name', required=True)
    level = fields.Char(string='Level')
    course = fields.Char(string='Course')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    student_count = fields.Integer(string='Student Count', compute='_compute_student_count')
    description = fields.Text(string='Description')

    @api.depends('student_ids')
    def _compute_student_count(self):
        for record in self:
            record.student_count = len(record.student_ids)

    student_ids = fields.One2many('school.student', 'class_id', string='Students')

class SchoolEvent(models.Model):
    _name = 'school.event'
    _description = 'School Event'
    _order = 'date'

    date = fields.Date(string='Date', required=True)
    event_type = fields.Selection([
        ('absence', 'Absence'),
        ('late', 'Late'),
        ('behavior', 'Behavior'),
        ('commendation', 'Commendation'),
    ], string='Event Type', required=True)
    description = fields.Text(string='Description')
    student_ids = fields.Many2many('school.student', string='Students')
    class_id = fields.Many2one('school.school_class', string='Class')
    teacher_id = fields.Many2one('hr.employee', string='Teacher')

    def name_get(self):
        result = []
        for record in self:
            name = f"{record.event_type} - {record.class_id.name}"
            result.append((record.id, name))
        return result
