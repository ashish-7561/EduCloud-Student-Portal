from azure.cosmos import CosmosClient

# ENTER YOUR AZURE COSMOS DB CREDENTIALS HERE
COSMOS_URI = "<ENTER THE URI>"
COSMOS_KEY = "<ENTER THE KEY>"

DATABASE_NAME = "database"
CONTAINER_NAME = "container2"
PARTITION_KEY_FIELD = "/city"

print("Initializing EduCloud Backend...")

try:
    # 1. Connect to Azure Cosmos DB
    client = CosmosClient(COSMOS_URI, credential=COSMOS_KEY)
    database = client.get_database_client(DATABASE_NAME)
    container = database.get_container_client(CONTAINER_NAME)
    print("✓ Connected to Cosmos DB successfully!\n")

    # 2. Add a Student Record
    student_item = {
        "id": "105",
        "firstname": "Ashish",
        "lastname": "Student",
        "Subject": "Cloud Computing",
        "city": "Delhi"
    }
    container.upsert_item(student_item)
    print(f"✓ Student Record Added: {student_item['firstname']} {student_item['lastname']}\n")

    # 3. Query the Database to show all records
    print("--- CURRENT STUDENT DATABASE RECORDS ---")
    query = "SELECT * FROM c"
    items = container.query_items(
        query=query,
        enable_cross_partition_query=True
    )

    for item in items:
        # Safely print items 
        fname = item.get('firstname', item.get('fname', 'Unknown'))
        lname = item.get('lastname', item.get('lname', 'Unknown'))
        city = item.get('city', 'Unknown')
        print(f"ID: {item['id']} | Name: {fname} {lname} | City: {city}")
        
    print("--------------------------------------")

except Exception as e:
    print(f"An error occurred: {e}")