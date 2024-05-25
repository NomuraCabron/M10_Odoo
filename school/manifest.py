# __manifest__.py
{
    'name': 'School Management',
    'version': '1.0',
    'summary': 'Gestió de l\'escola',
    'description': 'Mòdul per gestionar estudiants, classes i incidents en una escola.',
    'category': 'Education',
    'author': 'El teu nom',
    'website': 'https://www.teusite.com',
    'depends': ['base', 'hr'],
    'data': [
        'views/school_class_views.xml',
        'views/student_views.xml',
        'views/event_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
