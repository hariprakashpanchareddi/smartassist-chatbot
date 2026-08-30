import os

os.makedirs('data/knowledge_base', exist_ok=True)

topics = {
    'billing': ['refunds', 'invoices', 'payment_methods', 'subscription_cancellation', 'upgrade_plan', 'late_fees', 'tax_exemptions', 'currency_support'],
    'account': ['reset_password', 'two_factor_auth', 'change_email', 'delete_account', 'transfer_ownership', 'multiple_users', 'role_permissions', 'profile_picture'],
    'technical': ['api_limits', 'webhook_setup', 'ip_allowlisting', 'supported_browsers', 'mobile_app_sync', 'export_data', 'system_downtime', 'integration_errors'],
    'general': ['contact_support', 'business_hours', 'service_level_agreement', 'privacy_policy', 'terms_of_service', 'data_retention', 'feature_requests', 'company_location']
}

count = 0
for cat, items in topics.items():
    for item in items:
        title = item.replace('_', ' ').title()
        content = f"# {title}\n\n**Category:** {cat.title()}\n\nThis article provides standard information regarding {title.lower()}. If you require further assistance with your {cat} issue, our support team is ready to help.\n"
        with open(f"data/knowledge_base/{cat}_{item}.md", 'w') as f:
            f.write(content)
        count += 1

print(f"Successfully generated {count} markdown articles in data/knowledge_base/")
