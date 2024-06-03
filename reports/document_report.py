from odoo import models, fields, api


class DocumentReportPrint(models.AbstractModel):
    _name = 'report.ng_libre.document_report'
    _description = "report document"

    @api.model
    def _get_report_values(self, docids, data=None):

        Document = self.env['ng_libre.document']

        return {'docs': docids and Document.browse(docids) or Document.browse(data.get('docs'))}
