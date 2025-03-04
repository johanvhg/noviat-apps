# Copyright 2009-2021 Noviat
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Belgium - Multilingual Chart of Accounts (en/nl/fr)',
    'version': '11.0.1.2.5',
    'license': 'AGPL-3',
    'author': "Noviat",
    'website': 'http://www.noviat.com',
    'category': 'Localization',
    'depends': [
        'account_account_tag_code',
        'account_financial_report_date_range',
        'account_tax_code',
        'l10n_multilang',
        'l10n_account_translate_config',
        'base_vat',
        'base_iban',
        'account_invoicing',
        'account_fiscal_year',
        'account_move_line_tax_editable',
        'report_xlsx_helper',
        'web_tree_decoration_underline',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/account_chart_template_create.xml',
        'data/account_account_tag.xml',
        'data/account_tax_code_chart.xml',
        'data/account_account_template.xml',
        'data/account_chart_template_update.xml',
        'data/account_tax_template.xml',
        'data/account_fiscal_position_template.xml',
        'data/account_fiscal_position_tax_template.xml',
        'data/account_fiscal_position_account_template.xml',
        'data/account_financial_report.xml',
        'data/be_legal_financial_reportscheme.xml',
        'data/ir_sequence.xml',
        'views/account_account.xml',
        'views/account_financial_report.xml',
        'views/be_legal_financial_reportscheme.xml',
        'views/l10n_be_layouts.xml',
        'views/report_financial.xml',
        'views/report_l10nbevatdeclaration.xml',
        'views/report_l10nbevatintracom.xml',
        'views/report_l10nbevatlisting.xml',
        'views/res_partner.xml',
        'wizards/accounting_report.xml',
        'wizards/l10n_be_coa_multilang_config.xml',
        'wizards/l10n_be_update_be_reportscheme.xml',
        'wizards/l10n_be_vat_common.xml',
        'wizards/l10n_be_vat_declaration.xml',
        'wizards/l10n_be_vat_intracom.xml',
        'wizards/l10n_be_vat_listing.xml',
        'data/account_chart_template_data.yml',
    ],
    'installable': True,
}
