# Generated by Django 3.0 on 2019-12-14 00:49

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models

import djstripe.enums
import djstripe.fields


class Migration(migrations.Migration):

    dependencies = [
        ("djstripe", "0009_delete_upcominginvoice"),
    ]

    operations = [
        migrations.CreateModel(
            name="UpcomingInvoice",
            fields=[
                (
                    "djstripe_id",
                    models.BigAutoField(
                        primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "livemode",
                    models.NullBooleanField(
                        default=None,
                        help_text="Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.",
                    ),
                ),
                (
                    "created",
                    djstripe.fields.StripeDateTimeField(
                        blank=True,
                        help_text="The datetime this object was created in stripe.",
                        null=True,
                    ),
                ),
                (
                    "metadata",
                    djstripe.fields.JSONField(
                        blank=True,
                        help_text="A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.",
                        null=True,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="A description of this object.", null=True
                    ),
                ),
                ("djstripe_created", models.DateTimeField(auto_now_add=True)),
                ("djstripe_updated", models.DateTimeField(auto_now=True)),
                (
                    "account_country",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="The country of the business associated with this invoice, most often the business creating the invoice.",
                        max_length=2,
                    ),
                ),
                (
                    "account_name",
                    models.TextField(
                        blank=True,
                        help_text="The public name of the business associated with this invoice, most often the business creating the invoice.",
                        max_length=5000,
                    ),
                ),
                (
                    "amount_due",
                    djstripe.fields.StripeDecimalCurrencyAmountField(
                        decimal_places=2,
                        help_text="Final amount due (as decimal) at this time for this invoice. If the invoice's total is smaller than the minimum charge amount, for example, or if there is account credit that can be applied to the invoice, the amount_due may be 0. If there is a positive starting_balance for the invoice (the customer owes money), the amount_due will also take that into account. The charge that gets generated for the invoice will be for the amount specified in amount_due.",
                        max_digits=11,
                    ),
                ),
                (
                    "amount_paid",
                    djstripe.fields.StripeDecimalCurrencyAmountField(
                        decimal_places=2,
                        help_text="The amount, (as decimal), that was paid.",
                        max_digits=11,
                        null=True,
                    ),
                ),
                (
                    "amount_remaining",
                    djstripe.fields.StripeDecimalCurrencyAmountField(
                        decimal_places=2,
                        help_text="The amount remaining, (as decimal), that is due.",
                        max_digits=11,
                        null=True,
                    ),
                ),
                (
                    "application_fee_amount",
                    djstripe.fields.StripeDecimalCurrencyAmountField(
                        blank=True,
                        decimal_places=2,
                        help_text="The fee (as decimal) that will be applied to the invoice and transferred to the application owner's Stripe account when the invoice is paid.",
                        max_digits=11,
                        null=True,
                    ),
                ),
                (
                    "attempt_count",
                    models.IntegerField(
                        help_text="Number of payment attempts made for this invoice, from the perspective of the payment retry schedule. Any payment attempt counts as the first attempt, and subsequently only automatic retries increment the attempt count. In other words, manual payment attempts after the first attempt do not affect the retry schedule."
                    ),
                ),
                (
                    "attempted",
                    models.BooleanField(
                        default=False,
                        help_text="Whether or not an attempt has been made to pay the invoice. An invoice is not attempted until 1 hour after the ``invoice.created`` webhook, for example, so you might not want to display that invoice as unpaid to your users.",
                    ),
                ),
                (
                    "auto_advance",
                    models.NullBooleanField(
                        help_text="Controls whether Stripe will perform automatic collection of the invoice. When false, the invoice’s state will not automatically advance without an explicit action."
                    ),
                ),
                (
                    "billing_reason",
                    djstripe.fields.StripeEnumField(
                        blank=True,
                        default="",
                        enum=djstripe.enums.InvoiceBillingReason,
                        help_text="Indicates the reason why the invoice was created. subscription_cycle indicates an invoice created by a subscription advancing into a new period. subscription_create indicates an invoice created due to creating a subscription. subscription_update indicates an invoice created due to updating a subscription. subscription is set for all old invoices to indicate either a change to a subscription or a period advancement. manual is set for all invoices unrelated to a subscription (for example: created via the invoice editor). The upcoming value is reserved for simulated invoices per the upcoming invoice endpoint. subscription_threshold indicates an invoice created due to a billing threshold being reached.",
                        max_length=22,
                    ),
                ),
                (
                    "closed",
                    models.NullBooleanField(
                        default=False,
                        help_text="Whether or not the invoice is still trying to collect payment. An invoice is closed if it's either paid or it has been marked closed. A closed invoice will no longer attempt to collect payment.",
                    ),
                ),
                (
                    "collection_method",
                    djstripe.fields.StripeEnumField(
                        enum=djstripe.enums.InvoiceCollectionMethod,
                        help_text="When charging automatically, Stripe will attempt to pay this invoice using the default source attached to the customer. When sending an invoice, Stripe will email this invoice to the customer with payment instructions.",
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "currency",
                    djstripe.fields.StripeCurrencyCodeField(
                        help_text="Three-letter ISO currency code", max_length=3
                    ),
                ),
                (
                    "customer_address",
                    djstripe.fields.JSONField(
                        blank=True,
                        help_text="The customer’s address. Until the invoice is finalized, this field will equal customer.address. Once the invoice is finalized, this field will no longer be updated.",
                        null=True,
                    ),
                ),
                (
                    "customer_email",
                    models.TextField(
                        blank=True,
                        help_text="The customer’s email. Until the invoice is finalized, this field will equal customer.email. Once the invoice is finalized, this field will no longer be updated.",
                        max_length=5000,
                    ),
                ),
                (
                    "customer_name",
                    models.TextField(
                        blank=True,
                        help_text="The customer’s name. Until the invoice is finalized, this field will equal customer.name. Once the invoice is finalized, this field will no longer be updated.",
                        max_length=5000,
                    ),
                ),
                (
                    "customer_phone",
                    models.TextField(
                        blank=True,
                        help_text="The customer’s phone number. Until the invoice is finalized, this field will equal customer.phone_. Once the invoice is finalized, this field will no longer be updated.",
                        max_length=5000,
                    ),
                ),
                (
                    "customer_shipping",
                    djstripe.fields.JSONField(
                        blank=True,
                        help_text="The customer’s shipping information. Until the invoice is finalized, this field will equal customer.shipping. Once the invoice is finalized, this field will no longer be updated.",
                        null=True,
                    ),
                ),
                (
                    "customer_tax_exempt",
                    djstripe.fields.StripeEnumField(
                        default="",
                        enum=djstripe.enums.CustomerTaxExempt,
                        help_text="The customer’s tax exempt status. Until the invoice is finalized, this field will equal customer.tax_exempt. Once the invoice is finalized, this field will no longer be updated.",
                        max_length=7,
                    ),
                ),
                (
                    "due_date",
                    djstripe.fields.StripeDateTimeField(
                        blank=True,
                        help_text="The date on which payment for this invoice is due. This value will be null for invoices where billing=charge_automatically.",
                        null=True,
                    ),
                ),
                (
                    "ending_balance",
                    djstripe.fields.StripeQuantumCurrencyAmountField(
                        help_text="Ending customer balance (in cents) after attempting to pay invoice. If the invoice has not been attempted yet, this will be null.",
                        null=True,
                    ),
                ),
                (
                    "footer",
                    models.TextField(
                        blank=True,
                        help_text="Footer displayed on the invoice.",
                        max_length=5000,
                    ),
                ),
                (
                    "forgiven",
                    models.NullBooleanField(
                        default=False,
                        help_text="Whether or not the invoice has been forgiven. Forgiving an invoice instructs us to update the subscription status as if the invoice were successfully paid. Once an invoice has been forgiven, it cannot be unforgiven or reopened.",
                    ),
                ),
                (
                    "hosted_invoice_url",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="The URL for the hosted invoice page, which allows customers to view and pay an invoice. If the invoice has not been frozen yet, this will be null.",
                        max_length=799,
                    ),
                ),
                (
                    "invoice_pdf",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="The link to download the PDF for the invoice. If the invoice has not been frozen yet, this will be null.",
                        max_length=799,
                    ),
                ),
                (
                    "next_payment_attempt",
                    djstripe.fields.StripeDateTimeField(
                        blank=True,
                        help_text="The time at which payment will next be attempted.",
                        null=True,
                    ),
                ),
                (
                    "number",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="A unique, identifying string that appears on emails sent to the customer for this invoice. This starts with the customer’s unique invoice_prefix if it is specified.",
                        max_length=64,
                    ),
                ),
                (
                    "paid",
                    models.BooleanField(
                        default=False,
                        help_text="The time at which payment will next be attempted.",
                    ),
                ),
                (
                    "period_end",
                    djstripe.fields.StripeDateTimeField(
                        help_text="End of the usage period during which invoice items were added to this invoice."
                    ),
                ),
                (
                    "period_start",
                    djstripe.fields.StripeDateTimeField(
                        help_text="Start of the usage period during which invoice items were added to this invoice."
                    ),
                ),
                (
                    "post_payment_credit_notes_amount",
                    djstripe.fields.StripeQuantumCurrencyAmountField(
                        blank=True,
                        help_text="Total amount (in cents) of all post-payment credit notes issued for this invoice.",
                        null=True,
                    ),
                ),
                (
                    "pre_payment_credit_notes_amount",
                    djstripe.fields.StripeQuantumCurrencyAmountField(
                        blank=True,
                        help_text="Total amount (in cents) of all pre-payment credit notes issued for this invoice.",
                        null=True,
                    ),
                ),
                (
                    "receipt_number",
                    models.CharField(
                        blank=True,
                        help_text="This is the transaction number that appears on email receipts sent for this invoice.",
                        max_length=64,
                        null=True,
                    ),
                ),
                (
                    "starting_balance",
                    djstripe.fields.StripeQuantumCurrencyAmountField(
                        help_text="Starting customer balance (in cents) before attempting to pay invoice. If the invoice has not been attempted yet, this will be the current customer balance."
                    ),
                ),
                (
                    "statement_descriptor",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="An arbitrary string to be displayed on your customer's credit card statement. The statement description may not include <>\"' characters, and will appear on your customer's statement in capital letters. Non-ASCII characters are automatically stripped. While most banks display this information consistently, some may display it incorrectly or not at all.",
                        max_length=22,
                    ),
                ),
                (
                    "status_transitions",
                    djstripe.fields.JSONField(blank=True, null=True),
                ),
                (
                    "subscription_proration_date",
                    djstripe.fields.StripeDateTimeField(
                        blank=True,
                        help_text="Only set for upcoming invoices that preview prorations. The time used to calculate prorations.",
                        null=True,
                    ),
                ),
                (
                    "subtotal",
                    djstripe.fields.StripeDecimalCurrencyAmountField(
                        decimal_places=2,
                        help_text="Total (as decimal) of all subscriptions, invoice items, and prorations on the invoice before any discount or tax is applied.",
                        max_digits=11,
                    ),
                ),
                (
                    "tax",
                    djstripe.fields.StripeDecimalCurrencyAmountField(
                        blank=True,
                        decimal_places=2,
                        help_text="The amount (as decimal) of tax included in the total, calculated from ``tax_percent`` and the subtotal. If no ``tax_percent`` is defined, this value will be null.",
                        max_digits=11,
                        null=True,
                    ),
                ),
                (
                    "tax_percent",
                    djstripe.fields.StripePercentField(
                        blank=True,
                        decimal_places=2,
                        help_text="This percentage of the subtotal has been added to the total amount of the invoice, including invoice line items and discounts. This field is inherited from the subscription's ``tax_percent`` field, but can be changed before the invoice is paid. This field defaults to null.",
                        max_digits=5,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(100),
                        ],
                    ),
                ),
                (
                    "threshold_reason",
                    djstripe.fields.JSONField(
                        blank=True,
                        help_text="If billing_reason is set to subscription_threshold this returns more information on which threshold rules triggered the invoice.",
                        null=True,
                    ),
                ),
                (
                    "total",
                    djstripe.fields.StripeDecimalCurrencyAmountField(
                        decimal_places=2,
                        max_digits=11,
                        verbose_name="Total (as decimal) after discount.",
                    ),
                ),
                (
                    "webhooks_delivered_at",
                    djstripe.fields.StripeDateTimeField(
                        help_text="The time at which webhooks for this invoice were successfully delivered (if the invoice had no webhooks to deliver, this will match `date`). Invoice payment is delayed until webhooks are delivered, or until all webhook delivery attempts have been exhausted.",
                        null=True,
                    ),
                ),
                (
                    "charge",
                    models.OneToOneField(
                        help_text="The latest charge generated for this invoice, if any.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="latest_upcominginvoice",
                        to="djstripe.Charge",
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        help_text="The customer associated with this invoice.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="upcominginvoices",
                        to="djstripe.Customer",
                    ),
                ),
                (
                    "default_payment_method",
                    models.ForeignKey(
                        blank=True,
                        help_text="Default payment method for the invoice. It must belong to the customer associated with the invoice. If not set, defaults to the subscription’s default payment method, if any, or to the default payment method in the customer’s invoice settings.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="djstripe.PaymentMethod",
                    ),
                ),
                (
                    "payment_intent",
                    models.OneToOneField(
                        help_text="The PaymentIntent associated with this invoice. The PaymentIntent is generated when the invoice is finalized, and can then be used to pay the invoice.Note that voiding an invoice will cancel the PaymentIntent",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="djstripe.PaymentIntent",
                    ),
                ),
                (
                    "subscription",
                    models.ForeignKey(
                        help_text="The subscription that this invoice was prepared for, if any.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="upcominginvoices",
                        to="djstripe.Subscription",
                    ),
                ),
            ],
            options={"ordering": ["-created"], "abstract": False,},
        ),
    ]