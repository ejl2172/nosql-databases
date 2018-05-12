# Put the use case you chose here. Then justify your database choice:

# I am building a photo app using neo4j. Photo apps such as instagram are known as social networking websites, where people  each
# have their own profiles and are connected. Because it is easy to envision a social network as a graph (nodes represent
# people and edges represent  how they interact), neo4j, a graph database, made the most sense for the application.


# Explain what will happen if coffee is spilled on one of the servers in your cluster, causing it to go down.

# Neo4J is a master-slave cluster in which the slaves receive real-time updates from the master. Should the slave go down the
# master and/or any other slaves will remain up. There will be nodes to handle connections, and it will remain possible for the master to
# synchronize with the other slaves. If the slave that failed is brought back online, it will re-synchronize.
# If the master goes down, a slave will not automatically become a master; the slaves will continue to operate according to the last settings 
# they received from the master. When the master is brought back online, slaves will re-synchronize.


# What data is it not ok to lose in your app? What can you do in your commands to mitigate the risk of lost data?

# It is not okay for my app to lose the nodes that represent users or the photo nodes. It is not great but is not the worst should the follow 
# relationships be lost. It is okay if the comments on the photos are lost. To mitigate the risk of lost data, I could make copies of the nodes where
# it is crucial the data is not lost.

from py2neo import authenticate, Graph
authenticate("localhost:7474", "neo4j", "test")
import sys
from py2neo import Node, Relationship, Graph, NodeSelector, authenticate, GraphDatabase
#UPDATED WORK STARTS HERE
new_graph = Graph("http://localhost:7474/db/data/")
user1 = Node("Person", firstname="George", lastname="Bush",mode="Public")
user2 = Node("Person", firstname="Donald", lastname="Trump",mode="Public")
user3 = Node("Person", firstname="Jeb", lastname="Bush", mode="Public")
user4 = Node("Person", firstname="Al", lastname="Gore", mode="Public")
new_graph.create(user1 | user2 | user3 | user4)
follow1 = Relationship(user1, "FOLLOWED", user3)
follow2 = Relationship(user3, "FOLLOWED", user1)
follow3 = Relationship(user4, "FOLLOWED", user3)
follow4 = Relationship(user2, "FOLLOWED", user1)
new_graph.create(follow1 | follow2 | follow3 | follow4)
u13 = Relationship(user1, "SIBLING_OF", user3)
u31 = Relationship(user3, "SIBLING_OF", user1)
new_graph.create(u13|u31)
photoA = Node("Photo", caption = "CANNOT wait to see my brother in the Oval Office!")
postA = Relationship(user3, "POSTED", photoA)
tag1 = Relationship(user1, "TAGGED_IN", photoA)
like1 = Relationship(user1, "LIKED", photoA)
dislike1 = Relationship(user4, "DISLIKED", photoA)
photoB = Node("Photo", caption = "Bro...it is your turn now!")
postB = Relationship(user1, "POSTED", photoB)
tag2 = Relationship(user3, "TAGGED_IN", photoB)
like2 = Relationship(user3, "LIKED", photoB)
dislike2 = Relationship(user2, "DISLIKED", photoB)
comment = Relationship(user2, "COMMENTED", photoB, comment = "Um not on my watch...")
new_graph.create(tag1|tag2|like1|like2|dislike1|dislike2|comment)
photoC = Node("Photo", caption = "Great day at the Trump Tower!")
postC = Relationship(user2, "POSTED", photoC)
photoD = Node("Photo", caption = "Excited to travel and meet with President Trudeau!")
postD = Relationship(user2, "POSTED", photoD)
photoE = Node("Photo", caption = "Great day for a Texas Rangers game!")
postE = Relationship(user1, "POSTED", photoE)
photoF = Node("Photo", caption = "I hope my comrade over here wins his impeachment proceedings!")
postF = Relationship(user4, "POSTED", photoF)
photoG = Node("Photo", caption = "Florida weather = Best weather" )
postG = Relationship(user3, "POSTED", photoG)
photoH = Node("Photo", caption = "Go Miami Marlins!")
postH = Relationship(user3, "POSTED", photoH)
photoI = Node("Photo", caption = "TBT to when I was on WWE Smackdown!")
postI = Relationship(user2, "POSTED", photoI)
photoJ = Node("Photo", caption = "I miss the days of The Apprentice!")
postJ = Relationship(user2, "POSTED", photoJ)
photoK = Node("Photo", caption = "We need to be better about conservation!")
postK = Relationship(user4, "POSTED", photoK)
photoL = Node("Photo", caption = "GLOBAL WARMING AHHHH")
postL = Relationship(user4, "POSTED", photoL)
photoM = Node("Photo", caption = "It's true...I was in Skull and Bones at Yale..." )
postM = Relationship(user1, "POSTED", photoM)
photoN = Node("Photo", caption = "This app is fun...but I am gonna get back on Twitter!")
postN = Relationship(user2, "POSTED", photoN)
photoP = Node("Photo", caption = "In this tough time we must come together as one" )
postP = Relationship(user1, "POSTED", photoP)
new_graph.create(photoA|photoB|photoC|photoD|photoE|photoF|photoG|photoH|photoI|photoJ|photoK|photoL|photoM|photoN|photoP)
new_graph.create(postA|postB|postC|postD|postE|postF|postG|postH|postI|postJ|postK|postL|postM|postN|postP)
queryA = """
MATCH (person:Person)
RETURN person.firstname + " " + person.lastname AS User
"""
dataA = new_graph.run(queryA)
print("Users: ")
for dA in dataA:
	print(dA)
