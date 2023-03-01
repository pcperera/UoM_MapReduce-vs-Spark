### Commands

#### MapReduce

![cluster.png](MapReduce%2Fcluster.png)

1. ssh -i "~/vockey.pem" hadoop@ec2-3-88-33-238.compute-1.amazonaws.com
2. scp -i "~/vockey.pem" data/DelayedFlights-updated.csv hadoop@ec2-3-88-33-238.compute-1.amazonaws.com:~/
3. scp -i "~/vockey.pem" MapReduce/*.hql MapReduce/*.sh hadoop@ec2-3-88-33-238.compute-1.amazonaws.com:~/
4. hadoop fs -mkdir /flights
5. hadoop fs -put DelayedFlights-updated.csv /flights/
6. hive
7. source load-delayed-flights.hql;
8. chmod +x run-queries.sh
9. ./run-queries.sh > run-queries.log

![results.png](MapReduce%2Fresults.png)


#### Spark

![cluster.png](Spark%2Fcluster.png)

1. ssh -i ~/vockey.pem hadoop@ec2-3-80-225-46.compute-1.amazonaws.com
2. scp -i "~/vockey.pem" Spark/*.py hadoop@ec2-3-80-225-46.compute-1.amazonaws.com:~/
3. pyspark load.py
4. pyspark queries.py





