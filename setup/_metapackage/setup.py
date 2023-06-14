import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-shopinvader-odoo-shopinvader",
    description="Meta package for shopinvader-odoo-shopinvader Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-base_url',
        'odoo14-addon-shopinvader',
        'odoo14-addon-shopinvader_algolia',
        'odoo14-addon-shopinvader_assortment',
        'odoo14-addon-shopinvader_auth_api_key',
        'odoo14-addon-shopinvader_auth_jwt',
        'odoo14-addon-shopinvader_backend_image_proxy',
        'odoo14-addon-shopinvader_cart_expiry',
        'odoo14-addon-shopinvader_category_image_for_product',
        'odoo14-addon-shopinvader_contact_address_default',
        'odoo14-addon-shopinvader_customer_activity',
        'odoo14-addon-shopinvader_customer_invoicing_mode',
        'odoo14-addon-shopinvader_customer_multi_user',
        'odoo14-addon-shopinvader_customer_multi_user_company_group',
        'odoo14-addon-shopinvader_customer_multi_user_validate',
        'odoo14-addon-shopinvader_customer_multi_user_wishlist',
        'odoo14-addon-shopinvader_customer_price',
        'odoo14-addon-shopinvader_customer_price_wishlist',
        'odoo14-addon-shopinvader_customer_validate',
        'odoo14-addon-shopinvader_delivery_carrier',
        'odoo14-addon-shopinvader_delivery_carrier_category_keep_carrier',
        'odoo14-addon-shopinvader_delivery_instruction',
        'odoo14-addon-shopinvader_delivery_state',
        'odoo14-addon-shopinvader_easy_binding',
        'odoo14-addon-shopinvader_elasticsearch',
        'odoo14-addon-shopinvader_guest_mode',
        'odoo14-addon-shopinvader_image',
        'odoo14-addon-shopinvader_import_image',
        'odoo14-addon-shopinvader_invoice',
        'odoo14-addon-shopinvader_lead',
        'odoo14-addon-shopinvader_locomotive',
        'odoo14-addon-shopinvader_locomotive_algolia',
        'odoo14-addon-shopinvader_locomotive_guest_mode',
        'odoo14-addon-shopinvader_locomotive_reset_password',
        'odoo14-addon-shopinvader_locomotive_sale_profile',
        'odoo14-addon-shopinvader_locomotive_wishlist',
        'odoo14-addon-shopinvader_membership',
        'odoo14-addon-shopinvader_multi_cart',
        'odoo14-addon-shopinvader_multi_category',
        'odoo14-addon-shopinvader_notification_default',
        'odoo14-addon-shopinvader_partner_firstname',
        'odoo14-addon-shopinvader_partner_vat',
        'odoo14-addon-shopinvader_pending_cart_reminder',
        'odoo14-addon-shopinvader_portal_mode',
        'odoo14-addon-shopinvader_pos',
        'odoo14-addon-shopinvader_price_per_qty',
        'odoo14-addon-shopinvader_product_attribute_set',
        'odoo14-addon-shopinvader_product_brand',
        'odoo14-addon-shopinvader_product_brand_image',
        'odoo14-addon-shopinvader_product_brand_tag',
        'odoo14-addon-shopinvader_product_manufactured_for',
        'odoo14-addon-shopinvader_product_media',
        'odoo14-addon-shopinvader_product_new',
        'odoo14-addon-shopinvader_product_order',
        'odoo14-addon-shopinvader_product_price_tax',
        'odoo14-addon-shopinvader_product_stock',
        'odoo14-addon-shopinvader_product_stock_assortment',
        'odoo14-addon-shopinvader_product_stock_forecast',
        'odoo14-addon-shopinvader_product_stock_forecast_expiry',
        'odoo14-addon-shopinvader_product_stock_state',
        'odoo14-addon-shopinvader_product_template_multi_link',
        'odoo14-addon-shopinvader_product_template_multi_link_date_span',
        'odoo14-addon-shopinvader_product_template_tags',
        'odoo14-addon-shopinvader_product_variant_multi_link',
        'odoo14-addon-shopinvader_product_variant_selector',
        'odoo14-addon-shopinvader_product_video_link',
        'odoo14-addon-shopinvader_quotation',
        'odoo14-addon-shopinvader_sale_amount_by_group',
        'odoo14-addon-shopinvader_sale_automatic_workflow',
        'odoo14-addon-shopinvader_sale_coupon',
        'odoo14-addon-shopinvader_sale_packaging',
        'odoo14-addon-shopinvader_sale_packaging_wishlist',
        'odoo14-addon-shopinvader_sale_profile',
        'odoo14-addon-shopinvader_search_engine',
        'odoo14-addon-shopinvader_wishlist',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
