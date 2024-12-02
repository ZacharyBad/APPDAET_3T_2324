first_name_lower = "Zach"
first_name_upper = "ZACH"

print(first_name_lower.capitalize())
print(first_name_upper.capitalize())

country_1 = "Slovenia"
country_2 = "Lativa"

print(country_1.lower())
print(country_2.lower())

print(country_1.upper())
print(country_2.upper())

sm_mall_prefix = "SM"
mall_1 = "SM - Mall of Asia"
mall_2 = "SM Megamall"
mall_3 = "Robinson's Place Manila"

print(mall_1.startswith(sm_mall_prefix))
print(mall_2.startswith("SM"))
print(mall_3.startswith(sm_mall_prefix))

country_a = "Yugoslavia"
country_b = "Romania"
country_c= "Bavaria"
country_d = "Hungary"

print(country_a.endswith("ia"))
print(country_b.endswith("ia"))
print(country_c.endswith("ia"))
print(country_d.endswith("ia"))

print("\n\n\n\nNikola Jokic".strip())
print("Luka Doncic\t\t\t\t".strip())
print("  Peja Stojakovic ".strip())


campaign_paragraph = """
 Welcome to Resorts world! etc.
"""

print(campaign_paragraph)

print(campaign_paragraph.replace("Resorts World", "Newport"))