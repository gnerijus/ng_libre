# Copyright (C) 2024 ngsolution!, UAB https://odoo.ngsolution.eu

from odoo import models, fields, api


class DocumentWizard(models.TransientModel):
    _name = 'ng_libre.document_wizard'
    _description = 'Document Wizard'

    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")
    employer_id = fields.Many2one('hr.employee')

    def print_report(self):
        data = {
            'model': 'ng_libre.document_wizard',
            'form': self.read()[0]
        }
        domain = []
        Document = self.env['ng_libre.document']
        print(data.get('form'))
        if data.get('form') and data.get('form').get('employer_id'):
            employer_id = data['form']['employer_id'][0]
            print(employer_id)
            ids = []
            for doc in Document.search([]):
                if employer_id in doc.employer_ids.ids:
                    ids.append(doc.id)
            docs = Document.search([('id', 'in', ids)])
            print(docs)
            domain.append(('id', 'in', docs.ids))
        if data.get('form') and data.get('form').get('date_from'):
            date_from = data['form']['date_from']
            print(date_from)
            domain.append(('date', '>=', date_from))
        if data.get('form') and data.get('form').get('date_to'):
            date_to = data['form']['date_to']
            print(date_to)
            domain.append(('date', '<=', date_to))

        data['docs'] = Document.search(domain).ids

        return self.env.ref('ng_libre.report_document').report_action(self, data=data)

        #return self.env.ref('ng_libre.report_document').with_context(
        #    landscape=self.orientation == 'landscape').report_action(self, data=data)
