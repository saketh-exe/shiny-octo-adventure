from hashTagEngine import get_top_k_tags

print("Top 5 Hashtags:")
for tag in get_top_k_tags(5):
print(f"#{tag[0]}: {tag[1]}") #type: ignore