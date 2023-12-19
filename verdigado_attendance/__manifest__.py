# Copyright 2022 verdigado eG
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Verdigado HR Attendance",
    "version": "15.0.1.0.1",
    "category": "Human Resources",
    "website": "https://github.com/verdigado/odoo-customize",
    "author": "verdigado eG",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "auditlog",
        "base_ical",
        "board",
        "hr_attendance",
        "hr_attendance_autoclose",
        "hr_attendance_break",
        "hr_attendance_break_autoclose",
        "hr_attendance_missing_days",
        "hr_holidays_attendance",
        "l10n_de_holidays",
        "hr_holidays_public_overtime",
        "hr_holidays_overlap",
        "module_auto_update",
    ],
    "data": [
        "data/base_ical.xml",
        "data/hr_leave_type.xml",
        "data/ir_cron.xml",
        "data/res_company.xml",
        "data/res.lang.csv",
        "security/verdigado_attendance.xml",
        "security/ir.model.access.csv",
        "views/base_ical.xml",
        "views/hr_attendance_view.xml",
        "views/hr_attendance_report.xml",
        "views/hr_leave_type.xml",
        "views/hr_leave.xml",
        "views/hr_menu_human_resources_configuration.xml",
        "views/menu.xml",
    ],
    "demo": [
        "demo/res_users.xml",
        "demo/hr_employee.xml",
        "demo/hr_leave_allocation.xml",
    ],
    "assets": {
        "web._assets_primary_variables": [
            "verdigado_attendance/static/src/scss/primary_variables.scss",
        ],
        "web.assets_frontend": [
            "verdigado_attendance/static/src/scss/frontend.scss",
        ],
        "web.assets_backend": [
            "verdigado_attendance/static/src/scss/backend.scss",
            "verdigado_attendance/static/src/js/systray.esm.js",
            "verdigado_attendance/static/src/js/time_off_calendar.js",
        ],
        "web.assets_qweb": [
            "verdigado_attendance/static/src/xml/hr_holidays.xml",
            "verdigado_attendance/static/src/xml/systray.xml",
            "verdigado_attendance/static/src/xml/time_off_calendar.xml",
        ],
    },
}
