from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestDocument(TransactionCase):

    def test_create_document(self):
        # Create a partner
        partner = self.env['res.partner'].create({'name': 'Test Partner'})

        # Create an employee
        employee = self.env['hr.employee'].create({'name': 'Test Employee'})

        # Create a document
        document = self.env['ng_libre.document'].create({
            'title': 'Test Document',
            'description': 'This is a test document',
            'partner_id': partner.id,
            'date': '2024-06-03',
            'employer_ids': [(6, 0, [employee.id])]
        })

        # Check if the document is created successfully
        self.assertEqual(document.title, 'Test Document')
        self.assertEqual(document.description, 'This is a test document')
        self.assertEqual(document.partner_id, partner)
        self.assertEqual(document.date, '2024-06-03')
        self.assertIn(employee, document.employer_ids)

    def test_document_user_default(self):
        # Create a document without specifying the user
        document = self.env['ng_libre.document'].create({
            'title': 'Test Document',
            'description': 'This is a test document',
        })

        # Check if the user is automatically set to the current user
        self.assertEqual(document.user_id, self.env.user)

    def test_document_title_required(self):
        # Attempt to create a document without specifying the title
        with self.assertRaises(ValidationError):
            self.env['ng_libre.document'].create({
                'description': 'This is a test document',
            })