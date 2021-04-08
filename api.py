import redis
from neo4j import GraphDatabase
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
driverRedis = redis.Redis(connection_pool=pool)
driverNeo4j = GraphDatabase.driver(uri="bolt://localhost:7687",auth=("gerardoMiranda", "Ec0wcz:)"),encrypted = False)
print(str(driverRedis.ping()))
class Api(object):
    def finalizacion(self):
        driverNeo4j.close()
    #Queries to obtain detailed information about each of the entities in the database.
    def obtenerInfoPelicula(self,nombrePelicula):
        try:
            pelicula = driverRedis.get(nombrePelicula)
            if(pelicula is None):
                print("La información no se encuentra en Caché, \n consultando información con Neo4j.")
                for record in driverNeo4j.session().run("match(m:Movie) where m.title= $nombrePelicula return m", nombrePelicula = nombrePelicula):
                    driverRedis.set(nombrePelicula, "Informacion de la pelicula o show:\n->-> ->-> ->"+str(record["m"]))
                    driverRedis.expire(nombrePelicula,900)
                print("Se han guardado datos en chaché, duración de caché: 15 minutos.\n");
                print("INFORMACIÓN GENERAL \n")
                print("LLAVE: " + str(nombrePelicula)+"\n")
                return str(driverRedis.get(nombrePelicula))
            else:
                print("La información se encontraba vigente en caché.\n")
                return str(pelicula)
        except Exception as e:
            return {"Error ": "Descripción : {}".format(e)}
    def obtenerInfoDePeliculaDeActor(self,nombreActor):
        try:
            peliculasParticipacion = driverRedis.get(nombreActor)
            if(peliculasParticipacion is None):
                print("La información no se encuentra en Caché, \n consultando información con Neo4j.")
                for record in driverNeo4j.session().run("match(a:Actor)-[:PARTICIPATED_ON]->(m:Movie) where a.name=$nombreActor return m", nombreActor = nombreActor):
                    driverRedis.set(nombreActor, "Informacion de la pelicula o show en la que participa:\n"+ str(nombreActor)+" ->-> ->-> ->"+str(record["m"]))
                    driverRedis.expire(nombreActor,900)
                print("Se han guardado datos en chaché, duración de caché: 15 minutos.\n");
                print("INFORMACIÓN DE PELÍCULAS DE ACTOR \n")
                print("LLAVE: " + str(nombreActor)+"\n")
                return str(driverRedis.get(nombreActor))
            else:
                print("La información se encontraba vigente en caché.\n")
                return str(peliculasParticipacion)
        except Exception as e:
            return {"Error ": "Descripción : {}".format(e)}
    def obtenerInfoPais(self, nombrePelicula):
        try:
            paisPelicula = driverRedis.get(str("pais")+nombrePelicula)
            if(paisPelicula is None):
                print("La información no se encuentra en Caché, \n consultando información con Neo4j.")
                for record in driverNeo4j.session().run("match(m:Movie)-[:CREATED_ON]->(c:Country) where m.title=$nombrePelicula return c", nombrePelicula = nombrePelicula):
                    driverRedis.set(str("pais")+nombrePelicula, "Informacion del país de la pelicula o show es:\n->-> ->-> ->"+str(record["c"]))
                    driverRedis.expire(str("pais")+nombrePelicula,900)
                print("Se han guardado datos en chaché, duración de caché: 15 minutos.\n");
                print("INFORMACIÓN DE PAÍS DE PELÍCULA \n")
                print("LLAVE: pais"+nombrePelicula +"\n")
                return str(driverRedis.get(str("pais")+nombrePelicula))
            else:
                print("La información se encontraba vigente en caché.\n")
                return str(paisPelicula)
        except Exception as e:
            return {"Error ": "Descripción : {}".format(e)}
    
    def obtenerInfoDuracion(self, nombrePelicula):
        try:
            duracionPelicula = driverRedis.get(str("duracion")+nombrePelicula)
            if(duracionPelicula is None):
                print("La información no se encuentra en Caché, \n consultando información con Neo4j.")
                for record in driverNeo4j.session().run("match(m:Movie)-[:LASTS_AROUND]->(d:Duration) where m.title=$nombrePelicula return d", nombrePelicula = nombrePelicula):
                    driverRedis.set(str("duracion")+nombrePelicula, "Informacion de duración de la pelicula o show es:\n->-> ->-> ->"+str(record["d"]))
                    driverRedis.expire(str("duracion")+nombrePelicula,900)
                print("Se han guardado datos en chaché, duración de caché: 15 minutos.\n");
                print("INFORMACIÓN DE DURACIÓN DE PELÍCULA \n")
                print("LLAVE: duración"+nombrePelicula+"\n")
                return str(driverRedis.get(str("duracion")+nombrePelicula))
            else:
                print("La información se encontraba vigente en caché.\n")
                return str(duracionPelicula)
        except Exception as e:
            return {"Error ": "Descripción : {}".format(e)}
    def obtenerInfoGenero(self, nombrePelicula):
        try:
            generoPelicula = driverRedis.get(str("genero")+nombrePelicula)
            if(generoPelicula is None):
                print("La información no se encuentra en Caché, \n consultando información con Neo4j.")
                for record in driverNeo4j.session().run("match(m:Movie)-[:BELONGS_TO]->(g:Genre) where m.title=$nombrePelicula return g", nombrePelicula = nombrePelicula):
                    driverRedis.set(str("genero")+nombrePelicula, "Informacion del genero de la pelicula o show es:\n->-> ->-> ->"+str(record["g"]))
                    driverRedis.expire(str("genero")+nombrePelicula,900)
                print("Se han guardado datos en chaché, duración de caché: 15 minutos.\n");
                print("INFORMACIÓN DE GÉNERO DE PELÍCULA \n")
                print("LLAVE: genero"+nombrePelicula+"\n")
                return str(driverRedis.get(str("genero")+nombrePelicula))
            else:
                print("La información se encontraba vigente en caché.\n")
                return str(generoPelicula)
        except Exception as e:
            return {"Error ": "Descripción : {}".format(e)}
    
    def obtenerInfoTipo(self, nombrePelicula):
        try:
            tipoPelicula = driverRedis.get(str("tipo")+nombrePelicula)
            if(tipoPelicula is None):
                print("La información no se encuentra en Caché, \n consultando información con Neo4j.")
                for record in driverNeo4j.session().run("match(m:Movie)-[:IS_A]->(t:Type) where m.title=$nombrePelicula return t", nombrePelicula = nombrePelicula):
                    driverRedis.set(str("tipo")+nombrePelicula, "Informacion del tipo de la pelicula o show es:\n->-> ->-> ->"+str(record["t"]))
                    driverRedis.expire(str("tipo")+nombrePelicula,900)
                print("Se han guardado datos en chaché, duración de caché: 15 minutos.\n");
                print("INFORMACIÓN DE TIPO DE PELÍCULA \n")
                print("LLAVE: tipo"+nombrePelicula+"\n")
                return str(driverRedis.get(str("tipo")+nombrePelicula))
            else:
                print("La información se encontraba vigente en caché.\n")
                return str(tipoPelicula)
        except Exception as e:
            return {"Error ": "Descripción : {}".format(e)}
        
    def obtenerInfoAno(self, nombrePelicula):
        try:
            print("ano"+nombrePelicula)
            anoPelicula = driverRedis.get(str("ano")+nombrePelicula)
            if(anoPelicula is None):
                print("La información no se encuentra en Caché, \n consultando información con Neo4j.")
                for record in driverNeo4j.session().run("match(m:Movie)-[:PUBLISHED_IN]->(y:Year) where m.title=$nombrePelicula return y", nombrePelicula = nombrePelicula):
                    driverRedis.set(str("ano")+nombrePelicula, "Informacion del año de la pelicula o show es:\n->-> ->-> ->"+str(record["y"]))
                    driverRedis.expire(str("ano")+nombrePelicula,900)
                print("Se han guardado datos en chaché, duración de caché: 15 minutos.\n");
                print("INFORMACIÓN DE AÑO DE PELÍCULA \n")
                print("LLAVE: ano"+nombrePelicula+"\n")
                return str(driverRedis.get(str("ano")+nombrePelicula))
            else:
                print("La información se encontraba vigente en caché.\n")
                return str(anoPelicula)
        except Exception as e:
            return {"Error ": "Descripción : {}".format(e)}
    
    def obtenerInfoRating(self, nombrePelicula):
        try:
            print("rating"+nombrePelicula)
            ratingPelicula = driverRedis.get(str("rating")+nombrePelicula)
            if(ratingPelicula is None):
                print("La información no se encuentra en Caché, \n consultando información con Neo4j.")
                for record in driverNeo4j.session().run("match(m:Movie)-[:CLASIFICATES_AS]->(r:Rating) where m.title=$nombrePelicula return r", nombrePelicula = nombrePelicula):
                    driverRedis.set(str("rating")+nombrePelicula, "Informacion del rating de la pelicula o show es:\n-> -> -> -> ->"+str(record["r"]))
                    driverRedis.expire(str("rating")+nombrePelicula,900)
                print("INFORMACIÓN DE RATING DE PELÍCULA \n")
                print("LLAVE: rating"+nombrePelicula+"\n")
                print("Se han guardado datos en chaché, duración de caché: 15 minutos.\n");
                return str(driverRedis.get(str("rating")+nombrePelicula))
            else:
                print("La información se encontraba vigente en caché.\n")
                return str(ratingPelicula)
        except Exception as e:
            return {"Error ": "Descripción : {}".format(e)}
        #Here we end the methods to obtain detailed information about the database
        #3 Queries to obtain statistics about the database.
    def query1(self,anoEstadistico):
        try:
            query = driverRedis.get(str(anoEstadistico))
            if(query is None):
                print("La información no se encuentra en Caché, \n consultando información con Neo4j.")
                for record in driverNeo4j.session().run("match(y:Year)<-[n:PUBLISHED_IN]-(m:Movie) where y.release_year= $anoEstadistico return count(n)", anoEstadistico = anoEstadistico):
                    driverRedis.set(str(anoEstadistico), str(record["count(n)"]))
                    driverRedis.expire(str(anoEstadistico),900)
                print("Se han guardado datos en chaché, duración de caché: 15 minutos.\n");
                print("INFORMACIÓN DE NÚMERO DE PELÍCULAS QUE POSEE LA BASE DE DATOS DE  "+ anoEstadistico+" \n")
                print("LLAVE: " + str(anoEstadistico)+"\n")
                return str(driverRedis.get(str(anoEstadistico)))
            else:
                print("La información se encontraba vigente en caché.\n")
                return str(query)
        except Exception as e:
            return {"Error ": "Descripción : {}".format(e)}
    def query2(self,generoEstadistico):
        try:
            query = driverRedis.get(str(generoEstadistico))
            if(query is None):
                print("La información no se encuentra en Caché, \n consultando información con Neo4j.")
                for record in driverNeo4j.session().run("match(g:Genre)<-[n:BELONGS_TO]-(m:Movie) where g.genre= $generoEstadistico return count(n)", generoEstadistico = generoEstadistico):
                    driverRedis.set(str(generoEstadistico), str(record["count(n)"]))
                    driverRedis.expire(str(generoEstadistico),900)
                print("Se han guardado datos en chaché, duración de caché: 15 minutos.\n");
                print("INFORMACIÓN DE NÚMERO DE PELÍCULAS QUE POSEE LA BASE DE DATOS DE  "+ generoEstadistico+" \n")
                print("LLAVE: " + str(generoEstadistico)+"\n")
                return str(driverRedis.get(str(generoEstadistico)))
            else:
                print("La información se encontraba vigente en caché.\n")
                return str(query)
        except Exception as e:
            return {"Error ": "Descripción : {}".format(e)}
    def query3(self,actorEstadistico):
        try:
            query = driverRedis.get(str(actorEstadistico))
            if(query is None):
                print("La información no se encuentra en Caché, \n consultando información con Neo4j.")
                for record in driverNeo4j.session().run("match(m:Movie)<-[n:PARTICIPATED_ON]-(a:Actor) where a.name= $actorEstadistico return count(n)", actorEstadistico = actorEstadistico):
                    driverRedis.set(str(actorEstadistico), str(record["count(n)"]))
                    driverRedis.expire(str(actorEstadistico),900)
                print("Se han guardado datos en chaché, duración de caché: 15 minutos.\n");
                print("INFORMACIÓN DE NÚMERO DE PELÍCULAS QUE POSEE LA BASE DE DATOS DE  "+ actorEstadistico+" \n")
                print("LLAVE: " + str(actorEstadistico)+"\n")
                return str(driverRedis.get(str(actorEstadistico)))
            else:
                print("La información se encontraba vigente en caché.\n")
                return str(query)
        except Exception as e:
            return {"Error ": "Descripción : {}".format(e)}
    #HERE WE ENDTHE 3 Queries to obtain statistics about the database.
    #REGISTER A MOVIE
    def registrarPelicula(self,title, description, date_added, show_id, typeh, rating, country, duration, release_year, name, genre, actores):
        driverNeo4j.session().run("CREATE (movie: Movie{show_id: $show_id, title: $title, date_added: $date_added, description: $description})", show_id=show_id, title=title, date_added = date_added, description = description)
        if(len(actores)>1):
            for i in actores:
                aName =str(actores.pop())
                driverNeo4j.session().run("Match (m:Movie) where m.title=$title create (a:Actor{name:$aName})-[:PARTICIPATED_ON]->(m)", title= title, aName = aName)
        driverNeo4j.session().run("Match (m:Movie) where m.title=$title create (c:Country{country:$country})<-[:CREATED_ON]-(m)", title =title, country = country)
        driverNeo4j.session().run("Match (m:Movie) where m.title=$title create (d:Director{name:$name})<-[:DIRECTED_BY]-(m)", title =title, name = name)
        driverNeo4j.session().run("Match (m:Movie) where m.title=$title create (d:Duration{duration:$duration})<-[:LASTS_AROUND]-(m)", title =title, duration = duration)
        driverNeo4j.session().run("Match (m:Movie) where m.title=$title create (r:Rating{rating:$rating})<-[:CLASIFICATES_AS]-(m)", title =title, rating = rating)
        driverNeo4j.session().run("Match (m:Movie) where m.title=$title create (g:Genre{genre:$genre})<-[:BELONGS_TO]-(m)", title =title, genre = genre)
        if(release_year>2020):
            driverNeo4j.session().run("Match (m:Movie) where m.title=$title create (y:Year{release_year:$release_year})<-[:PUBLISHED_IN]-(m)", title =title, release_year = release_year)
        else:
            driverNeo4j.session().run("Match (m:Movie) where m.title=$title Match (y:Year) where y.release_year:$release_year create (y)<-[:PUBLISHED_IN]-(m)", title =title, release_year = release_year)
        driverNeo4j.session().run("Match (m:Movie) where m.title=$title create (t:Type{type:$typeh})<-[:IS_A]-(m)", title =title, typeh = typeh)
        print("R E G I S T R O     C O M P L E T O,      C H E C A R   E N  N E O 4 J")
    #UPDATING A MOVIE
    def actualizarPelicula(self,title, description, date_added, show_id):
        try:
            driverNeo4j.session().run("MATCH (m:Movie{title:$title})SET m.show_id=$show_id, m.description=$description, m.date_added=$date_added", show_id=show_id, title=title, date_added = date_added, description = description)
        except Exception as e:
            return {"Error ": "Descripción : {}".format(e)}
    
        
