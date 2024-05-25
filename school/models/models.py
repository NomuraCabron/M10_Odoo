# models/models.py
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date
from dateutil.relativedelta import relativedelta

class Student(models.Model):
    _name = 'school.student'
    _description = 'Student'

    name = fields.Char(string='Nombre', required=True)
    surname = fields.Char(string='Apellido', required=True)
    dni = fields.Char(string='DNI/NIE', required=True)
    birthdate = fields.Date(string='Fecha de Nacimiento')
    age = fields.Integer(string='Edad', compute='_compute_age', store=True)

    _sql_constraints = [
        ('dni_unique', 'unique(dni)', 'DNI/NIE debe ser único.'),
    ]

    @api.depends('birthdate')
    def _compute_age(self):
        for record in self:
            if record.birthdate:
                record.age = relativedelta(date.today(), record.birthdate).years
            else:
                record.age = 0

class SchoolClass(models.Model):
    _name = 'school.class'
    _description = 'School Class'

    name = fields.Char(string='Nombre de la Clase', required=True)
    level = fields.Char(string='Nivel')
    course = fields.Char(string='Curso Escolar')
    start_date = fields.Date(string='Fecha de Inicio')
    end_date = fields.Date(string='Fecha de Fin')
    student_count = fields.Integer(string='Cantidad de Estudiantes')
    description = fields.Text(string='Descripción')

class Event(models.Model):
    _name = 'school.event'
    _description = 'Event'
    _order = 'date'

    event_type = fields.Selection([
        ('absence', 'Absencia'),
        ('delay', 'Retraso'),
        ('behavior', 'Comportamiento'),
        ('commendation', 'Felicitación'),
    ], string='Tipo de Incidente', required=True)
    date = fields.Date(string='Fecha', required=True)
    description = fields.Text(string='Descripción')
    student_ids = fields.Many2many('school.student', string='Estudiantes')

    def name_get(self):
        result = []
        for record in self:
            name = f"{record.event_type} - {record.date}"
            result.append((record.id, name))
        return result
