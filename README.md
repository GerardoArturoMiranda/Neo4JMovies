# Neo4J Movies
 The following program was made with Pyhton. 
 The main Database is NEO4j and as a Cache Memory REDIS was used. 
 For running the program: 
   1.- Download the csv file. https://www.kaggle.com/shivamb/netflix-shows 
   2.- Install NEO4J 
   3.- Install Redis 
   4.- Install NEO4J SHELL for populating the database.
   5.- In th Neo4J Folder of the project you need to uncomment these lines. 
  dbms.security.procedures.whitelist=apoc.coll.*,apoc.load.* 
  dbms.security.procedures.unrestricted=apoc.* 
  dbms.jvm.additional=-Djdk.tls.rejectClientInitiatedRenegotiation=true 
  dbms.windows_service_name=neo4j 
  apoc.import.file.enabled=true 
   6.- Use the code from the Keynote to import the csv File 

