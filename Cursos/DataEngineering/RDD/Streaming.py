from pyspark.streaming import StreamingContext
from pyspark import SparkContext


sc = SparkContext("local[2]", "Contagem")
ssc = StreamingContext(sc, 10)

pesquisa = ssc.textFileStream('../Arquivos/stream/')

contagem = pesquisa.flatMap(lambda palavra: palavra.split(' '))
contagem = contagem.map(lambda palavra: (palavra, 1))
contagem = contagem.reduceByKey(lambda a, b: a + b)

contagem.pprint()

ssc.start()

ssc.awaitTermination()