queryB = """
MATCH (p:Person)-[:POSTED]->(h:Photo)<-[:LIKED]-(t:Person)
RETURN t.firstname + " liked " + p.firstname + "'s photo with caption " + h.caption AS Likes 
"""
dataB = new_graph.run(queryB)
print("Likes: ")
for dB in dataB:
	print(dB)
queryC = """
MATCH (p:Person)-[:POSTED]->(h:Photo)<-[:DISLIKED]-(t:Person)
RETURN t.firstname + " disliked " + p.firstname + "'s photo with caption " + h.caption AS Dislikes 
"""
dataC = new_graph.run(queryC)
print("Likes: ")
for dC in dataC:
        print(dC)
queryD = """
MATCH (p:Person)-[:POSTED]->(h:Photo)
RETURN p.firstname + " posted photo with caption: " + h.caption AS Photos
"""
dataD = new_graph.run(queryD)
print("Photos: ")
for dD in dataD:
	print(dD)
new_graph.delete_all()
#UPDATED WORK ENDS HERE
# Action 1: Barack Obama, Bill Clinton, and Nancy Pelosi create accounts on the app.
a = Node("Person", firstname="Barack", lastname="Obama",mode="Public")
b = Node("Person", firstname="Bill", lastname="Clinton",mode="Public")
c = Node("Person", firstname="Nancy", lastname="Pelosi",mode="Public")
new_graph.create(a | b | c)
query1 = """
MATCH (person:Person)
RETURN person.firstname + " " +  person.lastname AS User
"""
data1=new_graph.run(query1)
print("Action 1: Barack Obama, Bill Clinton, and Nancy Pelosi create accounts on the app.")
print("Users:")
for d1 in data1:
	print(d1)
#Action 2: Nancy Pelosi follows Bill Clinton and Barack Obama.
cb = Relationship(c, "FOLLOWED", b)
ca = Relationship(c, "FOLLOWED", a)
new_graph.create(cb|ca)
query2 = """
MATCH (p:Person)-[:FOLLOWED]->(h:Person)
RETURN p.firstname + " " + "FOLLOWED" + " " + h.firstname AS Activity
"""
data2 = new_graph.run(query2)
print("Action 2: Nancy Pelosi follows Bill Clinton and Barack Obama.")
print("Recent Activity: ")
for d2 in data2:
    print(d2)
#Action 3: Bill Clinton and Barack Obama post two photos each.
bc1 = Node("Photo", caption = "Love my job!")
postbc1 = Relationship(b, "POSTED", bc1)
bc2 = Node("Photo", caption = "Congrats George Bush!")
postbc2 = Relationship(b, "POSTED", bc2)
bo1 = Node("Photo", caption = "Love my daughters!")
postbo1 = Relationship(a, "POSTED", bo1)
bo2 = Node("Photo", caption = "Chicago is the best!")
postbo2 = Relationship(a, "POSTED", bo2)
new_graph.create(bc1|bc2|bo1|bo2|postbc1|postbc2|postbo1|postbo2)
query3 = """
MATCH (p:Person)-[:POSTED]->(h:Photo)
RETURN p.firstname + " " + "POSTED a photo; Caption: " + " " + h.caption AS Activity
"""
data3 = new_graph.run(query3)
print("Action 3: Bill Clinton and Barack Obama post two photos each.")
print("Recent Activity: ")
for d3 in data3:
    print(d3)
