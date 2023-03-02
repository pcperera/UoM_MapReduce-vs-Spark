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

1. ssh -i ~/vockey.pem hadoop@ec2-34-239-248-169.compute-1.amazonaws.com
2. scp -i "~/vockey.pem" Spark/*.py hadoop@ec2-34-239-248-169.compute-1.amazonaws.com:~/
3. spark-submit load-and-process.py

![results.png](Spark%2Fresults.png)


#### Evaluation

![Heterogeneous batch runtime vs Iteration.png](evaluation%2FHeterogeneous%20batch%20runtime%20vs%20Iteration.png)

![Homogeneous query average runtime.png](evaluation%2FHomogeneous%20query%20average%20runtime.png)

![Homogeneous query total runtime in 5 iterations.png](evaluation%2FHomogeneous%20query%20total%20runtime%20in%205%20iterations.png)