# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:46:56 2024

@author: Austin
"""

print("The Invoice program\n")

cust_type = input("Enter customer type (r/w):\t")
invoice_total = int(input("Enter invoice total:\t\t\t"))
                     
                      
if cust_type.lower() == "r":
    if invoice_total < 100:
        discount_percent = 0
    elif invoice_total >= 100 and invoice_total <250:
        discount_percent = 0.1
    elif invoice_total >= 250:
        discount_percent = 0.2
  
    
elif cust_type.lower() == "w":
    if invoice_total < 500:
        discount_percent = 0.4
    elif invoice_total >= 500:
        discount_percent = 0.5
        
discount_amount = invoice_total * discount_percent
new_total = invoice_total - discount_amount
print(f"\nInvoice total:\t\t\t\t{invoice_total:.1f}")
print(f"Discount percent:\t\t\t{discount_percent:.1f}")
print(f"Discount ammount:\t\t\t{discount_amount:.1f}")
print(f"New invoice total:\t\t\t{new_total:.1f}")

         
    
    
    

    
    