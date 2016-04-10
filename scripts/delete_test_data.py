import os
import time
import unittest
import swagger_client
import random

api = swagger_client.ApiClient("http://localhost:3000/v2/api-docs")
mill_api = swagger_client.MillresourceApi()
quality_api = swagger_client.QualityresourceApi()
price_api = swagger_client.PriceresourceApi()
sgs_api = swagger_client.SimplegsmshaderesourceApi()
dgs_api = swagger_client.DerivedgsmshaderesourceApi()
customer_api = swagger_client.CustomerresourceApi()
customer_group_api = swagger_client.CustomergroupresourceApi()
price_list_api = swagger_client.PricelistresourceApi()
taxtype_api = swagger_client.TaxtyperesourceApi()
tax_api = swagger_client.TaxresourceApi()
formula_api = swagger_client.FormularesourceApi()
formulae_api = swagger_client.FormulaeresourceApi()

while True:
    prices = price_api.get_all_prices_using_get()
    if not prices:
        break
    for price in prices:
       print "Deleting Price: %s" % price.id
       price_api.delete_price_using_delete(price.id)

while True:
    qualities = quality_api.get_all_qualitys_using_get()
    if not qualities:
        break
    for quality in qualities:
        print "Deleting Quality: %s" % quality.label
        quality_api.delete_quality_using_delete(quality.id)

while True:
    dgss = dgs_api.get_all_derived_gsm_shades_using_get()
    if not dgss:
        break
    for dgs in dgss:
        print "Deleting %s(%s-%s)" % (dgs.shade, dgs.min_gsm, dgs.max_gsm)
        dgs_api.delete_derived_gsm_shade_using_delete(dgs.id)

while True:
    sgss = sgs_api.get_all_simple_gsm_shades_using_get()
    if not sgss:
        break
    for sgs in sgss:
        print "Deleting %s(%s-%s)" % (sgs.shade, sgs.min_gsm, sgs.max_gsm)
        sgs_api.delete_simple_gsm_shade_using_delete(sgs.id)

while True:
    groups = customer_group_api.get_all_customer_groups_using_get()
    if not groups:
        break
    for group in groups:
        print "Deleting Customer Group: %s" % group.name
        customer_group_api.delete_customer_group_using_delete(group.id)
        
while True:
    taxes = tax_api.get_all_taxs_using_get()
    if not taxes:
        break
    for tax in taxes:
        print "Deleting Tax: %s" % tax.id
        tax_api.delete_tax_using_delete(tax.id)

while True:
    plists = price_list_api.get_all_price_lists_using_get()
    if not plists:
        break
    for plist in plists:
        print "Deleting Pricelist %s to %s" % (plist.wef_date_from, plist.wef_date_to)
        price_list_api.delete_price_list_using_delete(plist.id)

while True:
    mills = mill_api.get_all_mills_using_get()
    if not mills:
        break
    for mill in mills:
        print "Deleting Mill: %s" % mill.name
        mill_api.delete_mill_using_delete(mill.id)

while True:
    customers = customer_api.get_all_customers_using_get()
    if not customers:
        break
    for customer in customers:
        print "Deleting Customer: %s" % customer.name
        customer_api.delete_customer_using_delete(customer.id)

        
while True:
    taxtypes = taxtype_api.get_all_tax_types_using_get()
    if not taxtypes:
        break
    for taxtype in taxtypes:
        print "Deleting Tax Type: %s" % taxtype.label
        taxtype_api.delete_tax_type_using_delete(taxtype.id)

while True:
    formulas = formula_api.get_all_formulas_using_get()
    if not formulas:
        break
    for formula in formulas:
        print "Deleting Formula: %s" % formula.id
        formula_api.delete_formula_using_delete(formula.id)

while True:
    formulaes = formulae_api.get_all_formulaes_using_get()
    if not formulaes:
        break
    for formulae in formulaes:
        print "Deleting Formulae: %s" % formulae.id
        formulae_api.delete_formulae_using_delete(formulae.id)

