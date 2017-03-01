# -*- coding: utf-8 -*-
{
    'name': "moduloinstalador",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Your Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 
                'crm', 
'mail', 
'account_voucher', 
'point_of_sale', 
'project', 
'note', 
'account_accountant', 
'sale', 
'stock', 
'stock_account', 
'im_chat', 
'purchase', 
'hr', 
'account_asset', 
'account', 
'account_balance_reporting', 
'account_balance_reporting_xls', 
'account_banking_mandate', 
'account_banking_pain_base', 
'account_banking_payment_export', 
'account_banking_payment_transfer', 
'account_banking_sepa_direct_debit', 
'account_bank_statement_import', 
'account_cancel', 
'account_chart_update', 
'account_direct_debit', 
'account_due_list', 
'account_due_list_payment_mode', 
'account_export_csv', 
'account_invoice_constraint_chronology', 
'account_invoice_currency', 
'account_journal_always_check_date', 
'account_move_line_report_xls', 
'account_payment', 
'account_payment_partner', 
'account_refund_original', 
'account_renumber', 
'analytic', 
'auth_crypt', 
'auth_signup', 
'base', 
'base_action_rule', 
'base_iban', 
'base_import', 
'base_import_module', 
'base_location', 
'base_location_geonames_import', 
'base_partner_sequence', 
'base_setup', 
'base_vat', 
'board', 
'bus', 
'calendar', 
'contacts', 
'decimal_precision', 
'document', 
'document_url', 
'edi', 
'email_template', 
'fetchmail', 
'im_odoo_support', 
'knowledge', 
'l10n_es', 
'l10n_es_account_asset', 
'l10n_es_account_balance_report', 
'l10n_es_account_bank_statement_import_n43', 
'l10n_es_account_financial_report', 
'l10n_es_account_invoice_sequence', 
'l10n_es_aeat', 
'l10n_es_aeat_mod111', 
'l10n_es_aeat_mod115', 
'l10n_es_aeat_mod303', 
'l10n_es_aeat_mod340', 
'l10n_es_aeat_mod347', 
'l10n_es_aeat_mod349', 
'l10n_es_fiscal_year_closing', 
'l10n_es_partner', 
'l10n_es_toponyms', 
'mass_editing', 
'moduloinstalador', 
'payment', 
'payment_transfer', 
'portal', 
'portal_project', 
'portal_sale', 
'portal_stock', 
'procurement', 
'product', 
'report', 
'report_xls', 
'resource', 
'sale_crm', 
'sales_team', 
'sale_stock', 
'share', 
'web', 
'web_calendar', 
'web_diagram', 
'web_export_view', 
'web_gantt', 
'web_graph', 
'web_kanban', 
'web_kanban_gauge', 
'web_kanban_sparkline', 
'web_tests', 
'web_view_editor', 
],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
