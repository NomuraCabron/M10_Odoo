{
    'name': 'School Management',
    'version': '1.0',
    'summary': 'Manage students, classes, and incidents in a school.',
    'description': 'Module to manage students, classes, and incidents in a school.',
    'author': 'Your Name',
    'depends': ['base', 'hr'],
    'data': [
        'views/school_class_views.xml',
        'views/student_views.xml',
        'views/school_event_views.xml',
    ],
    'installable': True,
    'application': True,
}