# Copyright 2023 Hunki Enterprises BV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0)


from odoo import fields, models


class HrAttendanceReport(models.Model):
    _inherit = "hr.attendance.report"

    expected_hours = fields.Float()

    def _select(self):
        """Add expected hours"""
        return super()._select() + ", coalesce(ot.expected_hours, 0) expected_hours"

    def _join(self):
        """Add overtime adjustments"""
        return super()._join() + " UNION %s %s %s" % (
            self._select()
            .replace("hra.worked_hours", "0")
            .replace("break_hours", "0")
            .replace("ot.duration", "0")
            .replace("coalesce(ot.expected_hours, 0)", "0"),
            self._from(),
            super()._join().replace("ot.adjustment = FALSE", "ot.adjustment = TRUE"),
        )
