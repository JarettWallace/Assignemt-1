from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.
print("Available Products:")
for product in products:
    print(product)


# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences = [] 

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list

    customer_preferences.append(preference)
    response = input("Do you want to add another preference? (Y/N): ").upper()
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_tags = set(customer_preferences)


# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []
for product in products:
    converted_products.append({
        "name": product["name"],
        "tags": set(product["tags"])
        ])




# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    pass

return len(product_tags.intersection(customer_tags))


# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    pass
    
    recommendations = [] 
    for product in products:
        matches = count_matches(profuct["tags"], customer_tags)
        if matches > 0:
            reccomendations.append({
                "name": product["name"],
                "matches": matches
            }) 

    recommendations.sort(key = lambda x: (-x["matches"], x["name"]))
    return recommendations




# TODO: Step 7 - Call your function and print the results 
recommended = recommend_products(converted_products, customer_tags)

print("\nRecommmended Products:")
for item in recommended:
    print(f"- {item['name']} ({item['matches']} match(es))")





# DESIGN MEMO (write below in a comment): should be around 209 word -Jarett
# 1 Throughout my code I used several different core functions that are present within python; these functions include things like for loops and sorting. To start, loops are used mainly to help check every single product against what the customers preferences are, if this loop was not present we couldn't compare each product to each other leading to my code being very inefficient. Next up I used sorting functions through the use of lambda, the use of this function helps make sure my code is working efficiently as possible along with making sure the product with the most matches to the customers specifications will appear first. Both of these functions are used to ensure my code is as efficient as possible and meets the requirements of the code. 
# 2 If the amount of products grows over one thousand items it would be a good idea to prestore any tags as sets, it would also be important for the code to limit the top results as to not overwhelm any potential customers as showing every item that can relate to their result could show several items that they would not want to see. Limiting the results will also lead to more stream line results and letting a customer make different searches quickly. 


