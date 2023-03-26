{

    'name':"hms_odoo",
    'version':'1.0',
    'data' : [
    'views/createpatients.xml',
      'views/departments.xml',
        'views/doctor.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ]
}


# python3 odoo/odoo-bin -c odoo.conf -d odoo_db
