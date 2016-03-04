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
customer_api = swagger_client.CustomerresourceApi()
customer_group_api = swagger_client.CustomergroupresourceApi()
price_list_api = swagger_client.PricelistresourceApi()

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