# Action 4: Nancy Pelosi pulls up all the photos of Barack Obama and proceeds to comment on each.
print("Action 4: Nancy Pelosi pulls up all the photos of Barack Obama and proceeds to comment on each.")
print("Photos: ")
query4a = """
MATCH (p:Person)-[:POSTED]->(h:Photo)
WHERE p.firstname = {name}
RETURN p.firstname + "'s " + "Photo; Caption: " + h.caption AS Activity 
"""
data4a = new_graph.run(query4a, name = "Barack")
for d4a in data4a:
    print(d4a)
comment1 = Relationship(c, "COMMENTED", bo1, comment = "POTUS at his best job!")
comment2 = Relationship(c, "COMMENTED", bo2, comment = "No! D.C!")
new_graph.create(comment1|comment2)
query4b = """
MATCH (p:Person)-[m:COMMENTED]->(h:Photo)<-[:POSTED]-(t:Person)
WHERE p.firstname= {name} AND t.firstname = {name2}
RETURN p.firstname + " COMMENTED " + m.comment + " on photo of " + t.firstname AS Activity
"""
data4b = new_graph.run(query4b, name = "Nancy", name2 = "Barack")
print("Recent Activity: ")
for d4b in data4b:
    print(d4b) 
# Action 5: Nancy Pelosi pulls up all the photos of Bill Clinton and proceeds to comment on each.
print("Action 5: Nancy Pelosi pulls up all the photos of Bill Clinton and proceeds to comment on each.")
print("Photos: ")
query5a = """
MATCH (p:Person)-[:POSTED]->(h:Photo)
WHERE p.firstname = {name}
RETURN p.firstname + "'s " + "Photo; Caption: " + h.caption AS Activity 
"""
data5a = new_graph.run(query5a, name = "Bill")
for d5a in data5a:
    print(d5a)
comment3 = Relationship(c, "COMMENTED", bc1, comment = "Cannot wait to be Speaker!")
comment4 = Relationship(c, "COMMENTED", bc2, comment = "Uh oh...")
new_graph.create(comment3|comment4)
query5b = """
MATCH (p:Person)-[m:COMMENTED]->(h:Photo)<-[:POSTED]-(t:Person)
WHERE p.firstname= {name} AND t.firstname = {name2}
RETURN p.firstname + " COMMENTED " + m.comment + " on photo of " + t.firstname AS Activity
"""
data5b = new_graph.run(query5b, name = "Nancy", name2 = "Bill")
print("Recent Activity: ")
for d5b in data5b:
    print(d5b) 
# Action 6: The next day, Nancy Pelosi gets bored and wants to see all of the photos of all the people she follows (in no particular order).
print("Action 6: The next day, Nancy Pelosi gets bored and wants to see all of the photos of all the people she follows (in no particular order)")
print("Photos:")
query6="""
MATCH (p:Person)-[:FOLLOWED]->(h:Person)-[:POSTED]->(t:Photo)
WHERE p.firstname={name}
RETURN t.caption AS Caption
"""
data6 = new_graph.run(query6, name="Nancy")
print("All your followers' photos: ")
for d6 in data6:
	print(d6)
# Action 7: Nancy Pelosi gets bored of the app and decides to delete her account and all of the activity on the account.
print("Action 7: Nancy Pelosi gets bored of the app and decides to delete the account.")
query7 = """
MATCH (p:Person)
WHERE p.firstname = {name}
DETACH DELETE p
"""
data7 = new_graph.run(query7, name="Nancy")
# Action 8: Barack Obama decides that he does not want random people following him and therefore decides to change his account mode to private.
print("Action 8: Barack Obama decides that he does not want random people following him and therefore decides to change his account mode to private.")
query8 = """
MATCH (p:Person)
WHERE p.firstname = {name}
SET p.mode = "Private"
RETURN p
"""
data8= new_graph.run(query8, name="Barack")
for d8 in data8:
	print(d8)

new_graph.delete_all()
