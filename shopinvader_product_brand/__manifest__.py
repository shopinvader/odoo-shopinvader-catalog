# Copyright 2021 Akretion (https://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


{
    "name": "Shopinvader Product Brand",
    "summary": "Shopinvader product Brand",
    "version": "18.0.1.0.0",
    "category": "Shopinvader",
    "website": "https://github.com/shopinvader/odoo-shopinvader-catalog",
    "author": " Akretion",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        # OCA
        "base_url",
        "product_brand",
        # Shopinvader
        "shopinvader_product",
        "shopinvader_product_seo",
    ],
    "data": [
        "views/product_brand_view.xml",
    ],
    "external_dependencies": {"python": ["extendable_pydantic>=1.2.0"]},
    "development_status": "Alpha",
}
